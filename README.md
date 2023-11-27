# Paper_Coastal_V3

This repository contains the scripts and results used for the analysis of progradation and erosion in the Atrato River delta, supported in the paper 
`'Detection of erosion and progradation in the Colombian Atrato River Delta by using Sentinel-1 synthetic aperture radar data'`, where the methodology can be known in detail. At the root of the repository there are two folders, the first called `'Images'` which contains 7 folders with images of the step-by-step process of study, and a second called `'Scripts'` where 9 scripts are housed, with which the images of the first folder were obtained.

1. In the folder `'Images/1.Original'` there are 32 SAR images captured by Sentinel-1, taken in pairs from 11/06/2016 to 30/05/2023 in the VH and VV polarizations. By running the `'Scripts/1.Rescale_Intensity.py'` script, it is possible to have a better visualization of these images that are stored in `'Images/2.Rescaled'`(32 images).

2. The SAR images contain a characteristic speckle noise that must be eliminated, for this, we used an autoencoder located in `'Scripts/Autoencoder_despeckling.h5'` and executed by `'Scripts/2.Filter.py'` script that uses the images in `'Images/2.Rescaled'` folder (32 images). This autoencoder receives images of 512x512 pixels, by which it is necessary to divide each image, and after being filtered, they are saved in the folder `'Images/3.Filtered'`(32 images).

3. The process of composing the images after filtering them can be detailed in this [page](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-overview/polarimetry). This process is executed by `'Scripts/3.Compose.py'` script, which takes the images from `'Images/3.Filtered'` folder (32 images), and they are saved in `'Images/4.Composite'` folder (16 images).

4. To classify the water and non-water of the composite images, the Otsu algorithm was implemented in the script `'Scripts/4.Classify.py'` was used. The band for classification chosen was VV, the selection of this band is supported by the histogram analysis of the script `'Scripts/4.1Histogram_analysis.py'`. The chosen images are in `'Images/4.Composite'` folder and are saved in `'Images/5.Classified'`. The white area is the 'water' class, and the black area is the 'non-water' class.

5. To continue with the analysis, it was necessary to align all the images, as a reference, the oldest was taken dated 11/06/2016 and additionally, for display issues, 50 pixels were removed from each side of the image. This algorithm is executed in `'Scripts/5.Resgistration.py'` processing the images in the folder 'Images/5.Classified' and saving them in `'Images/6.Registration'`.

6. The `'Scripts/6.Heat_map.py'` script uses the images from `'Images/6.Registration'` to calculate the zones where there were changes in time, these changes can be seen in the heatmap saved in `'Images/7.Result/Heat/Heat_map.png'`.

7. In the `'Scripts/7.Measure_Area.py'` script the area in km^2 of the area classified as water and not water in `'Images/6.Registration'` images are measured, and these measurements are saved in an Excel file located at `'Images/7.Result/Areas.xlsx'`.

8. In the `'Scripts/8.Areas_Erosion_Progradation.py'` script, the area in km^2 of the erosion and progradation zones is measured, taking the images from `'Images/6.Registration'`, these measurements are saved in an Excel file located at `'Images/7.Result/Areas_Erosion_Progradation.xlsx'`.
