from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://petfriends1.herokuapp.com/")
myDynamicElement = driver.find_element_by_id("myDynamicElement")