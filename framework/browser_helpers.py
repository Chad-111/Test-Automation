from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def start_browser(headless=True):
    """Starts a Chrome browser instance with options for headless mode."""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def find_element(driver, by, value):
    """Finds an element using Selenium's 'find_element'."""
    return driver.find_element(by, value)

def click_element(driver, by, value, timeout=10):
    """Finds and clicks an element with an explicit wait until it's clickable."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def enter_text(driver, by, value, text):
    """Finds a text field and enters the provided text."""
    element = find_element(driver, by, value)
    element.send_keys(text)

def wait_for_title_contains(driver, text, timeout=10):
    """Waits until the page title contains the specified text."""
    WebDriverWait(driver, timeout).until(EC.title_contains(text))
