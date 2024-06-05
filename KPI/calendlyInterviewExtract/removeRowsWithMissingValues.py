import pandas as pd


def remove_rows_with_missing_values(df):
    """
    Remove rows with missing/null values in all columns of the provided DataFrame.

    Args:
    df (pandas.DataFrame): The DataFrame to check and clean.

    Returns:
    pandas.DataFrame: The cleaned DataFrame with rows containing missing/null values removed.
    """
    try:
        # Remove rows with missing/null values in any of the columns
        cleaned_df = df.dropna()
        return cleaned_df
    except Exception as e:
        # Catch any other exceptions that might occur
        print(f"An error occurred: {e}")
        return None
