# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 07:05:42 2019

@author: moona
"""


#%% ########################### Frames extraction from videos ###########################
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
import cv2
import os
mydir='D:\\facialexpression\\LIRISChildrenSpontaneousFacialExpressionVideoDatabase\\LIRISChildrenSpontaneousFacialExpressionVideoDatabase\\videos_208'
saveimage='D:\\facialexpression\\saveimagesnew'
import natsort
dlist1=os.listdir(mydir)
print(natsort.natsorted(dlist1,reverse=False))
image_num = 0
for file in natsort.natsorted(dlist1,reverse=False):
    print(natsort.natsorted(dlist1,reverse=False))
    path=os.path.join(mydir, file)
    cap = cv2.VideoCapture(path)
    fps=25
    frame_num = 0
    output_dir=saveimage
    ff=path.split('\\')[5]
    save_path=os.path.join(saveimage,ff)
    createFolder(save_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if frame_num % (fps // 25) == 0:
                cv2.imwrite(save_path+'\\'+"image{}.jpg".format(image_num),frame)
                #cv2.imwrite(save_path+'\\'+"img/frame %d.jpg" % image_num,frame)
                image_num += 1
        else:
            break
        frame_num += 1

#%%  ###################Make the number of classes based on each video cataegory ########################################3
import os
from fnmatch import fnmatch
import natsort
import cv2
########################################################### Fear Videos ##############################################3
root = 'D:\\facialexpression\\videofolders'
dlist1=os.listdir(root)
natsort.natsorted(dlist1,reverse=False)
subs='fear'
# using filter() + lambda  
# to get string with substring  
res = list(filter(lambda x: subs in x, natsort.natsorted(dlist1,reverse=False))) 
saveslices='D:\\facialexpression\\FearClass'
d=1
for uu in res:
    tt=os.path.join(root,uu)
    tt1=os.listdir(tt)
    for imge in natsort.natsorted(tt1,reverse=False):
        n= cv2.imread(os.path.join(tt,imge))
        filename = "%d.png"%d
        cv2.imwrite(saveslices+'\\'+filename,n) # save images
        d+=1 


########################################################### surprise Videos ##############################################3
import os
from fnmatch import fnmatch
import natsort
import cv2
root = 'D:\\facialexpression\\videofolders'
dlist1=os.listdir(root)
natsort.natsorted(dlist1,reverse=False)
subs1='surprise'
# using filter() + lambda  
# to get string with substring  
res1 = list(filter(lambda x: subs1 in x, natsort.natsorted(dlist1,reverse=False))) 
saveslices='D:\\facialexpression\\SurpriseClass'
d=1
for uu in res1:
    tt=os.path.join(root,uu)
    tt1=os.listdir(tt)
    for imge in natsort.natsorted(tt1,reverse=False):
        n= cv2.imread(os.path.join(tt,imge))
        filename = "%d.png"%d
        cv2.imwrite(saveslices+'\\'+filename,n) # save images
        d+=1 

########################################################### Sad Videos ##############################################3
import os
from fnmatch import fnmatch
import natsort
import cv2
root = 'D:\\facialexpression\\videofolders'
dlist1=os.listdir(root)
natsort.natsorted(dlist1,reverse=False)
subs11='sad'
# using filter() + lambda  
# to get string with substring  
res11 = list(filter(lambda x: subs11 in x, natsort.natsorted(dlist1,reverse=False))) 
saveslices='D:\\facialexpression\\SadClass'
d=1
for uu in res11:
    tt=os.path.join(root,uu)
    tt1=os.listdir(tt)
    for imge in natsort.natsorted(tt1,reverse=False):
        n= cv2.imread(os.path.join(tt,imge))
        filename = "%d.png"%d
        cv2.imwrite(saveslices+'\\'+filename,n) # save images
        d+=1 

########################################################### Happy Videos ##############################################3
import os
from fnmatch import fnmatch
import natsort
import cv2
root = 'D:\\facialexpression\\videofolders'
dlist1=os.listdir(root)
natsort.natsorted(dlist1,reverse=False)
subs111='happy'
# using filter() + lambda  
# to get string with substring  
res111 = list(filter(lambda x: subs111 in x, natsort.natsorted(dlist1,reverse=False))) 
saveslices='D:\\facialexpression\\HappyClass'
d=1
for uu in res111:
    tt=os.path.join(root,uu)
    tt1=os.listdir(tt)
    for imge in natsort.natsorted(tt1,reverse=False):
        n= cv2.imread(os.path.join(tt,imge))
        filename = "%d.png"%d
        cv2.imwrite(saveslices+'\\'+filename,n) # save images
        d+=1 

########################################################### disgust Videos ##############################################3
import os
from fnmatch import fnmatch
import natsort
import cv2
root = 'D:\\facialexpression\\videofolders'
dlist1=os.listdir(root)
natsort.natsorted(dlist1,reverse=False)
subs1111='disgust'
# using filter() + lambda  
# to get string with substring  
res1111 = list(filter(lambda x: subs1111 in x, natsort.natsorted(dlist1,reverse=False))) 
saveslices='D:\\facialexpression\\DisgustClass'
d=1
for uu in res1111:
    tt=os.path.join(root,uu)
    tt1=os.listdir(tt)
    for imge in natsort.natsorted(tt1,reverse=False):
        n= cv2.imread(os.path.join(tt,imge))
        filename = "%d.png"%d
        cv2.imwrite(saveslices+'\\'+filename,n) # save images
        d+=1 
        
        
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Convert class size according to Deep Network size ################################3       
        
        
import numpy as np
import scipy.misc  
import cv2
import numpy
import glob
import pylab as plt
import os
#import png
import pydicom
import numpy as np
from pydicom.tag import Tag
import time
from PIL import Image, ImageOps           
import numpy as np
import scipy.misc  
import cv2
import numpy
import glob
import pylab as plt
import os
#from glob import glob
#
folders = glob.glob('D:\\facialexpression\\SurpriseClass\\*')
foldername='D:\\facialexpression\\256surprizeclass'
#FolderList=os.listdir(folders)
#imagenames__list = []
#img_mask = 'D:\\AQProject\\imagedata/*.png'
#img_names = glob(folders)
#imgnames = sorted(glob.glob("/PATH_TO_IMAGES/*.png"))
import natsort
d=1
for folder in natsort.natsorted(folders,reverse=False):
    img=Image.open(folder)
    im=img
    old_size = img.size
    new_size = (256, 256)
    new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
    new_im.paste(img, ((new_size[0]-old_size[0])//2,(new_size[1]-old_size[1])//2))
    filename = "%d.png"%d
    #cv2.imwrite(foldername+'\\'+filename,im)
    new_im.save(foldername+'\\'+filename)
    d+=1
#        #imagenames_list.append(f)              
        
        
        
        
        
        