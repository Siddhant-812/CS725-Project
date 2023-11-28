import os
import re
from collections import defaultdict
import shutil
import csv
import json

folder_path = 'C:\\CMInDS\\CS725 - FML\\Project\\CS725-FML-Project-main\\yolo_demo\\images\\img'

def separate_images(folder_path):
    # Create dictionaries to store side view and top view images based on instance number
    side_view_dict = defaultdict(list)
    top_view_dict = defaultdict(list)

    # Define the pattern for matching image names
    pattern = re.compile('(\w+)(\d+)([ST])\((\d+)\)')

    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        match = pattern.match(file_name)
        
        
        if match:
            object_name, example_number, view_type, instance_number = match.groups()
            instance_number = int(instance_number)
            key = str(object_name)+str(example_number)
            # Separate side view and top view images based on the pattern
            if view_type == 'S':
                side_view_dict[key].append(file_name)
            elif view_type == 'T':
                top_view_dict[key].append(file_name)
    """
    data = [(key, value1, value2) for key, values1 in side_view_dict.items() for value1, value2 in zip(values1, top_view_dict[key])]

    # Specify the CSV file name
    csv_file = 'output.csv'

    # Write the data to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if needed
        # writer.writerow(['Key', 'Color', 'Quantity'])
        
        # Write data
        writer.writerows(data)
    """
    data = {key: [[f"yolo_demo\\images\\img\\{value1}", f"yolo_demo\\images\\img\\{value2}"] for value1, value2 in zip(side_view_dict[key], top_view_dict[key])] for key in side_view_dict}

    json_file = 'test_img_paths.json'

    # Write the data to a JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

separate_images(folder_path)

