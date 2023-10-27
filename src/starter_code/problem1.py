import pandas as pd
from pathlib import Path




def PrepareData(df, df2):
    '''Prepares data'''
    # Drop the list of named columns `['Events', 'Sports', 'Countries']
    df_dropcols = df.drop(['Events', 'Sports', 'Countries'], axis=1)
    # Drop rows where there is NaN in the 'Participants M' or 'Participants F' columns
    df_dropnans = df_dropcols.dropna(subset=['Participants (M)', 'Participants (F)'])
    # Replace the NaN in Type column with 'Winter'
    df_fillnans = df_dropnans.fillna({'Type': 'Winter'})
    # Remove the whitespace from the Type values using `str.strip()`
    df_fillnans['Type'] = df_fillnans['Type'].str.strip()
    # Create the merged dataframe
    df_merged = df_fillnans.merge(df2, how='left', left_on='Country', right_on='region')
    df_merged = df_merged.drop(['region'], axis=1)
    df_merged['NOC'] = df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR')
    df_merged['NOC'] = df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR')
    # Add the year to the Start and End columns to create a full date as a string.
    df_merged["Start"] = df_merged["Start"] + '-' + df_merged["Year"].astype(str)
    df_merged["End"] = df_merged["End"] + '-' + df_merged["Year"].astype(str)
    # Change the column datatype for Start and End from string to date-time format
    df_merged['Start'] = pd.to_datetime(df_merged['Start'], format='%d-%b-%Y')
    df_merged['End'] = pd.to_datetime(df_merged['End'], format='%d-%b-%Y')
    # Add a duration column to the DataFrame
    df_merged['Duration'] = df_merged['End'] - df_merged['Start']
    # Change the data type of df_merged['Duration'] to int
    df_merged['Duration'] = df_merged['Duration'].dt.days

    df_prepared = df_merged

    # 1. Save the prepared dataframe to a .csv file
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df_prepared.to_csv(prepared_csv_filepath, index=False)

    stupidlylongunusedstring = ("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch is a place in Wales that has a very long name")
    return df_prepared

if __name__ == '__main__':
    raw_data_events = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    events_df = pd.read_csv(raw_data_events)
    raw_data_noc = Path(__file__).parent.parent.joinpath('data', 'noc_regions.csv')
    cols = ['NOC', 'region']
    noc_df = pd.read_csv(raw_data_noc, usecols=cols)
    PrepareData(df=events_df, df2=noc_df)