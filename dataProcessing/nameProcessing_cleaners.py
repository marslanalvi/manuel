import pandas as pd


def extract_names(dataframe, column):
    """
    Extracts proper names from the specified column in the DataFrame,
    keeping only the part before '[Team]' if it exists, and returns the updated DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame.
    column (str): The name of the column to process.

    Returns:
    pd.DataFrame: The updated DataFrame with processed names, or None if an error occurs.

    Raises:
    TypeError: If the input is not a DataFrame or column is not a string.
    ValueError: If the specified column is not present in the DataFrame.
    """
    try:
        # Check if the input dataframe is a pandas DataFrame
        if not isinstance(dataframe, pd.DataFrame):
            print("The first argument must be a pandas DataFrame.")
            return None

        # Check if the column parameter is a string
        if not isinstance(column, str):
            print("The second argument must be a string representing the column name.")
            return None

        # Check if the specified column is in the DataFrame
        if column not in dataframe.columns:
            print(f"The column '{column}' is not in the DataFrame.")
            return None

        # Extract names before '[Team]' if it exists, otherwise keep the original value
        dataframe[column] = dataframe[column].apply(lambda x: x.split(' [Team]')[0].strip() if isinstance(x, str) and '[Team]' in x else x)

        return dataframe

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
