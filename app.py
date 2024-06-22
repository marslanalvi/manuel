import streamlit as st
from dataProcessing.fileConversion_df import upload_file_to_dataframe
from dataProcessing.fileIdentification import match_columns_to_key
from main import main

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")

# Heading
st.title("Urbanmop HR Project")

# Dictionary to keep track of renamed files
dataframe_dict = {}

# File uploader
uploaded_files = st.file_uploader("Upload up to six files (.csv or .xlsx)", accept_multiple_files=True,
                                  type=['csv', 'xlsx'])

# Check if maximum 6 files are uploaded
if uploaded_files and len(uploaded_files) != 6:
    st.error("Please upload all Six Files. ")
    st.stop()

# Display success or error messages after file upload
if uploaded_files:
    for file in uploaded_files:
        my_file = upload_file_to_dataframe(file)
        if my_file is None:
            st.error("Error in uploaded files.")
            print("Error Converting Dataframe.")
            exit()

        flag = match_columns_to_key(list(my_file.columns))
        if flag is None:
            st.error("Error in Identification.")
            print("Unable to Identify.")
            exit()

        dataframe_dict[flag] = my_file
        # print(dataframe_dict)
        print(list(my_file.columns))
        print(flag)
        print("++++")

# Process button

if st.button("Process"):
    main(
        dataframe_dict['Calendly'],
        dataframe_dict['Phone Interview'],
        dataframe_dict['Contract'],
        dataframe_dict['Endorsement'],
        dataframe_dict['Cleaners History'],
        dataframe_dict['L27 HR']
    )
