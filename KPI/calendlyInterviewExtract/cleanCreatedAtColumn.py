import pandas as pd


def format_date_column(df, date_column):
    """
    Convert the specified date column to YYYY-MM-DD format.

    Args:
    df (pandas.DataFrame): The DataFrame to clean.
    date_column (str): The name of the date column to format.

    Returns:
    pandas.DataFrame: The updated DataFrame with the specified date column formatted as YYYY-MM-DD.
    """
    try:
        # Convert the date column to datetime
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

        # Extract the date and format it as YYYY-MM-DD
        df[date_column] = df[date_column].dt.strftime('%Y-%m-%d')

        # Drop rows where the date column could not be parsed and resulted in NaT
        df = df.dropna(subset=[date_column])

        return df
    except KeyError as e:
        # Raise the exception message if a KeyError is encountered
        raise KeyError(f"Key error encountered: {str(e)}")
    except Exception as e:
        # Raise any other exceptions that might occur
        raise Exception(f"An error occurred: {str(e)}")
