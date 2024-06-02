import gspread
import pandas as pd


def get_sheet_data(creds_file_path, sheet_name, worksheet_name):
    try:
        # Authenticate with the downloaded JSON file
        gc = gspread.service_account(filename=creds_file_path)
        # Open the specified Google Sheet
        sh = gc.open(sheet_name)
        # Select the specified worksheet
        worksheet = sh.worksheet(worksheet_name)
        # Get all values from the worksheet
        data = worksheet.get_all_values()
        # Convert the data to a DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])
        return df

    except gspread.exceptions.SpreadsheetNotFound:
        print("Error: The specified spreadsheet was not found.")
        return None
    except gspread.exceptions.WorksheetNotFound:
        print("Error: The specified worksheet was not found in the spreadsheet.")
        return None
    except gspread.exceptions.APIError as e:
        print(f"API Error: {e}")
        return None
    except gspread.exceptions.GSpreadException as e:
        print(f"gspread Exception: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
