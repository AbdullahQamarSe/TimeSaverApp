from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_extension('3.20.0_0.crx')

driver = webdriver.Chrome(options=options)
driver.get("chrome-extension://ailoabdmgclmfmhdagmlohpjlbpffblp/index.html")
time.sleep(5)
print("hi")
LoginButton = driver.find_elements(by=By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div/button')
if LoginButton:
    print("hi1")
    LoginButton[0].click()

window_handles = driver.window_handles
time.sleep(2)
# Switch to the second tab/window
window_handles = driver.window_handles
if len(window_handles) > 1:
    driver.switch_to.window(window_handles[-1])
    print("hi2")
    email = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/section/div[1]/form/div[1]/input')))
    if email:
        print("hi3")
        email[0].send_keys("ali14zaidi@gmail.com")

    password = driver.find_elements(by=By.XPATH, value='/html/body/div/div/div[2]/div[2]/section/div[1]/form/div[2]/input')
    if password:
        print("hi5")
        password[0].send_keys("Crystalmind786@")  
        print("hi6")


    button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/section/div[1]/form/button[1]')))
    if button:
        print("hi3")
        button[0].click()    

    print("hi4")

    button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/a[2]')))
    if button:
        print("hi3")
        button[0].click()

    search = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div/input')))
    if search:
        print("hi3")
        search[0].send_keys('Spain')      

    button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]')))
    if button:
        print("hi3")
        button[0].click()

print("hi7")
time.sleep(188)