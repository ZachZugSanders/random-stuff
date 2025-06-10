from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    print("Initializing Chrome WebDriver...")
    
    # Set up Chrome options
    chrome_options = Options()
    
    # Create the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    
    # Navigate to Google
    print("Navigating to Google...")
    driver.get("https://www.google.com")
    
    # Keep the browser open for a bit so we can see the result
    input("Press Enter to close the browser...")
    
    # Close the browser
    driver.quit()
    print("Browser closed.")


if __name__ == "__main__":
    main()
