import pandas as pd

def split_csv_by_threshold(input_csv, threshold):
    try:
        # Load the csv data into a DataFrame
        df = pd.read_csv(input_csv)

        # Filter the data based on the 'magy' threshold
        df_high = df[df['magy'] > threshold]
        df_low = df[df['magy'] <= threshold]

        # Save the filtered data to separate csv files
        df_high.to_csv('mag_high.csv', index=False)
        df_low.to_csv('mag_low.csv', index=False)

    except FileNotFoundError:
        print("The file specified was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")