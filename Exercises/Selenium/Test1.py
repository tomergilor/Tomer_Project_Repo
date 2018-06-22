# import time
# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.yahoo.com/')
#
#
# driver.find_element_by_id('uh-search-box').send_keys('software testing')
# driver.maximize_window()
# #driver.implicitly_wait(20)
# driver.find_element_by_id("uh-search-button").click()
#
# driver.find_element_by_id("yschsp").clear()
#
#
# # Wait for 5 seconds
# time.sleep(5)
#
#
# driver.quit()

print ("hi selenium")
#open Firefox Browser an navigate to google home page
from selenium import webdriver
# invoking firefox Browser
driver= webdriver.Firefox()
#hit the URL
driver.get("http://google.com")

print(driver.current_url)
print(driver.title)
print("Navigaating to gmail")
driver.get("http://gmail.com")
print(driver.title)
driver.back()
print("Came back to google home page")
print(driver.title)
driver.forward()
print("Came back to gmail home page")
print(driver.title)
driver.refresh()
driver.maximize_window()
# driver.close()
driver.quit()


