import time
from selenium.webdriver.support import expected_conditions as EC



class CoinDataGetting:

    def __init__(self, driver, By,Keys) -> None:

        self.driver = driver
        self.By = By
        self.Keys = Keys
        
        
        self.search_bar = self.driver.find_element(By.XPATH, '//*[@id="search-bar"]')

        # click on the serach bar for to change its state
        self.search_bar.click()
        
        #find input fild
        self.input_fild = self.driver.find_element(By.ID, "search-input-field")
            # Enter coin name and submit search
        self.input_fild.clear()

    #this unction will get current price of the coin
    def get_coin_price(self, coin_name, price_div_xpath, table_div_xpath, historical_price_range_table):
        
        data = {}

        #get price
        self.input_fild.send_keys(str(coin_name))
        time.sleep(6)
        self.input_fild.send_keys(self.Keys.ENTER)
        time.sleep(2)
        price_div = self.driver.find_element(self.By.XPATH, f'{price_div_xpath}') 
        coin_price = price_div.find_element(self.By.TAG_NAME, 'span').text.replace(',', '').replace('.', '').replace('$', '')
        
        #get the table on the main page
        
        data = {coin_name:{'Current Price':coin_price,  }}

        table = self.driver.find_element(self.By.XPATH, f'{table_div_xpath}')
        table_body = table.find_element(self.By.TAG_NAME, "tbody")
        table_rows = table_body.find_elements(self.By.TAG_NAME, "tr")
  
        
        for rows in table_rows:
            #get the title of the parametere
            title = rows.find_element(self.By.TAG_NAME, "th").text
            
            #get the value_div
            value_div = rows.find_element(self.By.TAG_NAME, "td")
            #get the value
            value = value_div.text.replace(',', '').replace('.', '').replace('$', '')

            data[coin_name][title] = value
        
        
        #get 7 days historical data
        range_table = self.driver.find_element(self.By.XPATH, f'{historical_price_range_table}')
        range_table_body = range_table.find_element(self.By.TAG_NAME, "tbody")
        range_table_rows = range_table_body.find_elements(self.By.TAG_NAME, "tr")

        for row in range_table_rows:
            #get the title of the parametere
            title = row.find_element(self.By.TAG_NAME, "th").text

            if title.lower() == "7d range":
                seven_d_title = title
                seve_d_value = row.find_element(self.By.TAG_NAME, "td").text.replace(',', '').replace('.', '').replace('$', '')
                data[coin_name][seven_d_title] = seve_d_value

        
        return data
    
 
