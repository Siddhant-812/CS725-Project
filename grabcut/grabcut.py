import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import json
import csv
import os

json_data = 'Topview_pred.json'
view = "Top"

for i in range(2):
    # Open and read the JSON file
    with open(json_data, 'r') as file:
        data = json.load(file)

    xywh_list = []
    for obj in data:
        path = obj["image_name"]
        name=obj["object_name"]
        x = obj["x"]
        y = obj["y"]
        w = obj["w"]
        h = obj["h"]
        conf = obj["conf"]
        xywh_list.append((x, y, w, h,name))
        

    l = len(xywh_list)

    img = cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)
    img_copy = img
    assert img is not None, "File could not be read, check with os.path.exists()"
    p, q, r = img.shape

    # Create a CSV file to store non-zero pixel counts
    if(view=="Top"):
        csv_filename = "topview_pixels.csv"
    else:
        csv_filename = "sideview_pixels.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image Name','Bounding Box Objects', 'Total Pixel Count', 'Row Pixel Count Sum', 'Max Row Pixel Count', 'Bounding Box (H + W)', 'Height'])

    for i in range(0, l):
        
        img = img_copy
        p, q, r = img.shape
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        w0 = int((xywh_list[i][2]) * q)
        h0 = int((xywh_list[i][3]) * p)
        x0 = int((xywh_list[i][0] - xywh_list[i][2] / 2) * q)
        y0 = int((xywh_list[i][1] - xywh_list[i][3] / 2) * p)
        rect = (x0, y0, w0, h0)
        #print(rect)
        cv.grabCut(img, mask, rect, bgdModel, fgdModel, 10, cv.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == cv.GC_PR_BGD) | (mask == cv.GC_BGD), 0, 1).astype('uint8')
        img1 = img * mask2[:, :, np.newaxis]

        # Count non-zero pixels in the mask
        total_pixel_count = np.count_nonzero(mask2)
        rowwise_pixel_count = np.count_nonzero(mask2, axis=1)
        sum_rowwise_pixel_count = sum(j*j for j in rowwise_pixel_count)
        max_rowwise_pixel_count = np.amax(rowwise_pixel_count)

        #print(rowwise_pixel_count)
            
            
        # Display and save the segmented image
        plt.imshow(img1), plt.colorbar(), plt.show()

        # Append the non-zero pixel count to the CSV file
        with open(csv_filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([xywh_list[i][4], total_pixel_count, sum_rowwise_pixel_count, max_rowwise_pixel_count, w0+h0, h0])
        
        json_data = 'Sideview_pred.json'
        view = "Side"

