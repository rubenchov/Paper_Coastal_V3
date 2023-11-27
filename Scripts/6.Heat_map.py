import cv2
import numpy as np
import os

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/6.Registration"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/7.Result/Heat"

path_img_base = '20160611.png'
img_temp = cv2.imread(input_images_path + '/' + path_img_base, cv2.IMREAD_GRAYSCALE)
avg = np.zeros(img_temp.shape, dtype=np.single)

count = 0

for file_name in files_names:
    #print(file_name)
    image_path = input_images_path + "/" + file_name
    print(count)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        continue    
    
    img_temp = cv2.resize(img, (avg.shape[1], avg.shape[0]), interpolation=cv2.INTER_AREA)
    avg += img_temp
    count += 1  
    
avg_out = 255 * (avg - np.min(avg)) / (np.max(avg) - np.min(avg))
avg_out = avg_out.astype(np.uint8)

#Colormaps: https://docs.opencv.org/2.4.11/modules/contrib/doc/facerec/colormaps.html
imC = cv2.applyColorMap(avg_out, cv2.COLORMAP_HOT)
#cv2.imwrite(new_path + 'heatmap_color_Filt.png', imC)

# cv2.imshow('Heat map', cv2.resize(imC, (720,920)))    
cv2.imwrite(output_images_path + "/Heat_map.png" , imC)
