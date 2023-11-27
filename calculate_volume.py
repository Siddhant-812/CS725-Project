import pandas as pd
import math

cls_name = { "apple" : "ellipsoid", "banana" : "irregular", "bread" : "column",  "bun" : "irregular", "coin" : "",
            "doughnut" : "irregular", "egg" : "ellipsoid", "lemon" : "ellipsoid", "mongo" : "irregular",
            "orange" : "ellipsoid", "pear" : "irregular", "plum" : "ellipsoid", "qiwi" : "ellipsoid",
            "sachima" : "column", "tomato" : "ellipsoid" }


sideview_data = pd.read_csv("sideview_pixels.csv")  #[Bounding Box Objects,Total Pixel Count,Row Pixel Count Sum,Max Row Pixel Count,Bounding Box (H + W)]
object_sideview = list(sideview_data.loc[0])
coin_sideview = list(sideview_data.loc[1])

topview_data = pd.read_csv("topview_pixels.csv")
object_topview = list(topview_data.loc[0])
coin_topview = list(topview_data.loc[1])

object_name = object_sideview[0]
object_shape = cls_name[object_name]

alpha_side = 5/coin_sideview[4]
alpha_top = 5/coin_topview[4]

# Calculate Volume

if(object_shape == "ellipsoid"):
     volume = math.pi*math.pow(alpha_side,3)*object_sideview[2]/4

elif(object_shape == "column"):
     volume = math.pow(alpha_top,2)*alpha_side*object_sideview[5]*object_topview[1]

elif(object_shape == "irregular"):
     volume = object_topview[1]*math.pow(alpha_top,2)*alpha_side*object_sideview[2]/(object_sideview[2]**2)

print(f"Estimated Volume for {object_name} is: {volume}")
     

