
# =============================================================================
# Compose (based on https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-overview/polarimetry)
# =============================================================================

import cv2 
import numpy as np
import os

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/3.Filtered"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/4.Composite"
count = 0

for file_VH, file_VV in zip(files_names[::2], files_names[1::2]):

    print(file_VH, file_VV)
    image_path_VH = input_images_path + "/" + file_VH
    image_path_VV = input_images_path + "/" + file_VV
    # print(count)
    image_VH = cv2.imread(image_path_VV, cv2.IMREAD_GRAYSCALE)
    image_VV = cv2.imread(image_path_VH, cv2.IMREAD_GRAYSCALE)
    if image_VH is None:
        continue    
    if image_VV is None:
        continue
    
    one, two = file_VH.split('.')
    one, two = one.split('_')
    imgVH_s = image_VH.astype(np.single)
    imgVV_s = image_VV.astype(np.single)
    ratio = np.divide(imgVV_s, imgVH_s)
    ratio_normalize = ((ratio - np.min(ratio))/(np.max(ratio) - np.min(ratio)))*255
    ratio = ratio_normalize.astype(np.uint8)
    image_merge = cv2.merge([ratio, image_VH, image_VV]) # B, G, R
    cv2.imwrite(output_images_path + '/' + one + '.png', image_merge)
    count += 1