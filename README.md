# LinkedIn Job Scraper

A Python-based job scraper that collects job listings from LinkedIn using **Selenium** and **BeautifulSoup**, saves them as a CSV, and uploads them to **Google Sheets**. This project is intended as a learning example.


---

## Features

- **Selenium + BeautifulSoup** for scraping dynamic pages  
- **Pandas** for structuring data  
- **Google Sheets integration** using `gspread` + `oauth2client`  
- **Modular** code with clear separation of concerns  
- **Configurable** via `config.py`

---

## Requirements

1. [Python 3.7+](https://www.python.org/downloads/)  
2. [pip](https://pip.pypa.io/en/stable/)  
3. [Chromedriver](https://chromedriver.chromium.org/downloads) matching your local Chrome version (added to PATH)

---
## Troubleshooting
- ChromeDriver version mismatch: Ensure you download the correct version of ChromeDriver matching your local Chrome version.
- Blocked by LinkedIn: If scraping at scale, LinkedIn may block your IP. Consider using proxies or rotating user agents, and always respect their Terms of Service.
- Timeouts: Increase the wait time in scraper.py if you have slow internet or run into loading issues.
- Google Sheets: Verify you’ve shared your sheet with the service account email. Make sure the sheet name in config.py matches exactly.
---

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JussiToivanen/LinkedInJobScraper.git
   cd LinkedInJobScraper
   
2. **Create and activate a virtual environment (recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate
   # Windows: venv\Scripts\activate
   
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

4. **Set up Google Cloud credentials**:

   Create a Service Account in Google Cloud Console.
   Enable the Google Sheets API.
   Download the JSON credentials file.
   Share your target Google Sheet with the service account’s email.
   Update the path to your credentials in config.py (the variable CREDENTIALS_FILE).
   
5. **Configure project variables in config.py**:

   SEARCH_TERM — The job keyword you want to scrape (e.g., "python developer").
   CSV_FILENAME — Name of your CSV export file (e.g., "linkedin_jobs.csv").
   SHEET_NAME — Name of your Google Sheet.
   CREDENTIALS_FILE — Path to your service account credentials file.

## Usage

**Run the main script**:

   ```bash
     python main.py


