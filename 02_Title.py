from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# Absolute Xpath

'''
driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Shoes")
driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()
'''

# Relative Xpath

driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("Shoes")
driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()

# OR

# driver.find_element(By.XPATH,"")

time.sleep(5)
driver.close()











































