import pandas as pd
from datetime import datetime


def convert_date_column(df, date_column):
    # Define possible date formats
    date_formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%m/%d/%y",
        "%Y/%m/%d",
        "%d/%m/%Y",
        "%d/%b/%Y",
        "%b/%d/%Y",
        "%d-%b-%Y",
        "%b-%d-%Y",
        "%Y-%b-%d",
        "%d-%m-%y",
        "%m-%d-%y",
        "%y-%m-%d"
    ]

    def parse_date(date_str):
        for fmt in date_formats:
            try:
                return datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Unable to parse date: {date_str}")

    try:
        df[date_column] = df[date_column].apply(parse_date)
        df[date_column] = df[date_column].apply(lambda x: x.strftime('%Y-%m-%d'))
        df[date_column] = pd.to_datetime(df[date_column])
    except ValueError as e:
        print(f"Error: {e}")
        raise

    return df
