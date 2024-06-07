import streamlit as st
import pandas as pd


def upload_file_to_dataframe(uploaded_file):
    """
    Convert an uploaded file to a pandas DataFrame.
    The file can be a .csv or .xlsx file.

    Parameters:
    uploaded_file: The file uploaded via Streamlit.

    Returns:
    pd.DataFrame: The converted DataFrame.
    """
    try:
        if uploaded_file is not None:
            # Check the file extension
            file_extension = uploaded_file.name.split('.')[-1].lower()

            if file_extension == 'csv':
                # Read CSV file
                dataframe = pd.read_csv(uploaded_file)
            elif file_extension == 'xlsx':
                # Read Excel file
                dataframe = pd.read_excel(uploaded_file, engine='openpyxl')
            else:
                st.error("Unsupported file type. Please upload a .csv or .xlsx file.")
                return None

            return dataframe
        else:
            st.error("No file uploaded.")
            return None
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        return None
