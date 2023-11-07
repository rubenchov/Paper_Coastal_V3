import cv2
import os
import numpy as np
from tensorflow import keras

def preprocess (array):
  """
  Normalizes the supplied array and reshapes it into the appropriate format.
  """
  array = array.astype("float32") / 255.0
  array = np.reshape(array, (len(array), 512, 512, 1))
  return array

autoencoder = keras.models.load_model('P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Scripts/Autoencoder_despeckling.h5')

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/2.Rescaled"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/3.Filtered"
count = 0

for file_name in files_names:
    #print(file_name)
    image_path = input_images_path + "/" + file_name
    print(count)
    img2 = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img2 is None:
        continue
    
    print(count)
    new = np.zeros(img2.shape)
    h, w = new.shape
    tamano = 512
    for i in range(0, h, tamano):
        if i > (h - tamano):
            i = h - tamano
        for j in range(0, w, tamano):
              if j > (w - tamano):
                j = w - tamano
              #print(i,j)
              roi = img2[i:i+tamano, j:j+tamano]
              val1 = cv2.resize(roi, (tamano, tamano))
              sfs = []
              sfs.append(val1)
              valid = np.array(sfs, dtype = np.uint8)
              valida = preprocess(valid)
              prediction = autoencoder.predict(valida)
              imgfilt = prediction.reshape(tamano, tamano) * 255
              new[i:i+tamano, j:j+tamano] = imgfilt
              
    cv2.imwrite(output_images_path + "/" + file_name, new)
    count += 1