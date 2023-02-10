#title: Running chrome browser and open link
from selenium import webdriver
import time

# driver = webdriver.Chrome(executable_path="C:/Browser/chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
print(driver.title)
driver.maximize_window()


time.sleep(3600)