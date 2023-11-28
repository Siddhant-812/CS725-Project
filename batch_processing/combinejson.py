import json

def combine_json_files(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)

    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    combined_data = {}

    for key1, values1 in data1.items():
        for key2, values2 in data2.items():
            if len(key1) == len(key2) and sum(c1 != c2 for c1, c2 in zip(key1, key2)) == 1:
                combined_key = key1
                combined_values = [values1, values2]
                combined_data[combined_key] = combined_values

    with open(output_path, 'w') as output_file:
        json.dump(combined_data, output_file, indent=2)

# Example usage
file1_path = 'final_side.json'
file2_path = 'final_top.json'
output_path = 'combined_file.json'

combine_json_files(file1_path, file2_path, output_path)