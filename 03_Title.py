from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://egyan.ptgn.in/login")
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.TYPE,"password").send_keys("admin123")
# driver.find_element(By.ID,"Login").click()




driver.maximize_window()
# driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input").send_keys("Grocery")
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/header/div[1]/div[2]/form/div/button").click()

driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input").send_keys("Grocery")
driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/header/div[1]/div[2]/form/div/button").click()





time.sleep(10)
driver.close()



