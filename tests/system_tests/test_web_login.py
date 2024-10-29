import framework.browser_helpers as browser_helpers
from selenium.webdriver.common.by import By

def test_google_search():
    # Start the browser in headless mode
    driver = browser_helpers.start_browser(headless=True)
    
    # Open Google
    driver.get("https://www.google.com")
    
    # Enter text in the search box and click the search button
    browser_helpers.enter_text(driver, By.NAME, "q", "Test Automation")
    browser_helpers.click_element(driver, By.NAME, "btnK")
    
    # Wait for the page to load and validate the title
    browser_helpers.wait_for_title_contains(driver, "Test Automation", timeout=10)
    
    # Assert that "Test Automation" is in the page title
    assert "Test Automation" in driver.title
    driver.quit()
