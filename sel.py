from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection

# Set up the Chrome options
chrome_options = Options()


settings = initialize_vpn("France")  # starts nordvpn and stuff
rotate_VPN(settings)  # actually connect to server

# YOUR STUFF


# Set up the VPN
# # Replace with your VPN server address and port

# Start the Chrome driver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website to check your location
driver.get('https://www.whatismyip.com/')
time.sleep(100)
