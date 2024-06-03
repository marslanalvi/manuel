import pandas as pd


def process_dates(dataframe, date_column):
    """
    Processes the specified date column in the DataFrame to retain only the date part in
    'YYYY-MM-DD' format and changes the data type to pandas datetime format, ignoring null values.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame.
    date_column (str): The name of the column containing date values.

    Returns:
    pd.DataFrame: The updated DataFrame with processed dates, or None if an error occurs.

    Raises:
    TypeError: If the input is not a DataFrame or date_column is not a string.
    ValueError: If the specified date_column is not present in the DataFrame.
    """
    try:
        # Check if the input dataframe is a pandas DataFrame
        if not isinstance(dataframe, pd.DataFrame):
            print("The first argument must be a pandas DataFrame.")
            return None

        # Check if the date_column parameter is a string
        if not isinstance(date_column, str):
            print("The second argument must be a string representing the column name.")
            return None

        # Check if the specified date_column is in the DataFrame
        if date_column not in dataframe.columns:
            print(f"The column '{date_column}' is not in the DataFrame.")
            return None

        # Process the date column to retain only the date part in 'YYYY-MM-DD' format
        dataframe[date_column] = pd.to_datetime(dataframe[date_column], format='%Y-%m-%dT%H:%M:%S.%fZ', errors='coerce').dt.date

        # Convert the date column to pandas datetime format, ignoring null values
        dataframe[date_column] = pd.to_datetime(dataframe[date_column], format='%Y-%m-%d', errors='coerce')

        return dataframe

    except Exception as e:
        print(f"An error occurred: {e}")
        return None