# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:40:10 2022

@author: Abdul Qayyum
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