import csv
import json

# File paths
json_lines_file_path = '/Users/drumilved/Desktop/Development/Library-systems/server/json_lines_file_preprocessed.txt'
csv_file_path = 'books_data.csv'

json_lines_data = []
with open(json_lines_file_path, 'r', encoding='utf-8') as json_file:
    for line in json_file:
        # Replace single quotes with double quotes and remove leading/trailing whitespaces
        line = line.replace("'", "\"").strip()
        json_data = json.loads(line)
        json_lines_data.append(json_data)

# Extracting headers and rows from JSON data
headers = [key for key in json_lines_data[0]['row_to_json'].keys()]
rows = [data['row_to_json'] for data in json_lines_data]

# Writing to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(rows)

print(f'CSV file "{csv_file_path}" has been created.')