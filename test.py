import numpy as np
import pandas as pd
import os

test_img_path = "./yolo_demo/images/testing"

img_name_list = []
for i in os.listdir(test_img_path):
    img_name = i.replace(".jpg","").replace("S","").replace("T","")
    img_name_list.append(img_name)