from splinter import Browser
from bs4 import BeautifulSoup as sp
import re
import pandas as pd
import matplotlib.pyplot as plt
import time

# Correct way to initialize the browser
browser = Browser('chrome')  # ✅ Use 'Browser' (capital B) not 'browser'

# Alternative browser options:
# browser = Browser('firefox')
# browser = Browser('edge')

# Example usage
try:
    # Navigate to a URL
    browser.visit('https://www.google.com')
    print("Successfully opened browser and navigated to Google")
    
    # Get the page title
    title = browser.title
    print(f"Page title: {title}")
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    # Always close the browser when done
    browser.quit()
    print("Browser closed") 