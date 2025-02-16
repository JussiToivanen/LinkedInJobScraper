A Python-based job scraper that collects job listings from LinkedIn using Selenium and BeautifulSoup, saves them as a CSV, and uploads them to Google Sheets. This project is intended as a learning example or light-duty personal scraper.

Disclaimer: Scraping LinkedIn (or any website) may violate their Terms of Service. Please use responsibly, ethically, and in compliance with all relevant legal rules.

Features
Selenium + BeautifulSoup for scraping dynamic pages
Pandas for structuring data
Google Sheets integration using gspread + oauth2client
Modular code with clear separation of concerns
Configurable via config.py
Requirements
Python 3.7+
pip
Chromedriver matching your local Chrome version (added to PATH)
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YourUsername/LinkedInJobScraper.git
cd LinkedInJobScraper
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up Google Cloud credentials:

Create a Service Account in Google Cloud Console.
Enable the Google Sheets API.
Download the JSON credentials file.
Share your target Google Sheet with the service account’s email.
Update the path to your credentials in config.py (the variable CREDENTIALS_FILE).
Configure project variables in config.py:

SEARCH_TERM — The job keyword you want to scrape (e.g., "python developer").
CSV_FILENAME — Name of your CSV export file (e.g., "linkedin_jobs.csv").
SHEET_NAME — Name of your Google Sheet.
CREDENTIALS_FILE — Path to your service account credentials file.
Usage
Run the main script:

bash
Copy
Edit
python main.py
The scraper will open a headless Chrome session, navigate to LinkedIn Jobs, and scrape listings based on your SEARCH_TERM.
If successful, a CSV file is created/updated in the project directory.
The data is also pushed to your specified Google Sheet.
(Optional) Adjust or add logs, schedule the script via cron (Linux/macOS) or Task Scheduler (Windows), or integrate it with a workflow manager (e.g., Airflow).

Project Structure
