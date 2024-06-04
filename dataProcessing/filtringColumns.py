import pandas as pd


def filter_columns(dataframe, columns):
    """
    Filters the given DataFrame to include only the specified columns.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame.
    columns (list): A list of column names to include in the returned DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing only the specified columns.

    Raises:
    ValueError: If any of the specified columns are not present in the DataFrame.
    TypeError: If the input is not a DataFrame or the columns parameter is not a list.
    """
    try:
        # Check if the input dataframe is a pandas DataFrame
        if not isinstance(dataframe, pd.DataFrame):
            print("The first argument must be a pandas DataFrame.")
            return None

        # Check if the columns parameter is a list
        if not isinstance(columns, list):
            print("The second argument must be a list of column names.")
            return None

        # Check if all specified columns are in the DataFrame
        missing_columns = [col for col in columns if col not in dataframe.columns]
        if missing_columns:
            print(f"The following columns are not in the DataFrame: {missing_columns}")
            return None

        # Filter the DataFrame to include only the specified columns
        filtered_dataframe = dataframe[columns]

        return filtered_dataframe

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
