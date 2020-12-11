from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://petfriends1.herokuapp.com/my_pets")
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.title_is((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.title_contains((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.visibility_of((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.presence_of_all_elements_located((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element_value((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.frame_to_be_available_and_switch_to_it((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.invisibility_of_element_located((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.element_to_be_selected((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.element_located_to_be_selected((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.element_selection_state_to_be((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.element_located_selection_state_to_be((By.ID, "myDynamicElement"))
)
element = WebDriverWait(driver, 10).until(
EC.alert_is_present((By.ID, "myDynamicElement"))
)