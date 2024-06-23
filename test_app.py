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

# Create two rows with three columns each for the file uploaders
cols = st.columns(3)

with cols[0]:
    st.header("Calendly File")
    calendly_file = st.file_uploader("Calendly File", type=['csv', 'xlsx'], key="calendly")

with cols[1]:
    st.header("Phone Interview File")
    phone_interview_file = st.file_uploader("Phone Interview File", type=['csv', 'xlsx'], key="phone_interview")

with cols[2]:
    st.header("Contract File")
    contract_file = st.file_uploader("Contract File", type=['csv', 'xlsx'], key="contract")

cols = st.columns(3)

with cols[0]:
    st.header("Endorsement File")
    endorsement_file = st.file_uploader("Endorsement File", type=['csv', 'xlsx'], key="endorsement")

with cols[1]:
    st.header("Cleaners History File")
    cleaners_history_file = st.file_uploader("Cleaners History File", type=['csv', 'xlsx'], key="cleaners_history")

with cols[2]:
    st.header("L27 HR File")
    l27_hr_file = st.file_uploader("L27 HR File", type=['csv', 'xlsx'], key="l27_hr")


# Function to process and verify each uploaded file
def process_file(file, name):
    if file is not None:
        df = upload_file_to_dataframe(file)
        if df is None:
            st.error(f"Error in {name} file.")
            return None
        flag = match_columns_to_key(list(df.columns))
        if flag is None:
            st.error(f"Error in identification of {name} file.")
            return None
        dataframe_dict[name] = df


# Process each uploaded file
process_file(calendly_file, 'Calendly')
process_file(phone_interview_file, 'Phone Interview')
process_file(contract_file, 'Contract')
process_file(endorsement_file, 'Endorsement')
process_file(cleaners_history_file, 'Cleaners History')
process_file(l27_hr_file, 'L27 HR')

# Ensure all files are uploaded before processing
if st.button("Process"):
    if len(dataframe_dict) != 6:
        st.error("Please upload all six files.")
    else:
        main(
            dataframe_dict['Calendly'],
            dataframe_dict['Phone Interview'],
            dataframe_dict['Contract'],
            dataframe_dict['Endorsement'],
            dataframe_dict['Cleaners History'],
            dataframe_dict['L27 HR']
        )
        st.success("Processing completed successfully!")
