from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time
import json
# Create your views here.

province = 'Zaragoza'
procedure = 'INFORMACIÓN'
office = 'Oficina de Extranjeros, Obispo Covarrubias , 1'
nie1 = 'X7476224M'
dni = '29130412S'
passport1 = 'AW389665'
name = 'test'
birth_year = 1999
origin_country = 'Pakistan'
expiration_date = []
email = 'test@gmail.com'
country = 'Pakistan'
phone = '3065458407'
Forign='Information'
Reason = 'Aoa'
SelectDate = ("8","July","2022")
code1="1234"

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://icp.administracionelectronica.gob.es/icpplus/index")


        
# Select province
province_select = driver.find_elements(by=By.XPATH, value='//*[@id="form"]')
tag_options = driver.find_elements(By.TAG_NAME, 'option')
if province_select:
        for option in tag_options:
                if option.text == province:
                        option.click()
                        break

accept_button = driver.find_elements(By.XPATH, '//*[@id="btnAceptar"]')        
accept_button[0].click() 
        
office_select = driver.find_elements(by=By.XPATH, value='//*[@id="sede"]')
tag_options = driver.find_elements(By.TAG_NAME, 'option')
if office_select:
        for option in tag_options:
                if option.text == office:
                        option.click()
                        break

Forign_select = driver.find_elements(by=By.XPATH, value='//*[@id="tramiteGrupo[0]"]')
tag_options = driver.find_elements(By.TAG_NAME, 'option')
if Forign_select:
        for option in tag_options:
                if option.text == Forign:
                        option.click()
                        break                

national_select = driver.find_elements(by=By.XPATH, value='//*[@id="tramiteGrupo[1]"]')
tag_options = national_select.find_elements_by_tag_name("option")
if Forign_select:
        for option in tag_options:
                if option.text == Forign:
                        option.click()
                        break 
                

accept_button = driver.find_elements(By.XPATH, '//*[@id="btnAceptar"]')        
accept_button[0].click() 

Enter_button = driver.find_elements(By.XPATH, '//*[@id="btnEntrar"]')
Enter_button[0].click()

nie = driver.find_elements(by=By.XPATH, value='//*[@id="comp04_id_citado"]/div[1]/fieldset/ul/li[1]')
if nie:
        nie[0].click()
        nieno_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
        if nieno_select:
                nieno_select.send_keys(nie1)
                
        nie_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')
        if nie_name:
                nie_name.send_keys(name)    
                
        nie_year = driver.find_elements(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
        if nie_year:
                nie_year.send_keys(birth_year)
        
        nie_country = driver.find_elements(by=By.XPATH, value='//*[@id="txtPaisNac"]')
        if nie_country:
                nie_country.send_keys(country)                    
                
id = driver.find_elements(by=By.XPATH, value='//*[@id="comp04_id_citado"]/div[1]/fieldset/ul/li[2]')
if id:
        id.click()
        id_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
        if id_select:
                id_select.send_keys(dni)
        
        id_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')        
        if id_name:
                id_name.send_keys(name)     
                
        id_year = driver.find_elements_by_XPATH(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
        if id_year:
                id_year.send_keys(birth_year)                   
                
        id_country = driver.find_elements_by_XPATH(by=By.XPATH, value='//*[@id="txtPaisNac"]') 
        if id_country:
                id_country.send_keys(country)      
                
passport = driver.find_elements(by=By.XPATH, value='//*[@id="comp04_id_citado"]/div[1]/fieldset/ul/li[3]')
if passport:
        passport.click()
        passport_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
        if passport_select:
                passport_select.send_keys(passport1)
        
        passport_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')        
        if passport_name:
                passport_name.send_keys(name)     
                
        passport_year = driver.find_elements_by_XPATH(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
        if passport_year:
                passport_year.send_keys(birth_year)                   
                
        passport_country = driver.find_elements_by_XPATH(by=By.XPATH, value='//*[@id="txtPaisNac"]') 
        if passport_country:
                passport_country.send_keys(country)  
                
                
accept_button = driver.find_elements(By.XPATH, '//*[@id="btnEnviar"]')        
accept_button[0].click()   

request_button = driver.find_elements(By.XPATH, '//*[@id="btnEnviar"]')        
request_button[0].click()                             

telephone_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtTelefonoCitado"]')
if telephone_select:
        telephone_select.send_keys(phone)

email_select = driver.find_elements(by=By.XPATH, value='//*[@id="emailUNO"]')
if email_select:
        email_select.send_keys(email)
                
email_select_repeat = driver.find_elements(by=By.XPATH, value='//*[@id="emailDOS"]')
if email_select_repeat:
        email_select_repeat.send_keys(email)
                
Reason_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtObservaciones"]')
if Reason_select:
        Reason_select.send_keys(Reason)
        
        
Next_button = driver.find_elements(By.XPATH, '//*[@id="btnSiguiente"]')
Next_button[0].click()        

calender_select  = driver.find_elements(by=By.XPATH, value='//*[@id="datepicker"]/div')
if calender_select :
        calender_select .send_keys(SelectDate)
        
 
       
ap1  = driver.find_elements(by=By.XPATH, value='//*[@id="cita1"]') 
if ap1:
        ap1.click    

table1  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]')
if table1:
        tb1  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]/tbody/tr[1]/td[2]')
        tb2  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]/tbody/tr[1]/td[3]')
        tb3  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]/tbody/tr[2]/td[1]')
        tb4  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]/tbody/tr[7]/td[1]')
        tb5  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]/tbody/tr[7]/td[2]')
        tb6  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]/tbody/tr[7]/td[3]') 
             
        if tb1 == "Free":
                tb1.click 
        
            
        elif tb2 == "Free":
                tb2.click 
                
           
        elif tb3 == "Free":
                tb3.click 
        
            
        elif tb4 == "Free":
                tb4.click 
        
            
        elif tb5 == "Free":
                tb5.click 
        
           
        elif tb6 == "Free":
                tb6.click                                                
        
           
Next_button = driver.find_elements(By.XPATH, '//*[@id="btnSiguiente"]')
if Next_button:
        Next_button[0].click()


check1 = driver.find_elements(by=By.XPATH, value='//*[@id="chkTotal"]')
check1.click

check2 = driver.find_elements(by=By.XPATH, value='//*[@id="enviarCorreo"]')
check2.click

code = driver.find_elements(by=By.XPATH, value='//*[@id="txtCodigoVerificacion"]')
code.send_keys(code1)

confirm = driver.find_elements(By.XPATH, '//*[@id="btnConfirmar"]')
if confirm:
        confirm[0].click()
                 