def remove_rows_with_missing_values(df):
    """
    Remove rows with missing/null values in 'id', 'title', or 'createdAt' columns in the provided DataFrame.

    Args:
    df (pandas.DataFrame): The DataFrame to check and clean.

    Returns:
    pandas.DataFrame: The cleaned DataFrame with rows containing missing/null values in the specified columns removed.
    """
    # Generalize the module so that any dataset can be handled for missing / null values
    try:
        required_columns = ['id', 'title', 'createdAt']

        # Check if all required columns exist in the DataFrame
        if all(col in df.columns for col in required_columns):
            # Remove rows with missing/null values in the required columns
            cleaned_df = df.dropna(subset=required_columns)
            return cleaned_df
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