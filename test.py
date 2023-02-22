from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

PROXY_HOST = '202.159.60.145'
PROXY_PORT = 443

# Set up a proxy object
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': f'{PROXY_HOST}:{PROXY_PORT}',
    'ftpProxy': f'{PROXY_HOST}:{PROXY_PORT}',
    'sslProxy': f'{PROXY_HOST}:{PROXY_PORT}',
})

# Set up a Firefox webdriver with the proxy object
driver = webdriver.Firefox(proxy=proxy)

# Navigate to a website to test the proxy
driver.get('https://www.whatismyip.com/')

# Check if the proxy is working
if PROXY_HOST in driver.page_source:
    print('Proxy is working')
else:
    print('Proxy is not working')
    
# Close the webdriver
driver.quit()
