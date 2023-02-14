

im = 'D:\download (1).jpg'


import requests
import time

# Replace YOUR_API_KEY with your actual 2captcha API key
api_key = "87c7a62b9d6344c63e3d6a5c2c794018"

import sys
import os


from twocaptcha import TwoCaptcha

solver = TwoCaptcha(api_key)

try:
    result = solver.normal(im)

except Exception as e:
    sys.exit(e)

else:
    print(result)
    code = result['code']
    print(code)
    
 