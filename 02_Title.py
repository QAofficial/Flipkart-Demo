from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
# driver.get(" https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.get("https://admin:admin@egyan.ptgn.in/login")

time.sleep(2)

'''driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
time.sleep(2)

# my_alert = driver.switch_to.alert
# my_alert.accept()
           #  or
driver.switch_to.alert.accept()


time.sleep(3)
driver.quit()'''


