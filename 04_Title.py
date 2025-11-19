from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('--------------')
driver.maximize_window('------------')



driver.find_element(By.XPATH, .....).click()

checkboxes = driver.find_elements(By.XPATH, "Alterly")
print(len(checkboxes))


for i in range(len(checkboxes)):
    checkboxes[i].click()


for checkbox in checkboxes:
    checkbox.click()

for checkbox in checkboxes:
    weekname = check.get_attribute('id')
    if weekname == 'monday' or weekname == 'sunday':
        checkbox.click()



for i in range(len(checkboxes)-2, len(checkboxes)):   
    checkboxes[i].click()


for i in range(len(checkboxes)):
    if i <2 :
        checkboxes[i].click()


for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()









 