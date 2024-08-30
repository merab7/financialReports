from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
import time

# Initialize Firefox driver
service = Service(executable_path="./webdriver/geckodriver")
driver = webdriver.Firefox(service=service)



try:
    # Navigate to CoinGecko
    driver.get("https://www.coingecko.com/")
    
    # Wait for the search bar to be visible and interactable
    wait = WebDriverWait(driver, 20)



    #intereact with search bar
    search_bar = driver.find_element(By.XPATH, '//*[@id="search-bar"]')

    # click on the serach bar for to change its state
    search_bar.click()
    
    #find input fild
    input_fild = driver.find_element(By.ID, "search-input-field")
    input_fild.click()
    # Enter coin name and submit search
    input_fild.clear()
    input_fild.send_keys('bitcoin')
    time.sleep(2)
    input_fild.send_keys(Keys.ENTER)
    time.sleep(2)
    price_div = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div[4]/div/div[1]/div[2]')
    coin_price = price_div.find_element(By.TAG_NAME, 'span').text
    print(coin_price)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)  # Give time to observe results before quitting
    driver.quit()
