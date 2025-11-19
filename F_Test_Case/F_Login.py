from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com")

driver.find_element(By.XPATH, "//span[contains(text(),'Login')]").click()
driver.find_element(By.XPATH,"//input[contains(@class, 'r4vIwl')]").send_keys("najnee@sestinfotech.com")


driver.find_element(By.XPATH, "//button[contains(@class, 'QqFHMw')]").click()
time.sleep(3)

driver.find_element(By.XPATH, "//input[contains(@class, 'r4vIwl')]").send_keys(9899145041)

button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'twnTnD')]")
button.click()


time.sleep(10)