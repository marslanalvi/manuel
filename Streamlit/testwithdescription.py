import streamlit as st
# import pandas as pd

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")

# Function to check if the uploaded file is valid


def is_valid_file(file1):
    return file1 is not None and (file1.name.endswith('.csv') or file1.name.endswith('.xlsx'))

# Define a dictionary of file descriptions to placeholders for processing functions


processing_functions = {
    "Calendly Interview Extract": "process_calendly",  # Placeholder for the actual processing function
    "Phone Interview Extract Tariq": "process_phone_interview",  # Placeholder for the actual processing function
    "Cleaner's History Extract": "process_cleaners_history",  # Placeholder for the actual processing function
    "Contract Extract Tariq": "process_contract",  # Placeholder for the actual processing function
    "Endorsement Extract Tariq": "process_endorsement",  # Placeholder for the actual processing function
    "Calendly Interview Extract Updated": "process_calendly_updated",  # Placeholder for the actual processing function
}


# Heading
st.title("Urbanmop HR Project")

# File uploader
uploaded_files = st.file_uploader("Upload all files (.csv or .xlsx)", type=['csv', 'xlsx'], accept_multiple_files=True)
if uploaded_files:
    file_types = list(processing_functions.keys())
    selected_files = {}

    for file in uploaded_files:
        st.write(f"Processing {file.name}")
        file_type = st.selectbox(f"Select the type of {file.name}", file_types, key=file.name)
        if is_valid_file(file):
            selected_files[file_type] = file
        else:
            st.error(f"File {file.name} is not a valid .csv or .xlsx file. Please upload a valid file.")

    # Process button
    if st.button("Process"):
        for file_type, file in selected_files.items():
            st.write(f"File '{file.name}' mapped to '{file_type}' and ready for processing.")
            # Placeholder for actual processing call
            # processing_function = processing_functions[file_type]
            # processed_df = processing_function(file)
else:
    st.write("No files uploaded yet.")
