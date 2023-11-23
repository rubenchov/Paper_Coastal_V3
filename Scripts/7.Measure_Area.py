# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:50:51 2023

@author: Esteban VC
"""

import cv2
import numpy as np
import os
import pandas as pd 

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/6.Registration"
files_names = os.listdir(input_images_path)
print(files_names)

output_df_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/7.Result"

factory = 137.6173/1000000 # Pixel to km^2 conversion factor
count = 0
names = []
waters = []
non_waters = []
areas = []

for file_name in files_names:
    print(file_name)
    image_path = input_images_path + "/" + file_name
    # print(count)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue    

    h, w = img.shape
    area = h * w
    non_water = np.count_nonzero(img)
    water = area - non_water
    name = file_name.split('.')
    names.append(name[0])
    waters.append(water)
    non_waters.append(non_water)
    areas.append(area) 
    count += 1  
    
waters = np.array(waters)*factory
non_waters = np.array(non_waters)*factory
areas = np.array(areas)*factory
df = pd.DataFrame(list(zip(names, waters, non_waters, areas)), columns = ['ImageName', 'AreaWater(Km^2)', 'AreaNonWater(Km^2)', 'AreaAll(Km^2)'])
# df.to_csv(output_df_path + '/Areas.csv')
df.to_excel(output_df_path + '/Areas.xlsx')
