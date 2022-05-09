import os
import cv2

data_list = os.listdir("content\\crop_jpg_2")

for data in data_list:
    src = cv2.imread(f"content\\crop_jpg_2\\{data}", cv2.IMREAD_UNCHANGED)
    height = src.shape[0]
    new_width = int(src.shape[1] * 20 / height)
    dsize = (new_width, 20)
    output = cv2.resize(src, dsize)
    cv2.imwrite(f"content\\resized_files\\{data}", output)
