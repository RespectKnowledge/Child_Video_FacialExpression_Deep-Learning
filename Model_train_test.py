# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:49:20 2022

@author: Abdul Qayyum
"""

#%% models
# Data science tools
import numpy as np
import pandas as pd
import os

import torch
import torch.nn as nn
import torchvision.datasets 
from torchvision.datasets import ImageFolder
import torch
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor,Resize,Normalize
from torchvision.transforms import transforms
import os
import matplotlib.pyplot as plt
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
import seaborn as sns


import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from efficientnet_pytorch import EfficientNet
model = EfficientNet.from_pretrained('efficientnet-b7',num_classes=5) 
#summary(model, input_size=(3, 224, 224), batch_size=20, device='cuda')


optimizer=torch.optim.Adam(model.parameters(),lr=0.001)
criterion=nn.CrossEntropyLoss()

def train_epoch(model,Train_loader, optimizer,criterion):
    model.train()
    #model.to(device)
    
    running_loss=0.0
    start_time=time.time()
    for batch_idx,(data,target) in enumerate (Train_loader):
        output=model(data)
        loss=criterion(output,target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss+=loss
    end_time=time.time()
    
    running_loss/=len(Train_loader)
    print("training loss", running_loss,'Time',end_time-start_time,'z')
    return running_loss


def test_model(model,Test_loader,criterion):
    with torch.no_grad():
        model.eval()
        running_loss=0.0
        total_predictions=0.0
        correct_prediction=0.0
        for batch_idx,(data,target) in enumerate (Test_loader):
            outputs=model(data)
            _,predicted=torch.max(outputs.data,1)
            total_predictions+=target.size(0)
            correct_prediction+=(predicted==target).sum().item()
            loss=criterion(outputs,target).detach()
            running_loss+=loss.item()
        running_loss/=len(Test_loader)
        acc=(correct_prediction/total_predictions)*100.0
        print("testing loss", running_loss)
        print("testing accuracy", acc,'%')
        return running_loss,acc


import time
loss_train=[]
loss_test_acc=[]
n_epochs=2
for i in range(n_epochs):
    trep=train_epoch(model,Train_loader, optimizer,criterion)
    tesrep=test_model(model,Test_loader,criterion)
    loss_train.append(trep)
    loss_test_acc.append(tesrep)