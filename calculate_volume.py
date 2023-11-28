import pandas as pd
import math

cls_name = { "apple" : "ellipsoid", "banana" : "irregular", "bread" : "column",  "bun" : "irregular", "coin" : "",
            "doughnut" : "irregular", "egg" : "ellipsoid", "fired_dough_twist":"irregular", "grape":"irregular", "lemon" : "ellipsoid", "mango" : "irregular",
            "litchi":"irregular", "mooncake":"column", "orange" : "ellipsoid", "pear" : "irregular", "peach":"ellipsoid", "plum" : "ellipsoid", "qiwi" : "ellipsoid",
            "sachima" : "column", "tomato" : "ellipsoid" }

density_energy = { "apple" : [0.78,0.52], "banana" : [0.91,0.89], "bread" : [0.18,3.15],  "bun" : [0.34,2.23], 
            "doughnut" : [0.31,4.34], "egg" : [1.03,1.43], "fired_dough_twist":[0.58,24.16], "grape":[0.97,0.69],
            "lemon" : [0.96, 0.29], "litchi":[1.00,0.66],"mango" : [1.07,0.60], "mooncake": [0.96, 18.83], "orange" : [0.90,0.63], "pear" : [1.02,0.39],
            "peach":[0.96,0.57], "plum" : [1.01,0.46], "qiwi" : [0.97,0.61], "sachima" : [0.22,21.45], "tomato" : [0.98,0.27] }


sideview_data = pd.read_csv("sideview_pixels.csv")  #[Bounding Box Objects,Total Pixel Count,Row Pixel Count Sum,Max Row Pixel Count,Bounding Box (H + W)]
object_sideview = sideview_data[sideview_data["Image Name"]!="coin"]
coin_sideview = sideview_data[sideview_data["Image Name"]=="coin"]

topview_data = pd.read_csv("topview_pixels.csv")
object_topview = topview_data[topview_data["Image Name"]!="coin"]
coin_topview = topview_data[topview_data["Image Name"]=="coin"]

object_name = object_sideview.iloc[0,0]
object_shape = cls_name[object_name]

alpha_side = 5/coin_sideview.iloc[0,4]
alpha_top = 5/coin_topview.iloc[0,4]

# Calculate Volume

if(object_shape == "ellipsoid"):
     volume = math.pi*math.pow(alpha_side,3)*object_sideview.iloc[0,2]/4

elif(object_shape == "column"):
     volume = math.pow(alpha_top,2)*alpha_side*object_sideview.iloc[0,5]*object_topview.iloc[0,1]

elif(object_shape == "irregular"):
     volume = object_topview.iloc[0,1]*math.pow(alpha_top,2)*alpha_side*object_sideview.iloc[0,2]/(object_sideview.iloc[0,2]**2)

calories = volume*density_energy[object_name][0]*density_energy[object_name][1]

print(f"Estimated Volume for {object_name} is: {volume} mm³")
print(f"Calorie estimate for {object_name} is: {calories} Kcal")
     

