import framework.browser_helpers as browser_helpers
from selenium.webdriver.common.by import By

def test_google_search():
    driver = browser_helpers.start_browser(headless=True)
    driver.get("https://www.google.com")

    # Use helper to enter text into the search box and submit the form
    browser_helpers.enter_text(driver, By.NAME, "q", "Test Automation")
    
    # Use updated click_element with explicit wait for the search button
    browser_helpers.click_element(driver, By.NAME, "btnK")

    # Validate the result
    assert "Test Automation" in driver.title
    driver.quit()
