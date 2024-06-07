import streamlit as st
import pandas as pd

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")

# Heading
st.title("Urbanmop HR Project")

# Define the list of required columns for each file type with their specific names
required_columns = {
    "Calendly Interview Extract": ['id', 'title', 'createdAt'],
    "Cleaner's History Extract (3)": ["id", "name", "displayName", "gender", "custom.statusOfPersonStr",
                                      "custom.rentalOrOwnEquipmentStr", "custom.dateofHiringAt",
                                      "custom.dateOfFiringAt"],
    "Contract Extract Tariq": ["id", "preview", "customer.createdAt"],
    "Endorsement Extract Tariq": ["id", "createdAt", "custom.testCleanScoreStr"],
    "Phone Interview Extract Tariq": ["id", "createdAt", "custom.interviewedById", "custom.cleanerInterviewScoreNum"],
    "Dummy file": ["custom.reachedStr", "custom.interviewedById"]
}

# Dictionary to keep track of renamed files
renamed_files = {}

# File uploader
uploaded_files = st.file_uploader("Upload up to six files (.csv or .xlsx)", accept_multiple_files=True,
                                  type=['csv', 'xlsx'])

# Check if maximum 6 files are uploaded
if uploaded_files and len(uploaded_files) > 6:
    st.error("Maximum 6 files can be uploaded at a time.")
    st.stop()

# Display success or error messages after file upload
if uploaded_files:
    for file in uploaded_files:
        # Read the uploaded file into a DataFrame
        df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)

        # Flag to indicate if the file was matched
        file_matched = False

        # Check each file for all the required columns
        for file_name, req_cols in required_columns.items():
            file_columns = df.columns.tolist()  # Get the columns present in the file

            # Check if the required columns match all the columns in the file
            if all(col in file_columns for col in req_cols):
                if file_name in renamed_files:
                    st.error(f"File with the required columns already uploaded and stored as '{file_name}'")
                    file_matched = True
                    break
                st.success(f"File '{file.name}' has the required columns: {req_cols} and is renamed to '{file_name}'")
                # Store the file in a variable
                globals()[file_name.replace(' ', '_').replace("'", "")] = df
                renamed_files[file_name] = df  # Track renamed file
                st.write(df.head(5))  # Display the first 5 rows of the DataFrame
                file_matched = True
                break  # Move to the next file after finding the required columns

        if not file_matched:
            st.error(f"No matching file columns found for '{file.name}'")

# Process button
st.button("Process")
