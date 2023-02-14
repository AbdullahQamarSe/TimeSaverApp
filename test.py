from selenium import webdriver
from PIL import Image
import requests
from selenium.webdriver.common.by import By
api_key = "87c7a62b9d6344c63e3d6a5c2c794018"
from twocaptcha import TwoCaptcha

solver = TwoCaptcha(api_key)

try:
        result = solver.normal("download.png")

except Exception as e:
        print("Captha Error", e)

else:
        try:
                print(result)
                code = result['code']
                print(code)
        except Exception as e:
                print("Captha Error", e)  