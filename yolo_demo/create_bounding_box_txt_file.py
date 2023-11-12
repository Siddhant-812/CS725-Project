import xml.etree.ElementTree as ET
import pandas as pd
import os

def parse_xml_to_dataframe(xml_file, object_id_mapping, output_folder):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = {'filename': [], 'object_id': [], 'object_name': [],
            'x_center': [], 'y_center': [], 'width': [], 'height': []}

    filename = root.find('filename').text

    image_width = float(root.find('size/width').text)
    image_height = float(root.find('size/height').text)

    for obj in root.findall('object'):
        object_name = obj.find('name').text
        object_id = object_id_mapping.get(object_name, -1)

        if object_id == -1:
            raise ValueError(f"Object name '{object_name}' not found in the mapping dictionary.")

        bbox = obj.find('bndbox')
        xmin = float(bbox.find('xmin').text) / image_width
        ymin = float(bbox.find('ymin').text) / image_height
        xmax = float(bbox.find('xmax').text) / image_width
        ymax = float(bbox.find('ymax').text) / image_height

        x_center = (xmin + xmax) / 2
        y_center = (ymin + ymax) / 2
        width = xmax - xmin
        height = ymax - ymin

        data['filename'].append(filename)
        data['object_id'].append(object_id)
        data['object_name'].append(object_name)
        data['x_center'].append(x_center)
        data['y_center'].append(y_center)
        data['width'].append(width)
        data['height'].append(height)

    df = pd.DataFrame(data)

    # Save the normalized bounding box information to a text file
    output_file = filename.replace('.JPG', '.txt')
    with open(output_folder + output_file, 'w') as txt_file:
        for _, row in df.iterrows():
            txt_file.write(f"{row['object_id']} {row['x_center']} {row['y_center']} {row['width']} {row['height']}\n")

    return df

object_id_mapping = {'apple': 0, 'banana': 1, 'bread': 2, 'bun': 3, 'doughnut': 4,
    'egg': 5, 'fired_dough_twist': 6, 'grape': 7, 'lemon': 8, 'litchi': 9, 'mango': 10,
    'coin': 11, 'mooncake': 12, 'orange': 13, 'peach': 14, 'pear': 15, 'plum': 16,
    'qiwi': 17, 'sachima': 18, 'tomato': 19}

xml_folder = './data_prep/Annotations/'
output_folder = './data_prep/BBoxtexts/'
os.makedirs(output_folder, exist_ok=True)

for xml_file_path in os.listdir(xml_folder):
    parse_xml_to_dataframe(xml_folder + xml_file_path, object_id_mapping, output_folder)
    print(f"{xml_file_path} done")

