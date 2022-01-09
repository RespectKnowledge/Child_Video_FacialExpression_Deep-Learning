# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:41:35 2022

@author: AbdulQayyum
"""

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