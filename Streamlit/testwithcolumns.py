import streamlit as st
import pandas as pd

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")

# Define the required columns for each file type
file_columns = {
    "Calendly Interview Extract": ['id', 'title', 'createdAt'],
    "Cleaner's History Extract (3)": ["id", "name", "displayName", "gender", "custom.statusOfPersonStr",
                                      "custom.rentalOrOwnEquipmentStr", "custom.dateofHiringAt",
                                      "custom.dateOfFiringAt"],
    "Contract Extract Tariq": ["id", "preview", "customer.createdAt"],
    "Endorsement Extract Tariq": ["id", "createdAt", "custom.testCleanScoreStr"],
    "Phone Interview Extract Tariq - Copy": ["id", "createdAt", "custom.reachedStr", "custom.interviewedById",
                                             "custom.cleanerInterviewScoreNum"],
    "Phone Interview Extract Tariq": ["id", "createdAt", "custom.reachedStr", "custom.interviewedById",
                                      "custom.cleanerInterviewScoreNum"]
}

# Heading
st.title("Urbanmop HR Project")

# File uploader
uploaded_files = st.file_uploader("Upload all six files (.csv or .xlsx)", accept_multiple_files=True,
                                  type=['csv', 'xlsx'])

# Display success or error messages after file upload
if uploaded_files:
    for file in uploaded_files:
        # Check if the file name matches any of the keys in file_columns
        file_name = file.name.split(".")[0]  # Extract file name without extension
        if file_name in file_columns:
            required_columns = file_columns[file_name]
            df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
            # Read the uploaded file into a DataFrame
            if all(col in df.columns for col in required_columns):
                st.success(f"File '{file_name}' has the required columns: {required_columns}")
                st.write(df.head(5))  # Display the first 5 rows of the DataFrame
                # Perform specific processing for this file
                # Add your processing logic here
            else:
                st.error(f"File '{file_name}' is missing required columns: {required_columns}")
        else:
            st.error(f"No matching file columns found for '{file_name}'")

# Process button
st.button("Process")
