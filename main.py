
# import pandas as pd
from Google.googleSheetRead import get_sheet_data
from dataProcessing.filtringColumns import filter_columns
from dataProcessing.checkingNull import replace_and_remove
from dataProcessing.dateProcessing import process_dates
from dataProcessing.nameProcessing_cleaners import extract_names
from comparison.comparison import find_unique_rows
from Google.apeedGSheet import append_dataframe_to_google_sheet
from dataProcessing.dateProcessingL27 import convert_date_format_with_error_handling
from dataProcessing.removeBlanksL27 import remove_null_ratings


def main(calendly_l, phone_interview_l, contract_l, endorsement_l, cleaners_history_l, l27_hr_l):
    # Variable Definition
    credential_path = "Google/mauel-425211-3ec71dfc9025.json"

    try:
        # Reading Data via Google sheet
        calendly = get_sheet_data(credential_path, "HR", "Calendly_Extract")
        phone_interview = get_sheet_data(credential_path, "HR", "Phone_Interview_Extract")
        contract = get_sheet_data(credential_path, "HR", "Contract_Extract")
        endorsement = get_sheet_data(credential_path, "HR", "Endorsement_Extract")
        cleaners_history = get_sheet_data(credential_path, "HR", "Cleaners_History_Extract")
        l27_hr = get_sheet_data(credential_path, "HR", "L27_HR")

        # print(calendly)
        # print(phone_interview)
        # print(contract)
        # print(endorsement)
        # print(cleaners_history)
        # print(l27_hr)
        # *****************************

        # 1- Calendly Extract Processing
        calendly_shortlist_extract = ['id', 'title', 'createdAt']

        calendly_l = filter_columns(calendly_l, calendly_shortlist_extract)
        if calendly_l is None:
            print("Error filtering column calendly.")
            exit()
        # print(calendly_l)

        calendly_l = replace_and_remove(calendly_l, "id")
        if calendly_l is None:
            print("Error removing and handling Nulls in calendly.")
            exit()
        # print(calendly_l)

        calendly_l = process_dates(calendly_l, "createdAt")
        if calendly_l is None:
            print("Error processing dates in calendly.")
            exit()
        # print(calendly_l)
        # print(calendly_l.dtypes)
        # *****************************

        # 2- Phone Interview Extract Processing
        phone_interview_shortlist_extract = ["id", "createdAt", "custom.reachedStr", "custom.interviewedById",
                                             "custom.cleanerInterviewScoreNum"]

        phone_interview_l = filter_columns(phone_interview_l, phone_interview_shortlist_extract)
        if phone_interview_l is None:
            print("Error filtering column phone interview.")
            exit()
        # print(phone_interview_l)

        phone_interview_l = replace_and_remove(phone_interview_l, "id")
        if phone_interview_l is None:
            print("Error removing and handling Nulls in phone interview.")
            exit()
        # print(phone_interview_l)

        phone_interview_l = process_dates(phone_interview_l, "createdAt")
        if phone_interview_l is None:
            print("Error processing dates in phone interview.")
            exit()
        # print(phone_interview_l)
        # print(phone_interview_l.dtypes)
        # *****************************

        # 3- Contract Extract Processing
        contract_shortlist_extract = ["id", "preview", "customer.createdAt"]

        contract_l = filter_columns(contract_l, contract_shortlist_extract)
        if contract_l is None:
            print("Error filtering column contract.")
            exit()
        # print(contract_l)

        contract_l = replace_and_remove(contract_l, "id")
        if contract_l is None:
            print("Error removing and handling Nulls in contract.")
            exit()
        # print(contract_l)

        contract_l = process_dates(contract_l, "customer.createdAt")
        if contract_l is None:
            print("Error processing dates in contract.")
            exit()
        # print(contract_l)
        # print(contract_l.dtypes)
        # *****************************

        # 4- Endorsement Extract Processing
        endorsement_shortlist_extract = ["id", "createdAt", "custom.testCleanScoreStr"]

        endorsement_l = filter_columns(endorsement_l, endorsement_shortlist_extract)
        if endorsement_l is None:
            print("Error filtering column endorsement.")
            exit()
        # print(endorsement_l)

        endorsement_l = replace_and_remove(endorsement_l, "id")
        if endorsement_l is None:
            print("Error removing and handling Nulls in endorsement.")
            exit()
        # print(endorsement_l)

        endorsement_l = process_dates(endorsement_l, "createdAt")
        if endorsement_l is None:
            print("Error processing dates in endorsement.")
            exit()
        # print(endorsement_l)
        # print(endorsement_l.dtypes)
        # *****************************

        # 5- Cleaners Extract
        cleaners_shortlist_extract = ["id", "name", "displayName", "gender", "custom.statusOfPersonStr",
                                      "custom.rentalOrOwnEquipmentStr", "custom.dateofHiringAt",
                                      "custom.dateOfFiringAt", 'custom.cleanerCityStr']

        cleaners_history_l = filter_columns(cleaners_history_l, cleaners_shortlist_extract)
        if cleaners_history_l is None:
            print("Error filtering column cleaners.")
            exit()
        # print(cleaners_history_l)

        cleaners_history_l = replace_and_remove(cleaners_history_l, "id")
        if cleaners_history_l is None:
            print("Error removing and handling Nulls in cleaners.")
            exit()
        # print(cleaners_history_l)

        cleaners_history_l = process_dates(cleaners_history_l, "custom.dateofHiringAt")
        if cleaners_history_l is None:
            print("Error processing dates in cleaners.")
            exit()
        # print(cleaners_history_l)
        # print(cleaners_history_l.dtypes)

        cleaners_history_l = process_dates(cleaners_history_l, "custom.dateOfFiringAt")
        if cleaners_history_l is None:
            print("Error processing dates in cleaners.")
            exit()
        # print(cleaners_history_l)
        # print(cleaners_history_l.dtypes)

        cleaners_history_l = extract_names(cleaners_history_l, 'name')
        if cleaners_history_l is None:
            print("Error processing name column in cleaners.")
            exit()
        # print(cleaners_history_l['name'])
        # *****************************

        # 6- L27 for Quality of Hire Tracker
        l27_shortlist_extract = ["Date", "Full Name", "Rating Value", "Teams Assigned", "Booking ID"]

        l27_hr_l = filter_columns(l27_hr_l, l27_shortlist_extract)
        if l27_hr_l is None:
            print("Error filtering column L27 HR.")
            exit()
        # print(l27_hr_l)

        l27_hr_l = replace_and_remove(l27_hr_l, "Booking ID")
        if l27_hr_l is None:
            print("Error removing and handling Nulls in L27.")
            exit()
        # print(l27_hr_l)

        l27_hr_l = remove_null_ratings(l27_hr_l, "Rating Value")
        if l27_hr_l is None:
            print("Error removing and handling Nulls in L27.")
            exit()
        # print(l27_hr_l["Rating Value"].value_counts())

        l27_hr_l = convert_date_format_with_error_handling(l27_hr_l, "Date")
        if l27_hr_l is None:
            print("Error processing dates in endorsement.")
            exit()
        # print(l27_hr_l)
        # print(l27_hr_l.dtypes)
        # *****************************

        # Checking uploaded/local data with Google Sheet Data
        calendly_u = find_unique_rows(calendly, calendly_l, 'id')
        if calendly_u is None:
            print("Error calculating comparison Calendly.")
            exit()
        phone_interview_u = find_unique_rows(phone_interview, phone_interview_l, 'id')
        if phone_interview_u is None:
            print("Error calculating comparison Phone Interview.")
            exit()
        contract_u = find_unique_rows(contract, contract_l, 'id')
        if contract_u is None:
            print("Error calculating comparison Contract")
            exit()
        endorsement_u = find_unique_rows(endorsement, endorsement_l, 'id')
        if endorsement_u is None:
            print("Error calculating comparison endorsement.")
            exit()
        cleaners_history_u = find_unique_rows(cleaners_history, cleaners_history_l, 'id')
        if cleaners_history_u is None:
            print("Error calculating comparison cleaners history.")
            exit()
        l27_hr_u = find_unique_rows(l27_hr, l27_hr_l, "Booking ID")
        if l27_hr_u is None:
            print("Error calculating comparison l27.")
            exit()
        print(l27_hr_u)
        exit()
        # calendly_u = find_unique_rows(calendly, calendly_l, 'id')
        # print(calendly_u)
        # print(phone_interview_u)
        # print(contract_u)
        # print(endorsement_u)
        # print(cleaners_history_u)
        # *****************************

        # Append to Google Sheet
        calendly_result = append_dataframe_to_google_sheet(credential_path, "HR",
                                                           "Calendly_Extract", calendly_u)
        if calendly_result is None:
            print("Appending Google Drive Calendly Error.")
            exit()

        phone_interview_result = append_dataframe_to_google_sheet(credential_path, "HR",
                                                                  "Phone_Interview_Extract", phone_interview_u)
        if phone_interview_result is None:
            print("Appending Google Drive Phone Interview Error.")
            exit()

        contract_result = append_dataframe_to_google_sheet(credential_path, "HR",
                                                           "Contract_Extract", contract_u)
        if contract_result is None:
            print("Appending Google Drive Contract Error.")
            exit()

        endorsement_result = append_dataframe_to_google_sheet(credential_path, "HR",
                                                              "Endorsement_Extract", endorsement_u)
        if endorsement_result is None:
            print("Appending Google Drive Endorsement Error.")
            exit()

        cleaners_history_result = append_dataframe_to_google_sheet(credential_path, "HR",
                                                                   "Cleaners_History_Extract", cleaners_history_u)
        if cleaners_history_result is None:
            print("Appending Google Drive Cleaners History Error.")
            exit()
        # *****************************

    except Exception as e:
        print(f"An error occurred: {e}")


# Reading Data Uploaded/ Locally
import pandas as pd
calendly_l = pd.read_csv('Data/Calendly Extract Tariq.csv')
phone_interview_l = pd.read_csv("Data/Phone Interview Extract Tariq.csv")
contract_l = pd.read_csv("Data/Contract Extract Tariq.csv")
endorsement_l = pd.read_csv("Data/Endorsement Extract Tariq.csv")
cleaners_history_l = pd.read_csv("Data/Cleaner's History Extract Fixed.csv")
l27_hr_l = pd.read_csv("Data/L27_HR.csv")
#
main(calendly_l, phone_interview_l, contract_l, endorsement_l, cleaners_history_l, l27_hr_l)
# print(calendly_l)
# print(phone_interview_l)
# print(contract_l)
# print(endorsement_l)
# print(cleaners_history_l)
# *****************************
