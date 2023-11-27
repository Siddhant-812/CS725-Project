import pandas as pd
import math
import json
import csv

cls_name = { "apple" : "ellipsoid", "banana" : "irregular", "bread" : "column",  "bun" : "irregular", "coin" : "",
            "doughnut" : "irregular", "egg" : "ellipsoid", "fired_dough_twist":"irregular", "grape":"irregular", "lemon" : "ellipsoid", "mango" : "irregular",
            "litchi":"irregular", "mooncake":"column", "orange" : "ellipsoid", "pear" : "irregular", "peach":"ellipsoid", "plum" : "ellipsoid", "qiwi" : "ellipsoid",
            "sachima" : "column", "tomato" : "ellipsoid" }


  #[Bounding Box Objects,Total Pixel Count,Row Pixel Count Sum,Max Row Pixel Count,Bounding Box (H + W)]
json_data = 'combined_file.json'
with open(json_data, 'r') as file:
    # Load the JSON data into a dictionary
    data_dict = json.load(file)

res={}
file_path = 'volumes.csv'

for key,value in data_dict.items():

    if (value[0][0]['Bounding Box Objects']=='coin'):
        alphas = 5/int(value[0][0]['Bounding Box (H + W)'])
    elif (value[0][1]['Bounding Box Objects']=='coin'):
        alphas = 5/int(value[0][1]['Bounding Box (H + W)'])
    
    if (value[1][0]['Bounding Box Objects']=='coin'):
        alphat = 5/int(value[1][0]['Bounding Box (H + W)'])
    elif (value[1][1]['Bounding Box Objects']=='coin'):
        alphat = 5/int(value[1][1]['Bounding Box (H + W)'])
    
    if (value[0][0]['Bounding Box Objects']=='coin'):
        ls = int(value[0][1]['Row Pixel Count Sum'])
    elif (value[0][1]['Bounding Box Objects']=='coin'):
        ls = int(value[0][0]['Row Pixel Count Sum'])

    if (value[1][0]['Bounding Box Objects']=='coin'):
        st = int(value[1][1]['Total Pixel Count'])
    elif (value[1][1]['Bounding Box Objects']=='coin'):
        st = int(value[1][0]['Total Pixel Count'])

    if (value[0][0]['Bounding Box Objects']=='coin'):
        hs = int(value[0][1]['Height'])
    elif (value[0][1]['Bounding Box Objects']=='coin'):
        hs = int(value[0][0]['Height'])

    if (value[0][0]['Bounding Box Objects']=='coin'):
        lmax = int(value[0][1]['Max Row Pixel Count'])
    elif (value[0][1]['Bounding Box Objects']=='coin'):
        lmax = int(value[0][0]['Max Row Pixel Count'])

    if (value[0][0]['Bounding Box Objects']=='coin'):
        shape = cls_name[value[0][1]['Bounding Box Objects']]
    elif (value[0][1]['Bounding Box Objects']=='coin'):
        shape = cls_name[value[0][0]['Bounding Box Objects']]

    if(shape=='ellipsoid'):
        volume = math.pi*(alphas**3)*ls/4
    elif(shape=='column'):
        volume = st*(alphat**2)*hs*alphas
    elif(shape=='irregular'):
        volume = st*(alphat**2)*alphas*ls/(lmax**2)
     
    res[key]=volume

    
with open(file_path, 'w', newline='') as csvfile:
    # Create a CSV writer
    csv_writer = csv.writer(csvfile)

    # Write the dictionary values to the CSV file
    for key, value in res.items():
        csv_writer.writerow([key, value])
