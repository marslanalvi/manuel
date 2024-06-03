
import pandas as pd
from Google.googleSheetRead import get_sheet_data
from dataProcessing.filtringColumns import filter_columns
from dataProcessing.checkingNull import replace_and_remove
from dataProcessing.dateProcessing import process_dates
from dataProcessing.nameProcessing_cleaners import extract_names

# Variable Definition
credential_path = "Google/mauel-425211-3ec71dfc9025.json"

try:
    # Reading Data via Google sheet
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
    cleaners_history_l = pd.read_csv("Data/Cleaner's History Extract (3).csv")

    # print(calendly_l)
    # print(phone_interview_l)
    # print(contract_l)
    # print(endorsement_l)
    # print(cleaners_history_l)
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
                                  "custom.rentalOrOwnEquipmentStr", "custom.dateofHiringAt", "custom.dateOfFiringAt"]

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

    # Checking uploaded/local data with Google Sheet Data

    # *****************************

    # Append to Google Sheet

    # *****************************

except Exception as e:
    print(f"An error occurred: {e}")
