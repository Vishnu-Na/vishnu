import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(4)
element=driver.find_element(By.XPATH,"//button[.='Copy Text']")
actions=ActionChains(driver)
actions.double_click(element).perform()
time.sleep(4)
driver.quit()


