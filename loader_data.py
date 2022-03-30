import imp
from os import uname
import torch.utils.data
import torch
import torch.nn as nn
import random
from data import COCODataset, ValTransform

subset_len = 200
sample_method = 'random'
batch_size = 1


valdataset = COCODataset(
        data_dir="./imagenet",
        json_file="instances_val2017.json",
        name="val2017",
        img_size=(640, 640),
        preproc=ValTransform(
            rgb_means=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)
        ),
    )
sampler = torch.utils.data.SequentialSampler(valdataset)



if subset_len:
        if sample_method == 'random':
            dataset = torch.utils.data.Subset(valdataset, random.sample(range(0, len(valdataset)), subset_len))
        else:
            dataset = torch.utils.data.Subset(valdataset, list(range(subset_len)))

loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, sampler=sampler, shuffle=False)




