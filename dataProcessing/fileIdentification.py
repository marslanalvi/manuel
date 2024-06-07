
def match_columns_to_key(df_columns):
    """
    Check if a list of dataframe columns matches any of the required columns in the dictionary.

    Parameters:
    df_columns (list): List of dataframe columns.
    required_columns_dict (dict): Dictionary containing keys and lists of required columns.

    Returns:
    str: Key of the matching dictionary entry, or None if no match is found.
    """

    required_columns_dict = {
        "Calendly": ['id', 'title', 'createdAt'],
        "Cleaners History": ["id", "name", "displayName", "gender", "custom.statusOfPersonStr",
                             "custom.rentalOrOwnEquipmentStr", "custom.dateofHiringAt",
                             "custom.dateOfFiringAt", 'custom.cleanerCityStr'],
        "Contract": ["id", "preview", "customer.createdAt"],
        "Endorsement": ["id", "createdAt", "custom.testCleanScoreStr"],
        "Phone Interview": ["id", "createdAt", "custom.interviewedById", "custom.cleanerInterviewScoreNum"],
        "Dummy file": ["custom.reachedStr", "custom.interviewedById"]
    }

    for key, required_columns in required_columns_dict.items():
        # Check if all required columns are present in the dataframe columns
        if all(col in df_columns for col in required_columns):
            return key
    return None
