# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver.get("https://egyan.ptgn.in/login")

# print("Page title is:", driver.title)

# driver.quit()



# driver = webdriver.Chrome()

'''# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()


# driver.find_element_by_name("name").send_keys("Admin")
# driver.find_element_by_type("type").send_keys("admin123")
# actual_title = driver.title
# expected_title = "OrangeHRM"

# if actual_title == expected_title :
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")

# driver.close()

driver.maximize_window()
# driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")

# driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad Carbon Laptop")

# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
'''


driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")

time.sleep(5)
driver.close()



