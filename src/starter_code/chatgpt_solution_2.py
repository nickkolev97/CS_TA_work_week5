import pandas as pd
from pathlib import Path


def read_paralympics_data(file_path):
    """
    Read data from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str or Path): The path to the CSV file to be read.

    Returns:
        pd.DataFrame or None: A Pandas DataFrame containing the data if the file is successfully read,
        or None if there is an error.

    This function reads data from a CSV file and returns it as a Pandas DataFrame.
    If the file is not found or if an error occurs during reading, None is returned.
    """
    try:
        # Convert the file_path to a Path object and read the CSV file into a Pandas DataFrame
        file_path = Path(file_path)
        df = pd.read_csv(file_path)

        # Optionally, you can do further data manipulation or analysis here

        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def print_information(df):
    """
    Print various information about the provided DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be analyzed.

    This function prints the following information about the DataFrame:
    - Number of rows and columns using `.shape`
    - The first 7 rows of data using `.head()`
    - The last 6 rows of data using `.tail()`
    - Column labels using `.columns`
    - Column data types using `.dtypes`
    - General statistics using `.describe()`
    """
    if df is not None:
        # Print the number of rows and columns in the DataFrame using `.shape`
        print("Number of rows and columns:", df.shape)

        # Print the first 7 rows of data using `.head()` and the last 6 rows using `.tail()`
        print("First 7 rows:")
        print(df.head(7))
        print("Last 6 rows:")
        print(df.tail(6))

        # Print the column labels using `.info()` or `.columns`
        print("Column labels:")
        print(df.columns)

        # Print the column data types using `.info()` or `.dtypes`
        print("Column data types:")
        print(df.dtypes)

        # Print general statistics using `.describe()`
        print("General statistics:")
        print(df.describe())


# Specify the path to your raw data file
file_path = "data/paralympics_raw.csv"

# Call the function to read the data into a DataFrame
paralympics_df = read_paralympics_data(file_path)

# Call the function to print information about the DataFrame
print_information(paralympics_df)