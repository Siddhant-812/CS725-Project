from ultralytics import YOLO
import pandas as pd

# Train the model
train = 0
if train == 1:
    model = YOLO('yolov8m.yaml').load('yolov8m.pt')  # build from YAML and transfer weights
    train_results = model.train(data='dataset.yaml',
        epochs=3, imgsz=640, device='mps',
        save_period=1, save=True, verbose=True, val=True)

# Load a custom model
model = YOLO('runs/detect/train/weights/best.pt') 

# Define path to the test image file
source = 'images/testing/apple015S(1).jpg'

# Run inference on the source
results = model(source, conf=0.25, iou=0.7, imgsz=640,
    save=True)  # list of Results objects, output is saved in runs/detect/predict
object_id_mapping = {'apple': 0, 'banana': 1, 'bread': 2, 'bun': 3, 'doughnut': 4,
    'egg': 5, 'fired_dough_twist': 6, 'grape': 7, 'lemon': 8, 'litchi': 9, 'mango': 10,
    'coin': 11, 'mooncake': 12, 'orange': 13, 'peach': 14, 'pear': 15, 'plum': 16,
    'qiwi': 17, 'sachima': 18, 'tomato': 19}
reversed_map = {v: k for k, v in object_id_mapping.items()}

num_row = len([(i,j) for i in results for j in i.boxes.cls])
df = pd.DataFrame(index=range(num_row), columns=['image_name', 'object_id', 'object_name', 'x', 'y', 'w', 'h', 'conf'])

for r in results:
    for i in range(len(r.boxes.cls)):
        df.iloc[i,0] = str(r.path).replace("/","\\")
        df.iloc[i,1] = int(r.boxes.cls[i])
        df.iloc[i,2] = reversed_map[int(r.boxes.cls[i])]
        df.iloc[i,3:7] = r.boxes.xywhn[i].tolist()
        df.iloc[i,7] = float(r.boxes.conf[i])

df.to_json("output.json", orient='records', indent=4)



