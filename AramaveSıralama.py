from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service("./chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://www.arabam.com/")   ##ilgili url e gider.
driver.maximize_window()
time.sleep(2)

search_box = driver.find_element(By.CSS_SELECTOR, "input.input")
search_box.send_keys("Ford")
time.sleep(2)

search_button = driver.find_element(By.CSS_SELECTOR, "button.search-button") ## butona tıklanır. Listeler.
search_button.click()
time.sleep(2)

#Fiyat butonuna tıklayarak sıralama
#fiyat_button = driver.find_element(By.XPATH, '//a[@id="color-red4-on-hover tdu-on-hover sorting-item"]/thead/tr/td[5]/a') ## Fiyat butonuna tıklanır. Sıralama azalan artan olarak yapılır.
#fiyat_button.click()

prices = driver.find_element(By.CSS_SELECTOR, '.db.no-wrap.listing-price')

# Create a dictionary to store prices as integers
price_map = {}
for price in prices:
    text = price.text
    if text != "":
        price_map[price] = int(''.join(filter(str.isdigit, text)))
time.sleep(2)
# Print the original price map
for key, value in price_map.items():
    print(key, value)
time.sleep(2)
# Sort the price map by value
sorted_prices = sorted(price_map.items(), key=lambda x: x[1])

# Print the sorted price map
for key, value in sorted_prices:
    print(key, value)
time.sleep(2)
# Click on the second highest price product
sorted_prices[-2][0].click()

# Close the WebDriver
driver.quit()