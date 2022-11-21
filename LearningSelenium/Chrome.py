from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#s = Service("C:\\browserdrivers\\chromedriver.exe")
#driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.rcvacademy.com")
driver.maximize_window()
driver.minimize_window()
print(driver.title)
driver.close()
