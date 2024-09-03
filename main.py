from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from mainClass import CoinDataGetting
from analize import make_table
import pandas as pd
import time

frames = []


# Initialize Firefox driver
service = Service(executable_path="./webdriver/geckodriver")
driver = webdriver.Firefox(service=service)

#coin_data searching parameters
'''
index:
0 - price_div xpath
1 - table_div xpath
2 - historical data btn 
'''
COINS_AND_XPATHS = {'bitcoin':[
    '/html/body/div[2]/main/div/div[2]/div[4]/div/div[1]/div[2]', 
                               '/html/body/div[2]/main/div/div[2]/div[6]/div[2]/table',  
                               '/html/body/div[2]/main/div/div[2]/div[6]/div[6]/div[1]/div[1]/table'
                               ], 

                    'ethereum': [
                        '/html/body/div[2]/main/div/div[2]/div[4]/div/div[1]/div[2]', 
                                 '/html/body/div[2]/main/div/div[2]/div[6]/div[2]/table',  
                                '/html/body/div[2]/main/div/div[2]/div[6]/div[6]/div[1]/div[1]/table'
                                ], 

                    'BNB':[
                        '/html/body/div[1]/main/div/div[2]/div[4]/div/div[1]/div[2]', 
                           '/html/body/div[1]/main/div/div[2]/div[6]/div[3]/table', 
                           '/html/body/div[1]/main/div/div[2]/div[6]/div[7]/div[1]/div[1]/table'
                           ], 

                    'Ripple': [
                        '/html/body/div[1]/main/div/div[2]/div[4]/div/div[1]/div[2]', 
                                '/html/body/div[1]/main/div/div[2]/div[6]/div[3]/table',  
                                '/html/body/div[1]/main/div/div[2]/div[6]/div[7]/div[1]/div[1]/table'
                                ], 

                    'Solana':[
                        '/html/body/div[2]/main/div/div[2]/div[4]/div/div[1]/div[2]', 
                              '/html/body/div[2]/main/div/div[2]/div[6]/div[3]/table',  
                                '/html/body/div[2]/main/div/div[2]/div[6]/div[7]/div[1]/div[1]/table' 
                                
                                ]}



try:
    # Navigate to CoinGecko
    driver.get("https://www.coingecko.com/")
    
    # Wait for the search bar to be visible and interactable
    wait = WebDriverWait(driver, 20)
    frames.clear()
    for coin, path in COINS_AND_XPATHS.items():
        coinsData = CoinDataGetting(driver=driver, By=By, Keys=Keys)
        make_table(coinsData.get_coin_price(coin_name=coin, price_div_xpath=path[0], table_div_xpath=path[1], historical_price_range_table=path[2])).to_excel(f'report{coin}.xlsx')
      
     



     



except Exception as e:
    
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)  # Give time to observe results before quitting
    driver.quit()
