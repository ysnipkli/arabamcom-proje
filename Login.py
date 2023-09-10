
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
user1 = 'ykipekli@gmail.com'  #True Email
user2 = 'ykipeklii@gmail.com' #False Email
pass1 = 123456 #True Password
pass2 = 1234567 #False Password
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.arabam.com/uyelik?returnUrl=/")
driver.maximize_window()
time.sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, 'button#btnLoginWithGoogle')
login_button.click()
time.sleep(2)

#True Email - True Password. State 1
driver.find_element(By.ID,"identifierId").send_keys(user1)
time.sleep(5)
driver.find_element(By.ID, "identifierNext").click()

driver.find_element(By.NAME, "password").send_keys(pass1)
time.sleep(3)
driver.find_element(By.ID, "passwordNext").click()
time.sleep(2)

#False Email - True Password. State 2
#driver.find_element(By.ID,"identifierId").send_keys(user2)
#time.sleep(5)
#driver.find_element(By.ID, "identifierNext").click()
#True Email - False Password
#driver.find_element(By.NAME, "password").send_keys(pass1)
#time.sleep(3)
#driver.find_element(By.ID, "passwordNext").click()
#time.sleep(2)

#False email - False Password. State 3
#driver.find_element(By.ID,"identifierId").send_keys(user2)
#time.sleep(5)
#driver.find_element(By.ID, "identifierNext").click()

#driver.find_element(By.NAME, "password").send_keys(pass2)
#time.sleep(3)
#driver.find_element(By.ID, "passwordNext").click()
#time.sleep(2)

#True Email - False Password State 4
#driver.find_element(By.ID,"identifierId").send_keys(user1)
#time.sleep(5)
#driver.find_element(By.ID, "identifierNext").click()

#driver.find_element(By.NAME, "password").send_keys(pass2)
#time.sleep(3)
#driver.find_element(By.ID, "passwordNext").click()
#time.sleep(2)









# 1. Pozitif Test

# 2. Negatif Test





