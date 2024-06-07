import gspread
from gspread.exceptions import SpreadsheetNotFound, WorksheetNotFound, APIError, GSpreadException
import pandas as pd


def append_dataframe_to_google_sheet(creds_file_path, sheet_name, subsheet_name, dataframe):
    try:
        # Convert any Timestamp objects to strings using .loc[]
        for col in dataframe.select_dtypes(include=['datetime', 'datetimetz']).columns:
            dataframe.loc[:, col] = dataframe[col].astype(str)

        # Authenticate with the downloaded JSON file
        client = gspread.service_account(filename=creds_file_path)

        # Access the Google Sheet
        sheet = client.open(sheet_name)

        # Access the specified subsheet
        worksheet = sheet.worksheet(subsheet_name)

        # Convert the dataframe to a list of lists
        data_to_append = dataframe.values.tolist()

        # Append each row of the dataframe to the subsheet
        for row in data_to_append:
            worksheet.append_row(row, value_input_option='USER_ENTERED')

        return True  # Indicate success

    except SpreadsheetNotFound:
        print("Error: The specified spreadsheet was not found. Please check the spreadsheet name.")
    except WorksheetNotFound:
        print("Error: The specified worksheet was not found in the spreadsheet.")
    except APIError as e:
        print(f"API Error: {e}")
    except GSpreadException as e:
        print(f"gspread Exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None  # Indicate failure
