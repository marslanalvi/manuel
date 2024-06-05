import streamlit as st
# import pandas as pd

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")

# Function to check if the uploaded file is valid


def is_valid_file(file1):
    return file1 is not None and (file1.name.endswith('.csv') or file1.name.endswith('.xlsx'))

# Function to automatically map file names to processing functions


def map_file_to_processing(file_name1):
    file_name_lower = file_name1.lower()
    if "calendly interview extract" in file_name_lower:
        return "process_calendly"
    elif "phone interview extract tariq" in file_name_lower:
        return "process_phone_interview"
    elif "cleaner's history extract" in file_name_lower:
        return "process_cleaners_history"
    elif "contract extract tariq" in file_name_lower:
        return "process_contract"
    elif "endorsement extract tariq" in file_name_lower:
        return "process_endorsement"
    elif "calendly interview extract updated" in file_name_lower:
        return "process_calendly_updated"
    else:
        return None

# Heading


st.title("Urbanmop HR Project")

# File uploader
uploaded_files = st.file_uploader("Upload all files (.csv or .xlsx)", type=['csv', 'xlsx'], accept_multiple_files=True)
if uploaded_files:
    file_processing_map = {}

    for file in uploaded_files:
        processing_function = map_file_to_processing(file.name)
        if processing_function and is_valid_file(file):
            st.success(f"File '{file.name}' mapped to '{processing_function}'.")
            file_processing_map[file.name] = processing_function
        else:
            (st.error
             (f"File '{file.name}' is either not valid or could not be automatically mapped to a processing function."))

    # Process button
    if st.button("Process"):
        for file_name, processing_function in file_processing_map.items():
            st.write(f"File '{file_name}' will be processed with '{processing_function}'.")
            # Placeholder for actual processing call
            # processed_df = processing_function(file)
else:
    st.write("No files uploaded yet.")
