import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the URL with an expired SSL certificate
    driver.get("https://expired.badssl.com/")
    
    # Wait for 5 seconds to observe the page
    time.sleep(5)  # Adjust the time as needed

finally:
    driver.save_screenshot("ssl_handled.png")
    # Close the driver
    driver.quit()