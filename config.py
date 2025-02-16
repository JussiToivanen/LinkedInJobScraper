# config.py

# ----- Search / Scraper Configuration -----
SEARCH_TERM = "python developer"
BASE_URL = "https://www.linkedin.com/jobs/search/"
JOB_CARDS_SELECTOR = "ul.jobs-search__results-list li"

# ----- File / Local Data -----
CSV_FILENAME = "linkedin_jobs.csv"

# ----- Google Sheets Configuration -----
SHEET_NAME = "LinkedIn Jobs Data"  # The name of your Google Sheet
CREDENTIALS_FILE = "path/to/your_service_account_credentials.json"