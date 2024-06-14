import pandas as pd


def convert_date_format_with_error_handling(df, date_column):
    """
    Converts the dates in the specified column of the dataframe to datetime and ensures they are in YYYY-MM-DD format.
    Handles errors and different date formats.

    Args:
    df (pd.DataFrame): The dataframe containing the date column.
    date_column (str): The name of the date column to be converted.

    Returns:
    pd.DataFrame: The updated dataframe with the converted date column.
    """
    try:
        # Try common date formats
        formats = ['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%Y/%m/%d']
        for fmt in formats:
            try:
                df[date_column] = pd.to_datetime(df[date_column], format=fmt)
                break
            except ValueError:
                continue

        # Convert to datetime if not already in datetime format
        if df[date_column].dtype != 'datetime64[ns]':
            df[date_column] = pd.to_datetime(df[date_column], errors='raise')

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
