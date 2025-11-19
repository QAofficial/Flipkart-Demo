from selenium import webdriver
from selenium.webdriver.common.by import By
import time 



#selenium 3

'''driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_type("password").send_keys("admin123")

driver.find_element_by_class("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Login Test pass")
else:
    print("Login Test Fail ")

'''
driver.find_element(By.NAME)









'''
driver.get("https://www.google.com")

search = driver.find_element(By.NAME,"q")

search.send_keys("selenium")
search.submit()


driver.find_element(By.XPATH, "//h3[text()='selenium']").click()

'''








# driver.get("https://egyan.ptgn.in/admin/role")

#driver.get("https://demo.nopcommerce.com/")

#driver.get("https://admin-demo.nopcommerce.com/login")

# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Electronics")


# element = driver.find_element(By.XPATH, "//footer[@class='footer']//a")
# print(element.text)


# elements = driver.find_elements(By.XPATH, "//footer[@class='footer']//a")
# for el in elements:
#     print(el.text)


#driver.find_element(By.XPATH, "//input[@placeholder='Search name or email...']").send_keys("abc")

# login_element = driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()


# element = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(element))
# element[0].send_keys("Electronics")

# element = driver.find_elements(By.XPATH, "//div[@clsss='tr']//th")
# for ele in element:
#     print(ele)

'''
elements = driver.find_elements(By.XPATH, "//footer[@class='footer']//a")
print(len(elements))
# print(elements[0].text)

for ele in elements:
    print(ele.text)
'''


# email_box = driver.find_element(By.XPATH, "//input[@id='Email'] ")
# email_box.clear()
# email_box.send_keys("avb@gmail.com")
# print("Result of text : ",email_box.text)
# print("Result of get_attribute() : ",email_box.get_attribute('value'))


'''button = driver.find_element(By.XPATH, " //button[normalize-space()='Log in'] ")
print("Button text is : ",button.text)
print("Button Attibute is : ",button.get_attribute('value'))
print("Button attribute for class : ", button.get_attribute('class'))
print("Button attribute type : ", button.get_attribute('type'))


'''

# driver.get("https://www.snapdeal.com/ ")
# driver.get("https://www.amazon.in/")
# driver.back()
# driver.forward()
# driver.refresh()



# driver.find_element(By.ID,"small-searchterms").send_keys("Apple MacBook Pro")
#driver.find_element(By.NAME, "q").send_keys("Asus Laptop")

#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


# driver.find_element(By.CLASSNAME, "  ")

# links = driver.find_elements(By.TAG_NAME, "a")
# print(len(links))


#css selector   tag & id

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")

# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")

# driver.find_element(By.CSS_SELECTOR, "[data-testid='royal-email']").send_keys("abc@gmail.com")


#driver.find_element(By.CSS_SELECTOR, "[data-testid='royal-email']").send_keys("abc@gmail.com")

#driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid='royal-pass']").send_keys("abc")

#driver.find_element(By.XPATH, "//*[@id='navbarNav']/div/div/div[2]/li[2]/a/button")

#driver.find_element(by.xpath, '//*[@id="root"]/div/main/section[1]/h2')


#driver.find_element(By.XPATH, '//*[@id="root"]/div/aside/div[1]/h1')

# print(driver.title)
# print(driver.current_url)
# #print(driver.page_source)                       #rarely used

# ele = driver.find_element(By.XPATH, "//input[@placeholder='username']")
# print("Display status",ele.is_displayed())
# print("Enable: ",ele.is_enabled())
# print("Active:", ele.is_selected())

#driver.find_element(By.LINK_TEXT, " Inc").click()
#driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div[3]/div[3]/select[1]')


