from framework.browser_helpers import start_browser, click_element, enter_text
from selenium.webdriver.common.by import By

def test_google_search():
    driver = start_browser(headless=False)
    driver.get("https://www.google.com")

    # Use helper to enter text into the search box and submit the form
    enter_text(driver, By.NAME, "q", "Test Automation")
    
    # Use updated click_element with explicit wait for the search button
    click_element(driver, By.NAME, "btnK")

    # Validate the result
    assert "Test Automation" in driver.title
    driver.quit()
