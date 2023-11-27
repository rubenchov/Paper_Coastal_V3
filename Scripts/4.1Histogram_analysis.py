import cv2 
import numpy as np
import os
import matplotlib.pylab as plt

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/4.Composite"
files_names = os.listdir(input_images_path)
print(files_names)

max_level = 255
pixel_value = np.linspace(0,max_level,max_level+1) # possichannelle entries

fig, axs = plt.subplots(1, 3, figsize=(12,4))

for channel in range(0,3):
  total = []
  
  for file in files_names:
    image_path = input_images_path + "/" + file
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        continue 
    channels = cv2.split(img)
    total.append(channels[channel])
    
  for i in range(0,16):
    # We calculate the histogram of the current channel.
    histogram = cv2.calcHist([total[i]],[0],None,[max_level+1],[0,256])
    axs[channel].plot(pixel_value, histogram)
    '''
    if channel == 0:
      axs[2].plot(pixel_value, histogram)
    if channel == 1:
      axs[1].plot(pixel_value, histogram)
    if channel == 2:
      axs[0].plot(pixel_value, histogram)
    '''
  axs[channel].grid()  # Set grid for each subplot
  axs[channel].set_xlabel('Pixel Value')
  axs[channel].set_ylabel('Frequency')
  axs[channel].set_xlim(0,256)

axs[0].set_title('img_vv')
axs[1].set_title('img_vh')
axs[2].set_title('img_ratio')

plt.tight_layout()