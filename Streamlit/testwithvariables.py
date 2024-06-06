import streamlit as st
import pandas as pd

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")

# Heading
st.title("Urbanmop HR Project")

# Define the list of required columns for each file type
required_columns = [
    ['id', 'title', 'createdAt'],
    ["id", "name", "displayName", "gender", "custom.statusOfPersonStr", "custom.rentalOrOwnEquipmentStr",
     "custom.dateofHiringAt", "custom.dateOfFiringAt"],
    ["id", "preview", "customer.createdAt"],
    ["id", "createdAt", "custom.testCleanScoreStr"],
    ["id", "createdAt", "custom.reachedStr", "custom.interviewedById", "custom.cleanerInterviewScoreNum"],
    ["id", "createdAt", "custom.reachedStr", "custom.interviewedById", "custom.cleanerInterviewScoreNum"]
]

# List to keep track of uploaded filenames
uploaded_filenames = []

# File uploader
uploaded_files = st.file_uploader("Upload all six files (.csv or .xlsx)", accept_multiple_files=True,
                                  type=['csv', 'xlsx'])

# Check if maximum 6 files are uploaded
if uploaded_files and len(uploaded_files) > 6:
    st.error("Maximum 6 files can be uploaded at a time.")
    st.stop()


# Display success or error messages after file upload
if uploaded_files:
    for file in uploaded_files:
        if file.name in uploaded_filenames:
            st.error(f"File '{file.name}' has already been uploaded.")
            continue  # Skip processing the current file
        uploaded_filenames.append(file.name)  # Add filename to the list of uploaded filenames

        # Read the uploaded file into a DataFrame
        df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)

        # Check each file for all the required columns
        for file_idx, req_cols in enumerate(required_columns):
            file_name = f"file_{file_idx + 1}"  # Generate variable name for the file
            file_columns = df.columns.tolist()  # Get the columns present in the file

            # Check if the required columns match all the columns in the file
            if all(col in file_columns for col in req_cols):
                st.success(f"File '{file.name}' has the required columns: {req_cols}")
                # Store the file in a variable
                globals()[file_name] = df
                st.write(df.head(5))  # Display the first 5 rows of the DataFrame
                # Perform specific processing for this file
                # Add your processing logic here
                break  # Move to the next file after finding the required columns
        else:
            st.error(f"No matching file columns found for '{file.name}'")

# Process button
st.button("Process")
