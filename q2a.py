import pandas as pd
import json

def json_to_csv(json_file_path, csv_file):
    try:
        # Open and load the json data from the file
        with open(json_file_path, 'r') as file:
            data = json.load(file)  

        # Load the dict into a dataframe
        df = pd.DataFrame(data['imu_data'])

        # Save the dataframe to a csv file
        df.to_csv(csv_file, index=False)
        print("CSV file has been successfully created.")

    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
