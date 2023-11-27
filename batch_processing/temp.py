import csv
import json

csv_file_path = 'test_sideview_pixels.csv'  # Replace with the path to your CSV file
json_file_path = 'final_side.json'

result_dict = {}

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        key = row['Image Name']
        if key not in result_dict:
            result_dict[key] = [row]
        else:
            result_dict[key].append(row)

# Convert the result dictionary to JSON format
json_result = json.dumps(result_dict, indent=2)

# Write the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_result)

print("JSON file created successfully.")
