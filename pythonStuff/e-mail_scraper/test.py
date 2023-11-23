import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--remote-debugging-pipe")

driver = webdriver.Chrome(options=options)
driver.get("https://www.randomlists.com/email-addresses?qty=50")
time.sleep(5)
print(driver.title)