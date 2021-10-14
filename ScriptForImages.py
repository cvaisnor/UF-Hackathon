import numpy as np
import cv2 
import pandas as pd
import sys

# from specific directory, grab image

file_name = sys.argv[1]

file_year = file_name.split('.')[1:2]

file_month = file_name.split('.')[2:3]

print(type(file_year), file_month)

exit()
bgr_image = cv2.imread(file_name)

hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

# Global algae mask parameters
lower_global = np.array([5,0,0])
upper_global = np.array([150,255,255])

maskGlobal = cv2.inRange(hsv, lower_global, upper_global)
resGlobal = cv2.bitwise_or(bgr_image, bgr_image, mask=maskGlobal)


gray_global = cv2.cvtColor(resGlobal, cv2.COLOR_BGR2GRAY)

# Returns outs which is the image
ret, outs_global = cv2.threshold(src = gray_global, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY_INV)

total_pixel_count = outs_global.size

globalCount = total_pixel_count - cv2.countNonZero(outs_global) # Save global number of algae pixels


# Intense algae mask paramters
lower_intense = np.array([1,0,0])
upper_intense = np.array([33,255,255])

maskIntense = cv2.inRange(hsv, lower_intense, upper_intense)
resIntense = cv2.bitwise_or(bgr_image, bgr_image, mask=maskIntense)

gray_intense = cv2.cvtColor(resIntense, cv2.COLOR_BGR2GRAY)

# Returns outs which is the image
ret, outs_intense = cv2.threshold(src = gray_intense, thresh = 0, maxval = 255, type = cv2.THRESH_BINARY_INV)

intense_pixel_count = outs_intense.size

intenseCount = intense_pixel_count - cv2.countNonZero(outs_intense) # Save intense number of algae pixels


df = read_csv(file)

df.append()


# append file_name[date] to df
# append globalCount to df
# append intenseCount to df

