# scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Import config variables
from config import BASE_URL, JOB_CARDS_SELECTOR


def scrape_linkedin_jobs(search_query):
    """
    Scrapes LinkedIn job listings using Selenium + BeautifulSoup for a given search query.
    Returns a pandas DataFrame with the scraped data.
    """

    # 1. Configure Selenium (headless Chrome, for example)
    options = Options()
    options.add_argument("--headless")
    # You can add more options or tweaks:
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    # 2. Build the full URL and navigate
    url = f"{BASE_URL}?keywords={search_query}"
    driver.get(url)

    # 3. Wait for jobs to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, JOB_CARDS_SELECTOR))
        )
    except Exception as e:
        print(f"[Error] Timed out waiting for page to load: {e}")
        driver.quit()
        return pd.DataFrame()  # Return empty DataFrame if no data loaded

    # 4. Parse the page source
    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_cards = soup.select(JOB_CARDS_SELECTOR)

    jobs_data = []
    for card in job_cards:
        title_el = card.select_one("h3.base-search-card__title")
        company_el = card.select_one("h4.base-search-card__subtitle")
        location_el = card.select_one(".job-search-card__location")
        link_el = card.select_one("a.base-card__full-link")

        title = title_el.get_text(strip=True) if title_el else None
        company = company_el.get_text(strip=True) if company_el else None
        location = location_el.get_text(strip=True) if location_el else None
        link = link_el["href"] if link_el else None

        jobs_data.append({
            "title": title,
            "company": company,
            "location": location,
            "link": link
        })

    # 5. Close the browser
    driver.quit()

    # 6. Return as a DataFrame
    df = pd.DataFrame(jobs_data)
    return df