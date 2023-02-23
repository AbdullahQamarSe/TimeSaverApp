import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.firefox.options import Options
# get the path to the user's home directory
home_dir = os.path.expanduser("~")

# construct the path to the default Firefox profile directory
firefox_profile_dir = os.path.join(home_dir, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")

# find the name of the default Firefox profile directory
profile_name = None
for name in os.listdir(firefox_profile_dir):
    if name.endswith(".Default User"):
        profile_name = name
        break

# construct the path to the default Firefox profile directory
firefox_profile_dir = os.path.join(firefox_profile_dir, profile_name)

from selenium import webdriver
import time

# create a Firefox driver with the default profile
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=firefox_profile_dir)
options = Options()
# navigate to a webpage

driver.get("moz-extension://aff4ff16-e595-443f-881f-3f56ea619eda/index.html")
print("hi")

search = driver.find_elements(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div')
if search:
        print("hi1")
        search[0].click()



print("hi2")
search1 = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="input-label-9D284BCE-65D0-8E89-CD9B-3BB803B75458"]')))
if search1:
        print("hi3")
        search1[0].send_keys("Spain")

