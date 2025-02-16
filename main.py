# main.py

import pandas as pd
import os

# Local imports
from config import (
    SEARCH_TERM,
    CSV_FILENAME,
    SHEET_NAME,
    CREDENTIALS_FILE
)
from scraper import scrape_linkedin_jobs
from google_sheets import update_google_sheet

def main():
    # 1. Scrape data
    df = scrape_linkedin_jobs(SEARCH_TERM)
    print(f"[Info] Scraped {len(df)} job listings for '{SEARCH_TERM}'")

    # 2. Save to CSV if data is present
    if not df.empty:
        df.to_csv(CSV_FILENAME, index=False)
        print(f"[Info] Data saved to {CSV_FILENAME}")

        # 3. Update Google Sheet
        try:
            update_google_sheet(df, SHEET_NAME, CREDENTIALS_FILE)
            print("[Info] Google Sheet updated successfully!")
        except Exception as e:
            print(f"[Error] Could not update Google Sheet: {e}")
    else:
        print("[Warning] No data scraped. Skipping CSV and Google Sheets update.")

if __name__ == "__main__":
    main()
