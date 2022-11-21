from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service

chromeser = Service("C:\\browserdrivers\\chromedriver.exe")
edgeser = Service("C:\\browserdrivers\\msedgedriver.exe")
foxser = Service("C:\\browserdrivers\\geckodriver.exe")

driver = webdriver.Chrome(service=chromeser)
egdriver = webdriver.Edge(service=edgeser)
firedriver = webdriver.Firefox(service=foxser)

driver.get("https://www.rcvacademy.com")
egdriver.get("https://www.rcvacademy.com")
firedriver.get("https://www.rcvacademy.com")

driver.maximize_window()
egdriver.maximize_window()
firedriver.maximize_window()

driver.minimize_window()
egdriver.minimize_window()
firedriver.minimize_window()

print(driver.title)
print(egdriver.title)
print(firedriver.title)

driver.close()
egdriver.close()
firedriver.close()
