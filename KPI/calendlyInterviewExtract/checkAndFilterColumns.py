def check_and_filter_columns(df):
    """
    Check for the presence of 'id', 'title', and 'createdAt' columns in the provided DataFrame.

    If all three columns are found, keep only these columns and return the filtered DataFrame.
    If any of these columns are not found, print an error message.

    Args:
    df (pandas.DataFrame): The DataFrame to check and filter.

    Returns:
    pandas.DataFrame: The filtered DataFrame with only the required columns if successful, None otherwise.
    """
    try:
        required_columns = ['id', 'title', 'createdAt']

        # Check if all required columns exist in the DataFrame
        if all(col in df.columns for col in required_columns):
            # Filter the DataFrame to keep only the required columns
            filtered_df = df[required_columns]
            return filtered_df
        else:
            # If any required column does not exist, raise an exception
            missing_columns = [col for col in required_columns if col not in df.columns]
            print(f"Columns {', '.join(missing_columns)} do not exist in the DataFrame.")
            return None
    except KeyError as e:
        # Return the exception message if a KeyError is encountered
        print(str(e))
        return None
    except Exception as e:
        # Catch any other exceptions that might occur
        print(str(e))
        return None