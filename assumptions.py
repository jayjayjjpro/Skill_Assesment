"""
Assumptions for Task 2:
The JSON file follows a specific structure—an array of objects under the key imu_data, with each object representing a single record. 
Each record must include all necessary fields, with special emphasis on the magy field, which is critical for subsequent operations.

The magy field is assumed to be formatted as a numeric value (float or integer) in the CSV file, allowing for direct numerical comparisons without the need for type conversion.

Assumptions for Task 3:
A recent version of Python is being used, which is assumed to be compatible with all required libraries and the syntax used in the script. This is also to ensure compatibility with Conda.

"""