# google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def update_google_sheet(df, sheet_name, credentials_file):
    """
    Updates the given Google Sheet (first worksheet) with the contents of a pandas DataFrame.
    Args:
        df (pandas.DataFrame): Data to upload
        sheet_name (str): Name of the Google Sheet
        credentials_file (str): Path to the service account JSON
    """
    # Define the scope for Google APIs
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    # Create credentials using the service account JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(creds)

    # Open the spreadsheet and select the first worksheet
    sheet = client.open(sheet_name).sheet1

    # (Optional) Clear existing data
    sheet.clear()

    # Convert DataFrame to a list of lists
    data = [df.columns.values.tolist()] + df.values.tolist()

    # Update the sheet
    sheet.update(data)
