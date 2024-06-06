
import pandas as pd


def find_unique_values(db_dataframe, uploaded_dataframe, column_name):
    """
    Compares the specified column in the uploaded DataFrame with the database DataFrame
    and returns the unique values present in the uploaded DataFrame.

    Parameters:
    db_dataframe (pd.DataFrame): The database DataFrame.
    uploaded_dataframe (pd.DataFrame): The uploaded DataFrame.
    column_name (str): The name of the column to compare.

    Returns:
    pd.Series: A Series containing unique values in the uploaded DataFrame's specified column.
    None: If an error occurs during the process.
    """
    try:
        # Check if inputs are pandas DataFrames
        if not isinstance(db_dataframe, pd.DataFrame) or not isinstance(uploaded_dataframe, pd.DataFrame):
            print("Both db_dataframe and uploaded_dataframe must be pandas DataFrames.")
            return None

        # Check if column_name is a string
        if not isinstance(column_name, str):
            print("The column_name parameter must be a string.")
            return None

        # Check if the specified column exists in both DataFrames
        if column_name not in db_dataframe.columns or column_name not in uploaded_dataframe.columns:
            print(f"The column '{column_name}' must be present in both DataFrames.")
            return None

        # Find unique values in the uploaded DataFrame that are not in the database DataFrame
        unique_values = uploaded_dataframe[~uploaded_dataframe[column_name].isin(db_dataframe[column_name])]

        return unique_values

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
