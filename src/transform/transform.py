import pandas as pd


def clean_data(my_df):

    
    
    no_missing_df = remove_missing_value(my_df)
    no_duplicate_df = remove_duplicates(no_missing_df)
    drop_column_df = drop_column(no_duplicate_df)
    convert_carbon_df = convert_carbon(drop_column_df)
    clean_df = convert_currency(convert_carbon_df)

    return clean_df





def remove_missing_value(my_df):
    df = my_df.dropna()
    return df

def remove_duplicates(my_df):
    df = my_df.drop_duplicates()
    return df

def drop_column(my_df):
    df = my_df.drop(columns=['from_airport_code'], errors='ignore')
    return df

def convert_carbon(my_df):
    df = my_df.copy()
    df['co2_emissions'] = df['co2_emissions'] / 1000
    df['avg_co2_emissions'] = df['avg_co2_emission_for_this_route'] / 1000
    return df

def convert_currency(my_df):
    df = my_df.copy()
    df['price'] = df['price'] * 0.85
    return df


