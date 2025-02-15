from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = Options()

# Initialize the Chrome WebDriver with the Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open the URL
driver.get("https://link.onylinks.com/R9BZxty3")  # Replace with your actual URL

while driver.execute_script("return document.readyState;") != "complete":
    time.sleep(1)  # Wait for 1 second before checking again

    
time.sleep(5)
button4 = driver.find_element(By.XPATH, "//*[@id='top-sticky-close-icon']")  # Adjust XPath if needed
button4.click()

time.sleep(2)

for i in range(2):
    # Scroll down by a specific amount (e.g., 1000 pixels)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)  # Wait for a moment before the next scroll

# Wait for 16 seconds
time.sleep(15)

# Click the "Click here to continue" button (adjust selector as needed)
button1 = driver.find_element(By.XPATH, "//*[@id='scroll']")  # Adjust XPath if needed
button1.click()

# Wait for 5 seconds
time.sleep(5)

# Click the "Continue" button (adjust selector as needed)
button2 = driver.find_element(By.XPATH, "//*[@id='getlinks']") # Adjust XPath if needed
button2.click()


# Optional: Wait a bit to observe the result before closing (optional)
time.sleep(6)


# Close the browser
driver.quit()
