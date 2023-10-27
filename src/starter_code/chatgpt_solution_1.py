"""
Generated by ChatGPT using the following prompt:

Write a python function that reads from a raw data file in data/paralympics_raw.csv to a dataframe

"""
import pandas as pd

def read_paralympics_data(file_path):
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)

        # Optionally, you can do further data manipulation or analysis here

        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Specify the path to your raw data file
file_path = "data/paralympics_raw.csv"

# Call the function to read the data into a DataFrame
paralympics_df = read_paralympics_data(file_path)

if paralympics_df is not None:
    # You now have your data in the 'paralympics_df' DataFrame
    # You can perform various operations on this DataFrame for data analysis or manipulation
    print(paralympics_df.head())  # Display the first few rows as a sample