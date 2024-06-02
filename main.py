import pandas as pd
import numpy as np

from KPI.calendlyInterviewExtract.checkAndFilterColumns import check_and_filter_columns
from KPI.calendlyInterviewExtract.removeRowsWithMissingValues import remove_rows_with_missing_values
from KPI.calendlyInterviewExtract.cleanCreatedAtColumn import clean_created_at_column
from Google.googleSheetRead import get_sheet_data

# Example usage
credential_path = "Google/mauel-425211-3ec71dfc9025.json"
calendly = get_sheet_data(credential_path, "HR", "Calendly_Extract")
print(calendly)
exit()

try:
    # Load your CSV into a DataFrame
    data = pd.read_csv(r'Data/Calendly Interview Extract.csv')

    # Check and filter the DataFrame
    filtered_data = check_and_filter_columns(data)
    # If filtered_data is None (Amendment needed)
    if filtered_data is not None:
        # Remove rows with missing/null values in the required columns
        cleaned_data = remove_rows_with_missing_values(filtered_data)

        # Clean the 'createdAt' column
        cleaned_data = clean_created_at_column(cleaned_data)
        if cleaned_data is not None:
            print(cleaned_data.head())
except FileNotFoundError as e:
    print(f"File not found: {e}")
except pd.errors.EmptyDataError as e:
    print(f"Empty data: {e}")
except pd.errors.ParserError as e:
    print(f"Parsing error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")