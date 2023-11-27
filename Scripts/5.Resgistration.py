import cv2
import numpy as np
import os
import imutils

max = 10000
def align_image(image, template, maxFeatures=max, keepPercent=0.2, debug=False):
    # convert both the input image and template to grayscale
    imageGray = image.copy()
    templateGray = template.copy()
    # use ORB to detect keypoints and extract (binary) local
    # invariant features
    orb = cv2.ORB_create(maxFeatures)
    (kpsA, descsA) = orb.detectAndCompute(imageGray, None)
    (kpsB, descsB) = orb.detectAndCompute(templateGray, None)
    # match the features
    method = cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
    matcher = cv2.DescriptorMatcher_create(method)
    matches = matcher.match(descsA, descsB, None)
    # sort the matches by their distance (the smaller the distance,
    # the "more similar" the features are)
    matches = sorted(matches, key=lambda x: x.distance)
    # keep only the top matches
    keep = int(len(matches) * keepPercent)
    matches = matches[:keep]
    # check to see if we should visualize the matched keypoints
    if debug:
        matchedVis = cv2.drawMatches(image, kpsA, template, kpsB,
                                     matches, None)
        matchedVis = imutils.resize(matchedVis, width=1000)
        cv2.imshow("Matched Keypoints", matchedVis)
        cv2.waitKey(0)

    # allocate memory for the keypoints (x, y)-coordinates from the
    # top matches -- we'll use these coordinates to compute our
    # homography matrix
    ptsA = np.zeros((len(matches), 2), dtype="float")
    ptsB = np.zeros((len(matches), 2), dtype="float")
    # loop over the top matches
    for (i, m) in enumerate(matches):
        # indicate that the two keypoints in the respective images
        # map to each other
        ptsA[i] = kpsA[m.queryIdx].pt
        ptsB[i] = kpsB[m.trainIdx].pt

    # compute the homography matrix between the two sets of matched
    # points
    (H, mask) = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC)
    # use the homography matrix to align the images
    (h, w) = template.shape[:2]
    aligned = cv2.warpPerspective(image, H, (w, h))
    # return the aligned image
    return aligned

input_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/5.Classified"
files_names = os.listdir(input_images_path)
print(files_names)

output_images_path = "P:/.shortcut-targets-by-id/11U9sP9uc_lmRAe7rgiV0UB_1__qEdYzt/Paper_Coastal_V3/Images/6.Registration"

path_img_base = '20160611.png'
base = cv2.imread(input_images_path + '/' + path_img_base)  # Reference image.

count = 0
trim = 50

# =============================================================================
# The registration process accommodates the image with respect to a reference according to its 
# dimensions, therefore sometimes it fills with non-existent stripes, due to this the borders are cropped by 50 pixels
# =============================================================================

for file_name in files_names:
    #print(file_name)
    image_path = input_images_path + "/" + file_name
    print(count)
    img = cv2.imread(image_path)
    if img is None:
        continue    
    
    if file_name == path_img_base:
        h, w, _ = base.shape
        base_trim = base[trim:h-trim, trim:w-trim]
        cv2.imwrite(output_images_path + "/" + file_name, base_trim)
    else:
        aligned = align_image(img, base, maxFeatures=max, debug=False) # Image to be aligned. 
        h, w, _ = aligned.shape
        image_trim = aligned[trim:h-trim, trim:w-trim]
        cv2.imwrite(output_images_path + "/" + file_name, image_trim)
    count += 1  