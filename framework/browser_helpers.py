from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def start_browser(headless=True):
    """Starts a Chrome browser instance. Runs headless by default."""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def find_element(driver, by, value):
    """Finds an element using Selenium's 'find_element'."""
    return driver.find_element(by, value)

def click_element(driver, by, value):
    """Finds and clicks an element."""
    element = find_element(driver, by, value)
    element.click()

def enter_text(driver, by, value, text):
    """Finds a text field and enters the provided text."""
    element = find_element(driver, by, value)
    element.send_keys(text)
