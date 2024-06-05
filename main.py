
import pandas as pd
from KPI.calendlyInterviewExtract.checkAndFilterColumns import check_and_filter_columns
from KPI.calendlyInterviewExtract.removeRowsWithMissingValues import remove_rows_with_missing_values
from KPI.calendlyInterviewExtract.cleanCreatedAtColumn import format_date_column
# from Google.googleSheetRead import get_sheet_data
#
# # Variable Definition
# credential_path = "Google/manuel-425211-3ec71dfc9025.json"
#
try:
    # # Reading Data via Google sheet
    # calendly = get_sheet_data(credential_path, "HR", "Calendly_Extract")
    # phone_interview = get_sheet_data(credential_path, "HR", "Phone_Interview_Extract")
    # contract = get_sheet_data(credential_path, "HR", "Contract_Extract")
    # endorsement = get_sheet_data(credential_path, "HR", "Endorsement_Extract")
    # cleaners_history = get_sheet_data(credential_path, "HR", "Cleaners_History_Extract")

    # print(calendly)
    # print(phone_interview)
    # print(contract)
    # print(endorsement)
    # print(cleaners_history)
    # *****************************

    # Reading Data Uploaded/ Locally
    calendly_l = pd.read_csv('Data/Calendly Interview Extract.csv')
    phone_interview_l = pd.read_csv("Data/Phone Interview Extract Tariq.csv")
    contract_l = pd.read_csv("Data/Contract Extract Tariq.csv")
    endorsement_l = pd.read_csv("Data/Endorsement Extract Tariq.csv")
    cleaners_history_l = pd.read_csv("Data/Cleaners History Extract (3).csv")

    # print(calendly_l)
    # print(phone_interview_l)
    # print(contract_l)
    # print(endorsement_l)
    # print(cleaners_history_l)
    # *****************************

    # 1- Calendly Extract Processing
    # a- Define Columns - (One Function that take in dataframe local, list of columns and return filtered dataframe.)
    calendly_shortlist_extract = ['id', 'title', 'createdAt']
    # b- Define function that take in dataframe and check for all the missing values in all the present columns and
    # remove them.
    # c- Find the respected Data column in all extract and convert them to YYYY-MM-DD. The function take in dataframe,
    # date column name and return update dataframe with respected column turn into date time in YYYY-MM-DD format.
    # *****************************

    # 2- Phone Interview Extract Processing
    phone_interview_shortlist_extract = ["id", "createdAt", "custom.reachedStr", "custom.interviewedById",
                                         "custom.cleanerInterviewScoreNum"]

    # *****************************

    # 3- Contract Extract Processing

    # *****************************

    # 4- Endorsement Extract Processing

    # *****************************

    # 5- Cleaners Extract

    # *****************************

    # Checking uploaded/local data with Google Sheet Data

    # *****************************

    # Append to Google Sheet

    # *****************************

    # Define the required columns
    required_columns = ['id', 'title']

    # Define possible date columns
    date_columns = ['createdAt', 'date', 'Date', 'custom.dateofHiringAt', 'customer.createdAt']

    # Load your CSV into a DataFrame
    data = pd.read_csv(r'Data/Calendly Interview Extract.csv')

    # Check and filter the DataFrame
    filtered_data, date_column = check_and_filter_columns(data, required_columns, date_columns)

    # If filtered_data is None
    if filtered_data is None:
        print("Filtered data is None, cannot proceed.")
    else:
        # Remove rows with missing/null values in the required columns
        cleaned_data = remove_rows_with_missing_values(filtered_data)

        # If cleaned_data is None
        if cleaned_data is None:
            print("Cleaned data is None, cannot proceed.")
        else:
            # Format the date column
            updated_data = format_date_column(cleaned_data, date_column)

            # If updated_data is None
            if updated_data is None:
                print("Updated data is None, cannot proceed.")
            else:
                print(updated_data.head())

except FileNotFoundError as e:
    print(f"File not found: {e}")
except pd.errors.EmptyDataError as e:
    print(f"Empty data: {e}")
except pd.errors.ParserError as e:
    print(f"Parsing error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except KeyError as e:
    print(f"Key error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
