from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Test Automation")
    search_box.submit()

    # Wait for the title to contain "Test Automation" (up to 10 seconds)
    WebDriverWait(driver, 10).until(EC.title_contains("Test Automation"))
    
    assert "Test Automation" in driver.title
    driver.quit()
