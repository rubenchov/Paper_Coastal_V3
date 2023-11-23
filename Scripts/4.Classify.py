# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:41:40 2023

@author: Esteban VC
"""

import cv2 
import numpy as np
import os
import matplotlib.pylab as plt

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/4.Composite"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/5.Classified"

count = 0
total = []
b = 1 # channel chosen to make the classification

for file_name in files_names:
    #print(file_name)
    image_path = input_images_path + "/" + file_name
    print(count)
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        continue    

    channels = cv2.split(img)
    total.append(channels[b])
    ret, th = cv2.threshold(total[count],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # We apply a classification with the Otssu algorithm
    #print(ret)
    th = np.where(th == 255, 0, 255)   
    cv2.imwrite(output_images_path + "/" + file_name, th)
    count += 1  