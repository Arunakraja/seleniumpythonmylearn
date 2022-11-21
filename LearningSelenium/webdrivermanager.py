from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdrivermanager import GeckoDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
egdriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
firedriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

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
