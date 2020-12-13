from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

#driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
driver=webdriver.Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

driver.get("https://www.computerhope.com/jargon/u/url.htm")

print(driver.title)  #Title of the page

print(driver.current_url)

driver.close()       #Close the web page

