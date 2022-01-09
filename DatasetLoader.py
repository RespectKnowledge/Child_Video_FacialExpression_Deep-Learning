# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:46:15 2022

@author: Abdul Qayyum
"""

#%% # dataset loader for 2d images in pytorch
import os
import numpy as np
import cv2
from PIL import Image
import torch
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
import glob

class Facialdata(torch.utils.data.Dataset):
    def __init__(self,rootpath,training=True):
        self.rootpath=rootpath
        self.training=training
        classes1=glob.glob(os.path.join(trainPath,"*")) # extract list of folder
        labels = np.arange(5)
        self.trainList = []
        self.labelList = []
        for i,c in enumerate(classes1):
            #print(c)
            files=glob.glob(os.path.join(c,'*.png')) # extract samples from each folder
            for f in files:
                self.trainList.append(f)  # path of image samples
                self.labelList.append(float(labels[i])) # appened numbers as class labels
           
    def __getitem__(self,idx):
        
        image_path=self.trainList[idx] # clases paths
        img=cv2.imread(image_path) # read image
        label=self.labelList[idx] # read labels
        
        if self.training:
            self.transform=transforms.Compose([
                transforms.ToPILImage(),
                transforms.Resize((224, 224)),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.RandomVerticalFlip(p=0.5),
                transforms.ToTensor(), 
                transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
                ])
            
        img=self.transform(img)
        #label=label
        return img,label
    
    def __len__(self):
        return len(self.trainList)
    
trainPath='D:\\facialexpression\\FacialTT\\train2dclasses'
data_train=Facialdata(rootpath=trainPath)
imge,label=data_train[0]
print(imge.shape)
print(label)

train_loader=DataLoader(data_train,batch_size=4,shuffle=True)
im_batch,label_batch=next(iter(train_loader))
print(im_batch.shape)
print(label_batch.long()) # we can convert labels into long 