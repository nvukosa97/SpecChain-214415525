"""imports or reads your raw dataset; if you scraped, include scraper here"""
# Install any missing libraries
import subprocess
import sys


# Import required libraries
from google_play_scraper import app, reviews_all  # For scraping Google Play Store
import pandas as pd  # For data manipulation and analysis
from IPython.display import display, HTML  # For displaying data in Jupyter notebook
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import json  # For working with JSON data


def get_app_data(app_id):
    """Fetch app data from Google Play Store"""
    result = app(
        app_id,
        'en', # STUDENTS_TODO # Set language to English
        'us' # STUDENTS_TODO # Set country to United States
    )
    return result

def get_app_reviews(app_id):
    """Fetch reviews for an app"""
    print("Fectching reviews, this may take some time")
    result = reviews_all(
        app_id,
        sleep_milliseconds=0
    )
    print(f"number of reviews {len(result)}")
    return result # Return only the requested number of reviews

# List of app IDs to scrape
app_ids = [
    'bot.touchkin'
]

# Initialize lists to store app data and reviews
app_data_list = []
app_reviews_list = []

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file = BASE_DIR / "data" / "reviews_raw.jsonl"

with open(file, "w", encoding="utf-8") as f:
    for app_id in app_ids:
        try:
            data = get_app_data(app_id)
            app_data_list.append(data)

            reviews = get_app_reviews(app_id)

            for review in reviews:
                
                json.dump(review, f, default=str)
                f.write("\n")

            print(f"Successfully fetched data for {app_id}")

        except Exception as e:
            print(f"Error fetching data for {app_id}: {e}")