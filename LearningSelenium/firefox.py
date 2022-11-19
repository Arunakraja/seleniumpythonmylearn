from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\browserdrivers\\geckodriver.exe")

driver = webdriver.Firefox(service=s)

driver.get("https://www.rcvacademy.com")

driver.maximize_window()

driver.minimize_window()

print(driver.title)

driver.close()
