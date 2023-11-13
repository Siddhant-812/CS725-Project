import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import json
import csv

json_data = 'output.json'

# Open and read the JSON file
with open(json_data, 'r') as file:
    data = json.load(file)

xywh_list = []
for obj in data:
    name=obj["object_name"]
    x = obj["x"]
    y = obj["y"]
    w = obj["w"]
    h = obj["h"]
    xywh_list.append((x, y, w, h,name))

l = len(xywh_list)
img = cv.cvtColor(cv.imread('yolo_demo/images/testing/mix010S(1).jpg'), cv.COLOR_BGR2RGB)
img_copy = img
assert img is not None, "File could not be read, check with os.path.exists()"
p, q, r = img.shape

# Create a CSV file to store non-zero pixel counts
csv_filename = "non_zero_pixels.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Bounding Box Objects', 'Non-Zero Pixels Count'])

for i in range(0, l):
    img = img_copy
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    w0 = int((xywh_list[i][2]) * q)
    h0 = int((xywh_list[i][3]) * p)
    x0 = int((xywh_list[i][0] - xywh_list[i][2] / 2) * q)
    y0 = int((xywh_list[i][1] - xywh_list[i][3] / 2) * p)
    rect = (x0, y0, w0, h0)
    cv.grabCut(img, mask, rect, bgdModel, fgdModel, 10, cv.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == cv.GC_PR_BGD) | (mask == cv.GC_BGD), 0, 1).astype('uint8')
    img1 = img * mask2[:, :, np.newaxis]

    # Count non-zero pixels in the mask
    non_zero_pixel_count = np.count_nonzero(mask2)

    # Display and save the segmented image
    plt.imshow(img1), plt.colorbar(), plt.show()

    # Append the non-zero pixel count to the CSV file
    with open(csv_filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([xywh_list[i][4], non_zero_pixel_count])
