import cv2 
import numpy as np
import os

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/1.Original"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/2.Rescaled"
count = 0

for file_name in files_names:
    #print(file_name)
    image_path = input_images_path + "/" + file_name
    print(count)
    # print()
    image = cv2.imread(image_path)
    if image is None:
        continue
    # Comment the following 5 lines if you don't need them
    # print('Image shape: ', img.shape)
    # print('Image type: ', img.dtype)
    # print('Image max pixel value: ', np.max(img))
    # print('Image mean pixel value: ', np.mean(img))
    # print('Image min pixel value: ', np.min(img))

    img2 = image.astype(np.single) #Change datatype to real values
    escala_display = np.mean(img2) * 3.0 #Mean value times 3
    min = np.min(img2) #Calculation of minimum value of pixel of all the image
    img2[img2 > escala_display] = escala_display #Values higher or equal to mean*3 are reasigned to mean*3
    img2[img2 < min] = 0 #Values lower than min(img) are reasigned to zero. Other values will remain the same
    img3 = 255.0 * (img2 / escala_display) #Normalized to 0-1 and then rescaled 0-255
    img4 = img3.astype(np.uint8) #Change datatype to 8-bit unsigned integer

    pathsplit = file_name.split('.png') #Split the path of the image [name, '.png']
    imgpathscaled = output_images_path + '/' +pathsplit[0] + '_scaled.png' #Added string '_scaled.png' to new name of image to save
    cv2.imwrite(imgpathscaled, img4)
    # cv2.imshow( 'brillo',imgpathscaled)
    count += 1