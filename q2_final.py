from q2a import json_to_csv
from q2b import split_csv_by_threshold

# Let the user input the path to the json file
json_file_path = input("Please enter the path to the JSON file: ")

# Convert the json to csv
json_to_csv(json_file_path, 'vehicular_data.csv')

# Split the csv based on the threshold
split_csv_by_threshold('vehicular_data.csv', 0.09)
