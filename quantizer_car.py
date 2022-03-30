import random
import re
import sys
import time
import pdb
from pytorch_nndct.apis import torch_quantizer

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torch.utils.data
from torch.utils.tensorboard import SummaryWriter

import os
import argparse
from models import YOLOX, YOLOPAFPN, YOLOXHead
from utils import MeterBuffer, ModelEMA, all_reduce_norm, get_model_info, get_rank, get_world_size, gpu_mem_usage, load_ckpt, occupy_mem, save_checkpoint, setup_logger, synchronize
from data import DataPrefetcher
from data import COCODataset, ValTransform
import evaluate
import datetime
import os
import time


from tensorboardX import SummaryWriter
from tqdm import tqdm

parser = argparse.ArgumentParser()
# vck5000 config
parser.add_argument('--data_dir',
                    default="./imagenet",
                    help='Data set directory, when quant_mode=calib, it is for calibration, while quant_mode=test it is for evaluation')
parser.add_argument('--model_dir',
                    default="./weights/yolox_s.pth",
                    help='Trained model file path. Download pretrained model from the following url and put it in model_dir specified path: https://download.pytorch.org/models/resnet18-5c106cde.pth')
parser.add_argument('--subset_len',
                    default=200,
                    type=int,
                    help='subset_len to evaluate model, using the whole validation dataset if it is not set')
parser.add_argument('--batch_size',
                    default=32,
                    type=int,
                    help='input data batch size to evaluate model')
parser.add_argument('--quant_mode',
                    default='calib',
                    choices=['float', 'calib', 'test'],
                    help='quantization mode. 0: no quantization, evaluate float model, calib: quantize, test: evaluate quantized model')
parser.add_argument('--fast_finetune',
                    dest='fast_finetune',
                    action='store_true',
                    help='fast finetune model before calibration')
parser.add_argument('--deploy',
                    dest='deploy',
                    action='store_true',
                    help='export xmodel for deployment')

args = parser.parse_args()


def load_data(subset_len=200,
              data_dir=None,
              join_file="instances_val2017.json",
              img_size=(640, 640),
              sample_method='random',
              batch_size=128,
              distributed=False,
              ):
    valdataset = COCODataset(
        data_dir=data_dir,
        json_file=join_file,
        name="val2017",
        img_size=img_size,
        preproc=ValTransform(
            rgb_means=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)
        ),
    )

    sampler = torch.utils.data.SequentialSampler(valdataset)
    loader = torch.utils.data.DataLoader(valdataset, batch_size=batch_size, sampler=sampler, shuffle=False)

    # if subset_len:
    #     if sample_method == 'random':
    #         dataset = torch.utils.data.Subset(valdataset, random.sample(range(0, len(valdataset)), subset_len))
    #     else:
    #         dataset = torch.utils.data.Subset(valdataset, list(range(subset_len)))

    # loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, sampler=sampler, shuffle=False)
    print(loader)
    return loader


def quantization(title='optimize',
                 model_name='yolox_s',
                 file_path='',
                 ):
    data_dir = args.data_dir
    quant_mode = args.quant_mode
    finetune = args.fast_finetune
    deploy = args.deploy
    batch_size = args.batch_size
    subset_len = args.subset_len

    def init_yolo(M):
        for m in M.modules():
            if isinstance(m, nn.BatchNorm2d):
                m.eps = 1e-3
                m.momentum = 0.03

    if quant_mode != 'test' and deploy:
        deploy = False
        print(r'Warning: Exporting xmodel needs to be done in quantization test mode, turn off it in this running!')
    if deploy and (batch_size != 1 or subset_len != 1):
        print(r'Warning: Exporting xmodel needs batch size to be 1 and only 1 iteration of inference, change them automatically!')
        batch_size = 1
        subset_len = 1

    in_channels = [256, 512, 1024]
    backbone = YOLOPAFPN(0.33, 0.50, in_channels=in_channels)
    head = YOLOXHead(80, 0.50, in_channels=in_channels)
    model = YOLOX(backbone, head)
    model.apply(init_yolo)
    model.head.initialize_biases(1e-2)
    model.eval()
    weights = torch.load(file_path, map_location='cpu')
    model.load_state_dict(weights['model'])

    inp = torch.randn([batch_size, 3, 640, 640])

    if quant_mode == 'float':
        quant_model = model
    else:
        quantizer = torch_quantizer(quant_mode, model, (inp), device=device)
        quant_model = quantizer.quant_model

    val_loader = load_data(subset_len=subset_len, batch_size=batch_size, sample_method='random', data_dir=data_dir)



    if finetune == True:
        ft_loader = load_data(subset_len=1024, batch_size=batch_size, sample_method=None, data_dir=data_dir)
        if quant_mode == 'calib':
            quantizer.fast_finetune(evaluate.init_main, (quant_model, ft_loader))
        elif quant_mode == 'test':
            quantizer.load_ft_param()
    
    sum = evaluate.init_main(model=quant_model, loader=val_loader)
    print("\n" + sum)


    if quant_mode == 'calib':
        quantizer.export_quant_config()
    if deploy:
        quantizer.export_xmodel(deploy_check=True)


if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_name = 'yolox_s'
    # file_path = os.path.join(args.model_dir, model_name + '.pth')

    feature_test = 'float model evalution'
    if args.quant_mode != 'float':
        feature_test = 'quantization'
        args.optimize = 1
        feature_test += 'with model evaluation'
    title = model_name + feature_test

    print("-------- Start {} test".format(model_name))

    quantization(
        title=title,
        file_path=args.model_dir,
    )

    print("-------- End of {} test ".format(model_name))






