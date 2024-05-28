import pandas as pd
def clean_created_at_column(df):
    """
    Clean the 'createdAt' column to extract the date and format it as YYYY-MM-DD.

    Args:
    df (pandas.DataFrame): The DataFrame to clean.

    Returns:
    pandas.DataFrame: The cleaned DataFrame with the 'createdAt' column formatted as YYYY-MM-DD.
    """
    try:
        # Check if 'createdAt' column exists in the DataFrame
        if 'createdAt' in df.columns:
            # Convert 'createdAt' column to datetime
            df['createdAt'] = pd.to_datetime(df['createdAt'], errors='coerce')

            # Extract the date and format it as YYYY-MM-DD
            df['createdAt'] = df['createdAt'].dt.strftime('%Y-%m-%d')

            # Drop rows where 'createdAt' could not be parsed and resulted in NaT
            df = df.dropna(subset=['createdAt'])

            return df
        else:
            print("The 'createdAt' column does not exist in the DataFrame.")
            return None
    except KeyError as e:
        # Return the exception message if a KeyError is encountered
        print(str(e))
        return None
    except Exception as e:
        # Catch any other exceptions that might occur
        print(str(e))
        return None