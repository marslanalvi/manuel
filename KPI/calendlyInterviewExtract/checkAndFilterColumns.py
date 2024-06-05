import pandas as pd


def check_and_filter_columns(df, required_columns, date_columns):
    """
    Check for the presence of specified columns in the provided DataFrame.

    If all specified columns are found, keep only these columns and return the filtered DataFrame.
    If any of these columns are not found, raise an error.

    Args:
    df (pandas.DataFrame): The DataFrame to check and filter.
    required_columns (list): The list of columns to check for and retain in the DataFrame.
    date_columns (list): The list of possible date column names.

    Returns:
    pandas.DataFrame: The filtered DataFrame with only the required columns if successful, raises an error otherwise.
    """
    try:
        # Check if all required columns exist in the DataFrame
        required_columns_exist = all(col in df.columns for col in required_columns)
        date_column = next((col for col in date_columns if col in df.columns), None)

        if required_columns_exist and date_column:
            # Add the identified date column to the required columns
            columns_to_keep = required_columns + [date_column]
            # Filter the DataFrame to keep only the required columns
            filtered_df = df[columns_to_keep]
            return filtered_df, date_column
        else:
            # If any required column does not exist, raise an exception
            missing_columns = [col for col in required_columns if col not in df.columns]
            if not date_column:
                missing_columns += date_columns
            raise ValueError(f"Columns {', '.join(missing_columns)} do not exist in the DataFrame.")
    except KeyError as e:
        # Raise the exception message if a KeyError is encountered
        raise KeyError(f"Key error encountered: {str(e)}")
    except Exception as e:
        # Raise any other exceptions that might occur
        raise Exception(f"An error occurred: {str(e)}")
