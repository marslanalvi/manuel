import pandas as pd
import numpy as np


def remove_null_ratings(dataframe, rating_column):
    """
    This function takes a dataframe and the name of the rating column,
    and returns the dataframe with no rows containing null values in the rating column.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe.
    rating_column (str): The name of the column containing rating values.

    Returns:
    pd.DataFrame: The dataframe with no rows containing null values in the rating column.
    """
    try:
        # Check if the dataframe is a valid pandas DataFrame
        if not isinstance(dataframe, pd.DataFrame):
            print("The provided input is not a valid pandas DataFrame.")
            return None

        # Check if the rating column exists in the dataframe
        if rating_column not in dataframe.columns:
            print(f"The column '{rating_column}' does not exist in the dataframe.")
            return None

        # Replace 'NULL' strings with np.nan
        dataframe[rating_column] = dataframe[rating_column].replace('NULL', np.nan)

        # Convert column to numeric, forcing errors to NaN
        dataframe[rating_column] = pd.to_numeric(dataframe[rating_column], errors='coerce')

        # Remove rows with null values in the rating column
        cleaned_dataframe = dataframe.dropna(subset=[rating_column])

        return cleaned_dataframe
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An error occurred: {e}")
