import pandas as pd


def find_unique_rows(old_df, new_df, unique_col):
    """
    Function to find rows in the old dataframe that have unique IDs not present in the new dataframe.

    Parameters:
    old_df (pd.DataFrame): The old dataframe.
    new_df (pd.DataFrame): The new dataframe.
    unique_col (str): The column name which holds unique values.

    Returns:
    pd.DataFrame: DataFrame containing unique rows from the old dataframe.
    """
    try:
        # Check if the inputs are pandas DataFrames
        if not isinstance(old_df, pd.DataFrame) or not isinstance(new_df, pd.DataFrame):
            print("Both inputs must be pandas DataFrames.")
            return None

        # Check for the unique column in both DataFrames
        if unique_col not in old_df.columns or unique_col not in new_df.columns:
            print(f"'{unique_col}' column must be present in both DataFrames.")
            return None

        # Convert the unique column to string and strip any leading/trailing whitespace
        old_df[unique_col] = old_df[unique_col].astype(str).str.strip()
        new_df[unique_col] = new_df[unique_col].astype(str).str.strip()

        # Find unique IDs in the old dataframe that are not in the new dataframe
        unique_ids_in_old_df = set(new_df[unique_col]).difference(set(old_df[unique_col]))

        # Extract the rows with these unique IDs
        unique_rows_in_old_df = new_df[new_df[unique_col].isin(unique_ids_in_old_df)]

        return unique_rows_in_old_df

    except Exception as e:
        # Handle any other exception that might occur
        print(f"An error occurred: {e}")
        return None

# Example usage:
# unique_rows = find_unique_rows(old_df, new_df, 'id')
# print(unique_rows)
