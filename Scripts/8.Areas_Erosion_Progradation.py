# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 17:50:10 2023

@author: Esteban VC
"""

import cv2
import numpy as np
import os
import pandas as pd 

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/6.Registration/"

output_df_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/7.Result"

factory = 137.6173/1000000 # Pixel to km^2 conversion factor

dirname = os.path.join(os.getcwd(), input_images_path)
files = next(os.walk(input_images_path))[2]
files.sort()
print(files)
eros_l = []
prograd_l = []
names = []

for i in range(1, len(files)): #Descarta la primera
  print(files[i])
  img_base = cv2.imread(input_images_path + files[i-1], cv2.IMREAD_GRAYSCALE)  # Reference image.
  img_analize = cv2.imread(input_images_path + files[i], cv2.IMREAD_GRAYSCALE)  # Analysis image.
  if img_analize is None:
      continue   
  if img_base is None:
      continue   
  prograd = cv2.subtract(img_base, img_analize)
  eros = cv2.subtract(img_analize, img_base)

  h, w = img_base.shape
  h, w = prograd.shape
  area = h * w
  prograd_c = np.count_nonzero(prograd)
  eros_c = np.count_nonzero(eros)
  one, two = files[i].split('.')
  names.append(one)
  prograd_l.append(prograd_c)
  eros_l.append(eros_c)
  
eros_l = np.array(eros_l)*factory
prograd_l = np.array(prograd_l)*factory

df = pd.DataFrame(list(zip(names, prograd_l, eros_l,)), columns =['ImageName', 'Prograd_Area', 'Eros_Area'])
df.to_excel(output_df_path + '/Areas_Erosion_Progradation.xlsx')