import streamlit as st

# Set wide mode layout
st.set_page_config(page_title="Urbanmop HR Project", layout="wide")


# Function to check if the uploaded file is valid
def is_valid_file(file1):
    if file1 is not None and (file1.name.endswith('.csv') or file1.name.endswith('.xlsx')):
        return True
    return False


# Heading
st.title("Urbanmop HR Project")

# File uploaders in a grid layout
cols = st.columns(2)
uploaded_files = []

# File names and descriptions
file_names = [
    "Calendly Interview Extract (.csv or .xlsx)",
    "Cleaner's History Extract (.csv or .xlsx)",
    "Contract Extract Tariq (.csv or .xlsx)",
    "Endorsement Extract Tariq (.csv or .xlsx)",
    "Phone Interview Extract Tariq (.csv or .xlsx)",
    "Calendly Interview Extract Updated (.csv or .xlsx)"
]

# Loop through and create file uploaders for six files
for i in range(6):
    with cols[i % 2]:
        # Display the file name with custom styling
        st.markdown(f"<h3 style='text-align: center;'>{file_names[i]}</h3>", unsafe_allow_html=True)

        file = st.file_uploader("", type=['csv', 'xlsx'], key=f'file_{i + 1}')
        if file:
            if is_valid_file(file):
                st.success(f"File {i + 1} uploaded successfully!")
                uploaded_files.append(file)
            else:
                st.error(f"File {i + 1} is not a valid .csv or .xlsx file. Please upload a valid file.")

# Process button
if st.button("Process"):
    st.write("Processing... (This button doesn't do anything yet)")
