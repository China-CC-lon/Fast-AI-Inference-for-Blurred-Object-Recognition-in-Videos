# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class YOLOX(torch.nn.Module):
    def __init__(self):
        super(YOLOX, self).__init__()
        self.module_0 = py_nndct.nn.Input() #YOLOX::input_0
        self.module_1 = py_nndct.nn.strided_slice() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/15479
        self.module_2 = py_nndct.nn.strided_slice() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/15489
        self.module_3 = py_nndct.nn.strided_slice() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/15499
        self.module_4 = py_nndct.nn.strided_slice() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/15509
        self.module_5 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/input.1
        self.module_6 = py_nndct.nn.Conv2d(in_channels=12, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/BaseConv[conv]/Conv2d[conv]/input.2
        self.module_8 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Focus[stem]/BaseConv[conv]/ReLU[act]/input.4
        self.module_9 = py_nndct.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/BaseConv[0]/Conv2d[conv]/input.5
        self.module_11 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/BaseConv[0]/ReLU[act]/input.7
        self.module_12 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.8
        self.module_14 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv1]/ReLU[act]/input.12
        self.module_15 = py_nndct.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.10
        self.module_17 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv2]/ReLU[act]/15621
        self.module_18 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.13
        self.module_20 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.15
        self.module_21 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.16
        self.module_23 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/15673
        self.module_24 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/15675
        self.module_25 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/input.18
        self.module_26 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.19
        self.module_28 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark2]/CSPLayer[1]/BaseConv[conv3]/ReLU[act]/input.21
        self.module_29 = py_nndct.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/BaseConv[0]/Conv2d[conv]/input.22
        self.module_31 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/BaseConv[0]/ReLU[act]/input.24
        self.module_32 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.25
        self.module_34 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv1]/ReLU[act]/input.29
        self.module_35 = py_nndct.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.27
        self.module_37 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv2]/ReLU[act]/15782
        self.module_38 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.30
        self.module_40 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.32
        self.module_41 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.33
        self.module_43 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/15834
        self.module_44 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/input.35
        self.module_45 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.36
        self.module_47 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/ReLU[act]/input.38
        self.module_48 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.39
        self.module_50 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/ReLU[act]/15888
        self.module_51 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/input.41
        self.module_52 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.42
        self.module_54 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/ReLU[act]/input.44
        self.module_55 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/Conv2d[conv]/input.45
        self.module_57 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/ReLU[act]/15942
        self.module_58 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/15944
        self.module_59 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/input.47
        self.module_60 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.48
        self.module_62 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark3]/CSPLayer[1]/BaseConv[conv3]/ReLU[act]/input.50
        self.module_63 = py_nndct.nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/BaseConv[0]/Conv2d[conv]/input.51
        self.module_65 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/BaseConv[0]/ReLU[act]/input.53
        self.module_66 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv1]/Conv2d[conv]/input.54
        self.module_68 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv1]/ReLU[act]/input.58
        self.module_69 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv2]/Conv2d[conv]/input.56
        self.module_71 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv2]/ReLU[act]/16051
        self.module_72 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.59
        self.module_74 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.61
        self.module_75 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.62
        self.module_77 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/16103
        self.module_78 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[0]/input.64
        self.module_79 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.65
        self.module_81 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv1]/ReLU[act]/input.67
        self.module_82 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.68
        self.module_84 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/BaseConv[conv2]/ReLU[act]/16157
        self.module_85 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[1]/input.70
        self.module_86 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/Conv2d[conv]/input.71
        self.module_88 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv1]/ReLU[act]/input.73
        self.module_89 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/Conv2d[conv]/input.74
        self.module_91 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/BaseConv[conv2]/ReLU[act]/16211
        self.module_92 = py_nndct.nn.Add() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/Sequential[m]/Bottleneck[2]/16213
        self.module_93 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/input.76
        self.module_94 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv3]/Conv2d[conv]/input.77
        self.module_96 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark4]/CSPLayer[1]/BaseConv[conv3]/ReLU[act]/input.79
        self.module_97 = py_nndct.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/BaseConv[0]/Conv2d[conv]/input.80
        self.module_99 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/BaseConv[0]/ReLU[act]/input.82
        self.module_100 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv1]/Conv2d[conv]/input.83
        self.module_102 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv1]/ReLU[act]/16294
        self.module_103 = py_nndct.nn.MaxPool2d(kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/MaxPool2d[m]/ModuleList[0]/16308
        self.module_104 = py_nndct.nn.MaxPool2d(kernel_size=[9, 9], stride=[1, 1], padding=[4, 4], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/MaxPool2d[m]/ModuleList[1]/16322
        self.module_105 = py_nndct.nn.MaxPool2d(kernel_size=[13, 13], stride=[1, 1], padding=[6, 6], dilation=[1, 1], ceil_mode=False) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/MaxPool2d[m]/ModuleList[2]/16336
        self.module_106 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/input.85
        self.module_107 = py_nndct.nn.Conv2d(in_channels=1024, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv2]/Conv2d[conv]/input.86
        self.module_109 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/SPPBottleneck[1]/BaseConv[conv2]/ReLU[act]/input.88
        self.module_110 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv1]/Conv2d[conv]/input.89
        self.module_112 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv1]/ReLU[act]/input.93
        self.module_113 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv2]/Conv2d[conv]/input.91
        self.module_115 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv2]/ReLU[act]/16417
        self.module_116 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.94
        self.module_118 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.96
        self.module_119 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.97
        self.module_121 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/16469
        self.module_122 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/input.99
        self.module_123 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv3]/Conv2d[conv]/input.100
        self.module_125 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPDarknet[backbone]/Sequential[dark5]/CSPLayer[2]/BaseConv[conv3]/ReLU[act]/input.102
        self.module_126 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[lateral_conv0]/Conv2d[conv]/input.103
        self.module_128 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[lateral_conv0]/ReLU[act]/input.105
        self.module_129 = py_nndct.nn.Interpolate() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Upsample[upsample]/16533
        self.module_130 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/input.106
        self.module_131 = py_nndct.nn.Conv2d(in_channels=512, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/BaseConv[conv1]/Conv2d[conv]/input.107
        self.module_133 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/BaseConv[conv1]/ReLU[act]/input.111
        self.module_134 = py_nndct.nn.Conv2d(in_channels=512, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/BaseConv[conv2]/Conv2d[conv]/input.109
        self.module_136 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/BaseConv[conv2]/ReLU[act]/16588
        self.module_137 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.112
        self.module_139 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.114
        self.module_140 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.115
        self.module_142 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/16640
        self.module_143 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/input.117
        self.module_144 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/BaseConv[conv3]/Conv2d[conv]/input.118
        self.module_146 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p4]/BaseConv[conv3]/ReLU[act]/input.120
        self.module_147 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[reduce_conv1]/Conv2d[conv]/input.121
        self.module_149 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[reduce_conv1]/ReLU[act]/input.123
        self.module_150 = py_nndct.nn.Interpolate() #YOLOX::YOLOX/YOLOPAFPN[backbone]/Upsample[upsample]/16700
        self.module_151 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/input.124
        self.module_152 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/BaseConv[conv1]/Conv2d[conv]/input.125
        self.module_154 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/BaseConv[conv1]/ReLU[act]/input.129
        self.module_155 = py_nndct.nn.Conv2d(in_channels=256, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/BaseConv[conv2]/Conv2d[conv]/input.127
        self.module_157 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/BaseConv[conv2]/ReLU[act]/16755
        self.module_158 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.130
        self.module_160 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.132
        self.module_161 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.133
        self.module_163 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/16807
        self.module_164 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/input.135
        self.module_165 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/BaseConv[conv3]/Conv2d[conv]/input.136
        self.module_167 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_p3]/BaseConv[conv3]/ReLU[act]/input.138
        self.module_168 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv2]/Conv2d[conv]/input.139
        self.module_170 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv2]/ReLU[act]/16862
        self.module_171 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/input.141
        self.module_172 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/BaseConv[conv1]/Conv2d[conv]/input.142
        self.module_174 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/BaseConv[conv1]/ReLU[act]/input.146
        self.module_175 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/BaseConv[conv2]/Conv2d[conv]/input.144
        self.module_177 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/BaseConv[conv2]/ReLU[act]/16917
        self.module_178 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.147
        self.module_180 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.149
        self.module_181 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.150
        self.module_183 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/16969
        self.module_184 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/input.152
        self.module_185 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/BaseConv[conv3]/Conv2d[conv]/input.153
        self.module_187 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n3]/BaseConv[conv3]/ReLU[act]/input.155
        self.module_188 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv1]/Conv2d[conv]/input.156
        self.module_190 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/BaseConv[bu_conv1]/ReLU[act]/17024
        self.module_191 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/input.158
        self.module_192 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/BaseConv[conv1]/Conv2d[conv]/input.159
        self.module_194 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/BaseConv[conv1]/ReLU[act]/input.163
        self.module_195 = py_nndct.nn.Conv2d(in_channels=512, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/BaseConv[conv2]/Conv2d[conv]/input.161
        self.module_197 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/BaseConv[conv2]/ReLU[act]/17079
        self.module_198 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/Conv2d[conv]/input.164
        self.module_200 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv1]/ReLU[act]/input.166
        self.module_201 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/Conv2d[conv]/input.167
        self.module_203 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/Sequential[m]/Bottleneck[0]/BaseConv[conv2]/ReLU[act]/17131
        self.module_204 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/input.169
        self.module_205 = py_nndct.nn.Conv2d(in_channels=512, out_channels=512, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/BaseConv[conv3]/Conv2d[conv]/input.170
        self.module_207 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOPAFPN[backbone]/CSPLayer[C3_n4]/BaseConv[conv3]/ReLU[act]/input.202
        self.module_208 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[0]/Conv2d[conv]/input.172
        self.module_210 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[0]/ReLU[act]/input.174
        self.module_211 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[0]/Conv2d[conv]/input.175
        self.module_213 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[0]/ReLU[act]/input.177
        self.module_214 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[1]/Conv2d[conv]/input.178
        self.module_216 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[0]/BaseConv[1]/ReLU[act]/input.180
        self.module_217 = py_nndct.nn.Conv2d(in_channels=128, out_channels=80, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[0]/17261
        self.module_218 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[0]/Conv2d[conv]/input.181
        self.module_220 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[0]/ReLU[act]/input.183
        self.module_221 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[1]/Conv2d[conv]/input.184
        self.module_223 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[0]/BaseConv[1]/ReLU[act]/input.186
        self.module_224 = py_nndct.nn.Conv2d(in_channels=128, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[0]/17332
        self.module_225 = py_nndct.nn.Conv2d(in_channels=128, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[0]/17351
        self.module_226 = py_nndct.nn.Sigmoid() #YOLOX::YOLOX/YOLOXHead[head]/17352
        self.module_227 = py_nndct.nn.Sigmoid() #YOLOX::YOLOX/YOLOXHead[head]/17353
        self.module_228 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/17356
        self.module_229 = py_nndct.nn.Conv2d(in_channels=256, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[1]/Conv2d[conv]/input.187
        self.module_231 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[1]/ReLU[act]/input.189
        self.module_232 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[0]/Conv2d[conv]/input.190
        self.module_234 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[0]/ReLU[act]/input.192
        self.module_235 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[1]/Conv2d[conv]/input.193
        self.module_237 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[1]/BaseConv[1]/ReLU[act]/input.195
        self.module_238 = py_nndct.nn.Conv2d(in_channels=128, out_channels=80, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[1]/17453
        self.module_239 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[0]/Conv2d[conv]/input.196
        self.module_241 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[0]/ReLU[act]/input.198
        self.module_242 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[1]/Conv2d[conv]/input.199
        self.module_244 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[1]/BaseConv[1]/ReLU[act]/input.201
        self.module_245 = py_nndct.nn.Conv2d(in_channels=128, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[1]/17524
        self.module_246 = py_nndct.nn.Conv2d(in_channels=128, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[1]/17543
        self.module_247 = py_nndct.nn.Sigmoid() #YOLOX::YOLOX/YOLOXHead[head]/17544
        self.module_248 = py_nndct.nn.Sigmoid() #YOLOX::YOLOX/YOLOXHead[head]/17545
        self.module_249 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/17548
        self.module_250 = py_nndct.nn.Conv2d(in_channels=512, out_channels=128, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[2]/Conv2d[conv]/input.203
        self.module_252 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/BaseConv[stems]/ModuleList[2]/ReLU[act]/input.205
        self.module_253 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[0]/Conv2d[conv]/input.206
        self.module_255 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[0]/ReLU[act]/input.208
        self.module_256 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[1]/Conv2d[conv]/input.209
        self.module_258 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[cls_convs]/ModuleList[2]/BaseConv[1]/ReLU[act]/input.211
        self.module_259 = py_nndct.nn.Conv2d(in_channels=128, out_channels=80, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[cls_preds]/ModuleList[2]/17645
        self.module_260 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[0]/Conv2d[conv]/input.212
        self.module_262 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[0]/ReLU[act]/input.214
        self.module_263 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[1]/Conv2d[conv]/input.215
        self.module_265 = py_nndct.nn.ReLU(inplace=True) #YOLOX::YOLOX/YOLOXHead[head]/Sequential[reg_convs]/ModuleList[2]/BaseConv[1]/ReLU[act]/input
        self.module_266 = py_nndct.nn.Conv2d(in_channels=128, out_channels=4, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[reg_preds]/ModuleList[2]/17716
        self.module_267 = py_nndct.nn.Conv2d(in_channels=128, out_channels=1, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #YOLOX::YOLOX/YOLOXHead[head]/Conv2d[obj_preds]/ModuleList[2]/17735
        self.module_268 = py_nndct.nn.Sigmoid() #YOLOX::YOLOX/YOLOXHead[head]/17736
        self.module_269 = py_nndct.nn.Sigmoid() #YOLOX::YOLOX/YOLOXHead[head]/17737
        self.module_270 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/output
        self.module_271 = py_nndct.nn.Module('flatten') #YOLOX::YOLOX/YOLOXHead[head]/17779
        self.module_272 = py_nndct.nn.Module('flatten') #YOLOX::YOLOX/YOLOXHead[head]/17782
        self.module_273 = py_nndct.nn.Module('flatten') #YOLOX::YOLOX/YOLOXHead[head]/17785
        self.module_274 = py_nndct.nn.Cat() #YOLOX::YOLOX/YOLOXHead[head]/17788
        self.module_275 = py_nndct.nn.Module('permute') #YOLOX::YOLOX/YOLOXHead[head]/17793

    def forward(self, *args):
        self.output_module_0 = self.module_0(input=args[0])
        self.output_module_1 = self.module_1(start=[0,0,0,0], input=self.output_module_0, step=[1,1,2,2], end=[2147483647,2147483647,2147483647,2147483647])
        self.output_module_2 = self.module_2(start=[0,0,0,1], input=self.output_module_0, step=[1,1,2,2], end=[2147483647,2147483647,2147483647,2147483647])
        self.output_module_3 = self.module_3(start=[0,0,1,0], input=self.output_module_0, step=[1,1,2,2], end=[2147483647,2147483647,2147483647,2147483647])
        self.output_module_4 = self.module_4(start=[0,0,1,1], input=self.output_module_0, step=[1,1,2,2], end=[2147483647,2147483647,2147483647,2147483647])
        self.output_module_5 = self.module_5(tensors=[self.output_module_1,self.output_module_3,self.output_module_2,self.output_module_4], dim=1)
        self.output_module_6 = self.module_6(self.output_module_5)
        self.output_module_8 = self.module_8(self.output_module_6)
        self.output_module_9 = self.module_9(self.output_module_8)
        self.output_module_11 = self.module_11(self.output_module_9)
        self.output_module_12 = self.module_12(self.output_module_11)
        self.output_module_14 = self.module_14(self.output_module_12)
        self.output_module_15 = self.module_15(self.output_module_11)
        self.output_module_17 = self.module_17(self.output_module_15)
        self.output_module_18 = self.module_18(self.output_module_14)
        self.output_module_20 = self.module_20(self.output_module_18)
        self.output_module_21 = self.module_21(self.output_module_20)
        self.output_module_23 = self.module_23(self.output_module_21)
        self.output_module_24 = self.module_24(alpha=1, input=self.output_module_23, other=self.output_module_14)
        self.output_module_25 = self.module_25(tensors=[self.output_module_24,self.output_module_17], dim=1)
        self.output_module_26 = self.module_26(self.output_module_25)
        self.output_module_28 = self.module_28(self.output_module_26)
        self.output_module_29 = self.module_29(self.output_module_28)
        self.output_module_31 = self.module_31(self.output_module_29)
        self.output_module_32 = self.module_32(self.output_module_31)
        self.output_module_34 = self.module_34(self.output_module_32)
        self.output_module_35 = self.module_35(self.output_module_31)
        self.output_module_37 = self.module_37(self.output_module_35)
        self.output_module_38 = self.module_38(self.output_module_34)
        self.output_module_40 = self.module_40(self.output_module_38)
        self.output_module_41 = self.module_41(self.output_module_40)
        self.output_module_43 = self.module_43(self.output_module_41)
        self.output_module_44 = self.module_44(alpha=1, input=self.output_module_43, other=self.output_module_34)
        self.output_module_45 = self.module_45(self.output_module_44)
        self.output_module_47 = self.module_47(self.output_module_45)
        self.output_module_48 = self.module_48(self.output_module_47)
        self.output_module_50 = self.module_50(self.output_module_48)
        self.output_module_51 = self.module_51(alpha=1, input=self.output_module_50, other=self.output_module_44)
        self.output_module_52 = self.module_52(self.output_module_51)
        self.output_module_54 = self.module_54(self.output_module_52)
        self.output_module_55 = self.module_55(self.output_module_54)
        self.output_module_57 = self.module_57(self.output_module_55)
        self.output_module_58 = self.module_58(alpha=1, input=self.output_module_57, other=self.output_module_51)
        self.output_module_59 = self.module_59(tensors=[self.output_module_58,self.output_module_37], dim=1)
        self.output_module_60 = self.module_60(self.output_module_59)
        self.output_module_62 = self.module_62(self.output_module_60)
        self.output_module_63 = self.module_63(self.output_module_62)
        self.output_module_65 = self.module_65(self.output_module_63)
        self.output_module_66 = self.module_66(self.output_module_65)
        self.output_module_68 = self.module_68(self.output_module_66)
        self.output_module_69 = self.module_69(self.output_module_65)
        self.output_module_71 = self.module_71(self.output_module_69)
        self.output_module_72 = self.module_72(self.output_module_68)
        self.output_module_74 = self.module_74(self.output_module_72)
        self.output_module_75 = self.module_75(self.output_module_74)
        self.output_module_77 = self.module_77(self.output_module_75)
        self.output_module_78 = self.module_78(alpha=1, input=self.output_module_77, other=self.output_module_68)
        self.output_module_79 = self.module_79(self.output_module_78)
        self.output_module_81 = self.module_81(self.output_module_79)
        self.output_module_82 = self.module_82(self.output_module_81)
        self.output_module_84 = self.module_84(self.output_module_82)
        self.output_module_85 = self.module_85(alpha=1, input=self.output_module_84, other=self.output_module_78)
        self.output_module_86 = self.module_86(self.output_module_85)
        self.output_module_88 = self.module_88(self.output_module_86)
        self.output_module_89 = self.module_89(self.output_module_88)
        self.output_module_91 = self.module_91(self.output_module_89)
        self.output_module_92 = self.module_92(alpha=1, input=self.output_module_91, other=self.output_module_85)
        self.output_module_93 = self.module_93(tensors=[self.output_module_92,self.output_module_71], dim=1)
        self.output_module_94 = self.module_94(self.output_module_93)
        self.output_module_96 = self.module_96(self.output_module_94)
        self.output_module_97 = self.module_97(self.output_module_96)
        self.output_module_99 = self.module_99(self.output_module_97)
        self.output_module_100 = self.module_100(self.output_module_99)
        self.output_module_102 = self.module_102(self.output_module_100)
        self.output_module_103 = self.module_103(self.output_module_102)
        self.output_module_104 = self.module_104(self.output_module_102)
        self.output_module_105 = self.module_105(self.output_module_102)
        self.output_module_106 = self.module_106(tensors=[self.output_module_102,self.output_module_103,self.output_module_104,self.output_module_105], dim=1)
        self.output_module_107 = self.module_107(self.output_module_106)
        self.output_module_109 = self.module_109(self.output_module_107)
        self.output_module_110 = self.module_110(self.output_module_109)
        self.output_module_112 = self.module_112(self.output_module_110)
        self.output_module_113 = self.module_113(self.output_module_109)
        self.output_module_115 = self.module_115(self.output_module_113)
        self.output_module_116 = self.module_116(self.output_module_112)
        self.output_module_118 = self.module_118(self.output_module_116)
        self.output_module_119 = self.module_119(self.output_module_118)
        self.output_module_121 = self.module_121(self.output_module_119)
        self.output_module_122 = self.module_122(tensors=[self.output_module_121,self.output_module_115], dim=1)
        self.output_module_123 = self.module_123(self.output_module_122)
        self.output_module_125 = self.module_125(self.output_module_123)
        self.output_module_126 = self.module_126(self.output_module_125)
        self.output_module_128 = self.module_128(self.output_module_126)
        self.output_module_129 = self.module_129(input=self.output_module_128, size=None, scale_factor=[2.0,2.0], mode='nearest')
        self.output_module_130 = self.module_130(tensors=[self.output_module_129,self.output_module_96], dim=1)
        self.output_module_131 = self.module_131(self.output_module_130)
        self.output_module_133 = self.module_133(self.output_module_131)
        self.output_module_134 = self.module_134(self.output_module_130)
        self.output_module_136 = self.module_136(self.output_module_134)
        self.output_module_137 = self.module_137(self.output_module_133)
        self.output_module_139 = self.module_139(self.output_module_137)
        self.output_module_140 = self.module_140(self.output_module_139)
        self.output_module_142 = self.module_142(self.output_module_140)
        self.output_module_143 = self.module_143(tensors=[self.output_module_142,self.output_module_136], dim=1)
        self.output_module_144 = self.module_144(self.output_module_143)
        self.output_module_146 = self.module_146(self.output_module_144)
        self.output_module_147 = self.module_147(self.output_module_146)
        self.output_module_149 = self.module_149(self.output_module_147)
        self.output_module_150 = self.module_150(input=self.output_module_149, size=None, scale_factor=[2.0,2.0], mode='nearest')
        self.output_module_151 = self.module_151(tensors=[self.output_module_150,self.output_module_62], dim=1)
        self.output_module_152 = self.module_152(self.output_module_151)
        self.output_module_154 = self.module_154(self.output_module_152)
        self.output_module_155 = self.module_155(self.output_module_151)
        self.output_module_157 = self.module_157(self.output_module_155)
        self.output_module_158 = self.module_158(self.output_module_154)
        self.output_module_160 = self.module_160(self.output_module_158)
        self.output_module_161 = self.module_161(self.output_module_160)
        self.output_module_163 = self.module_163(self.output_module_161)
        self.output_module_164 = self.module_164(tensors=[self.output_module_163,self.output_module_157], dim=1)
        self.output_module_165 = self.module_165(self.output_module_164)
        self.output_module_167 = self.module_167(self.output_module_165)
        self.output_module_168 = self.module_168(self.output_module_167)
        self.output_module_170 = self.module_170(self.output_module_168)
        self.output_module_171 = self.module_171(tensors=[self.output_module_170,self.output_module_149], dim=1)
        self.output_module_172 = self.module_172(self.output_module_171)
        self.output_module_174 = self.module_174(self.output_module_172)
        self.output_module_175 = self.module_175(self.output_module_171)
        self.output_module_177 = self.module_177(self.output_module_175)
        self.output_module_178 = self.module_178(self.output_module_174)
        self.output_module_180 = self.module_180(self.output_module_178)
        self.output_module_181 = self.module_181(self.output_module_180)
        self.output_module_183 = self.module_183(self.output_module_181)
        self.output_module_184 = self.module_184(tensors=[self.output_module_183,self.output_module_177], dim=1)
        self.output_module_185 = self.module_185(self.output_module_184)
        self.output_module_187 = self.module_187(self.output_module_185)
        self.output_module_188 = self.module_188(self.output_module_187)
        self.output_module_190 = self.module_190(self.output_module_188)
        self.output_module_191 = self.module_191(tensors=[self.output_module_190,self.output_module_128], dim=1)
        self.output_module_192 = self.module_192(self.output_module_191)
        self.output_module_194 = self.module_194(self.output_module_192)
        self.output_module_195 = self.module_195(self.output_module_191)
        self.output_module_197 = self.module_197(self.output_module_195)
        self.output_module_198 = self.module_198(self.output_module_194)
        self.output_module_200 = self.module_200(self.output_module_198)
        self.output_module_201 = self.module_201(self.output_module_200)
        self.output_module_203 = self.module_203(self.output_module_201)
        self.output_module_204 = self.module_204(tensors=[self.output_module_203,self.output_module_197], dim=1)
        self.output_module_205 = self.module_205(self.output_module_204)
        self.output_module_207 = self.module_207(self.output_module_205)
        self.output_module_208 = self.module_208(self.output_module_167)
        self.output_module_210 = self.module_210(self.output_module_208)
        self.output_module_211 = self.module_211(self.output_module_210)
        self.output_module_213 = self.module_213(self.output_module_211)
        self.output_module_214 = self.module_214(self.output_module_213)
        self.output_module_216 = self.module_216(self.output_module_214)
        self.output_module_217 = self.module_217(self.output_module_216)
        self.output_module_218 = self.module_218(self.output_module_210)
        self.output_module_220 = self.module_220(self.output_module_218)
        self.output_module_221 = self.module_221(self.output_module_220)
        self.output_module_223 = self.module_223(self.output_module_221)
        self.output_module_224 = self.module_224(self.output_module_223)
        self.output_module_225 = self.module_225(self.output_module_223)
        self.output_module_226 = self.module_226(self.output_module_225)
        self.output_module_227 = self.module_227(self.output_module_217)
        self.output_module_228 = self.module_228(tensors=[self.output_module_224,self.output_module_226,self.output_module_227], dim=1)
        self.output_module_229 = self.module_229(self.output_module_187)
        self.output_module_231 = self.module_231(self.output_module_229)
        self.output_module_232 = self.module_232(self.output_module_231)
        self.output_module_234 = self.module_234(self.output_module_232)
        self.output_module_235 = self.module_235(self.output_module_234)
        self.output_module_237 = self.module_237(self.output_module_235)
        self.output_module_238 = self.module_238(self.output_module_237)
        self.output_module_239 = self.module_239(self.output_module_231)
        self.output_module_241 = self.module_241(self.output_module_239)
        self.output_module_242 = self.module_242(self.output_module_241)
        self.output_module_244 = self.module_244(self.output_module_242)
        self.output_module_245 = self.module_245(self.output_module_244)
        self.output_module_246 = self.module_246(self.output_module_244)
        self.output_module_247 = self.module_247(self.output_module_246)
        self.output_module_248 = self.module_248(self.output_module_238)
        self.output_module_249 = self.module_249(tensors=[self.output_module_245,self.output_module_247,self.output_module_248], dim=1)
        self.output_module_250 = self.module_250(self.output_module_207)
        self.output_module_252 = self.module_252(self.output_module_250)
        self.output_module_253 = self.module_253(self.output_module_252)
        self.output_module_255 = self.module_255(self.output_module_253)
        self.output_module_256 = self.module_256(self.output_module_255)
        self.output_module_258 = self.module_258(self.output_module_256)
        self.output_module_259 = self.module_259(self.output_module_258)
        self.output_module_260 = self.module_260(self.output_module_252)
        self.output_module_262 = self.module_262(self.output_module_260)
        self.output_module_263 = self.module_263(self.output_module_262)
        self.output_module_265 = self.module_265(self.output_module_263)
        self.output_module_266 = self.module_266(self.output_module_265)
        self.output_module_267 = self.module_267(self.output_module_265)
        self.output_module_268 = self.module_268(self.output_module_267)
        self.output_module_269 = self.module_269(self.output_module_259)
        self.output_module_270 = self.module_270(tensors=[self.output_module_266,self.output_module_268,self.output_module_269], dim=1)
        self.output_module_271 = self.module_271(input=self.output_module_228, start_dim=2, end_dim=3)
        self.output_module_272 = self.module_272(input=self.output_module_249, start_dim=2, end_dim=3)
        self.output_module_273 = self.module_273(input=self.output_module_270, start_dim=2, end_dim=3)
        self.output_module_274 = self.module_274(tensors=[self.output_module_271,self.output_module_272,self.output_module_273], dim=2)
        self.output_module_275 = self.module_275(input=self.output_module_274, dims=[0,2,1])
        return self.output_module_275
