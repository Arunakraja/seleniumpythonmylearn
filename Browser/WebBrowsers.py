from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdrivermanager import GeckoDriverManager

chromedriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
egdriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
firedriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))