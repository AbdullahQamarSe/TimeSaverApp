from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import data_model
import time
from django.http import HttpResponse
from django.core.mail import send_mail
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import json
import imaplib
import email
from PIL import Image
import pytesseract
import Screenshot
import base64
import geckodriver_autoinstaller




def my_cron_job():
        data_model1 = data_model.objects.all() 
        for item in data_model1:
                if item.appointment == "NotApproved":
                        try:
                                from selenium.webdriver.firefox.options import Options
                                options = Options()
                                options.add_argument('--headless')
                                driver = webdriver.Firefox(options=options)
                                driver.get("https://icp.administracionelectronica.gob.es/icpplus/index")
                                
                                consent_button1=driver.find_elements(by=By.XPATH, value='//*[@id="cookie-law-info-bar"]')
                                if consent_button1:
                                        consent_button=driver.find_element(by=By.XPATH, value='//*[@id="cookie-law-info-bar"]')
                                        print("Accept")
                                        if consent_button:
                                                print("Accept")
                                                consent_button1=driver.find_element(by=By.XPATH, value='//*[@id="cookie_action_close_header"]')
                                                if consent_button1:
                                                        consent_button1.click()
                                                        print("Accept")

                                province_select = driver.find_elements(by=By.XPATH, value='//*[@id="form"]')
                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                if province_select:
                                        for option in tag_options:
                                                if option.text == item.province:
                                                        option.click()
                                                        break
                                                
                                accept_button = driver.find_elements(By.XPATH, '//*[@id="btnAceptar"]')        
                                if accept_button:
                                        accept_button[0].click()
                                     

                                Forign_select = driver.find_elements(by=By.XPATH, value='//*[@id="tramiteGrupo[0]"]')
                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                if Forign_select:
                                        for option in tag_options:
                                                if option.text == item.procedure:
                                                        option.click()
                                                        break                    

                                print("0")  
                                                

                                accept_button = driver.find_elements(By.XPATH, '//*[@id="btnAceptar"]')        
                                if accept_button:
                                        accept_button[0].click() 


                                
                                Enter = driver.find_elements(By.ID, 'btnEntrar')
                                if Enter:
                                        Enter[0].click()
                                
                                nie = driver.find_elements(by=By.XPATH, value='//*[@id="rdbTipoDocNie"]')
                                id = driver.find_elements(by=By.XPATH, value='//*[@id="rdbTipoDocDni"]')
                                passport = driver.find_elements(by=By.XPATH, value='//*[@id="rdbTipoDocPas"]')
                                passport1 = driver.find_elements(by=By.XPATH, value='//*[@id="rdbTipoDocPas"]')
                                
                                if item.nie != "":
                                        nie[0].click()
                                        nieno_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
                                        if nieno_select:
                                                nieno_select[0].send_keys(item.nie)
                                                
                                        nie_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')
                                        if nie_name:
                                                nie_name[0].send_keys(item.name)    
                                                
                                        nie_year = driver.find_elements(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
                                        if nie_year:
                                                nie_year[0].send_keys(item.birth_year)
                                        
                                        nie_country = driver.find_elements(by=By.XPATH, value='//*[@id="txtPaisNac"]')
                                        if nie_country:
                                                nie_country[0].send_keys(item.origin_country)  
                                                
                                        id = driver.find_elements(by=By.XPATH, value='txtPaisNac')
                                        print(province_select)
                                        tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                        if province_select:
                                                for option in tag_options:
                                                        if option.text == item.origin_country:
                                                                option.click()
                                                                break                            
                                                
                                
                                elif item.dni != "":
                                        id[0].click()
                                        id_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
                                        if id_select:
                                                id_select[0].send_keys(item.dni)
                                        
                                        id_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')        
                                        if id_name:
                                                id_name[0].send_keys(item.name)     
                                                
                                        id_year = driver.find_elements(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
                                        if id_year:
                                                id_year[0].send_keys(int(item.birth_year))
                                                time.sleep(10)                   
                                                
                                        id_country = driver.find_elements_by_XPATH(by=By.XPATH, value='//*[@id="txtPaisNac"]') 
                                        if id_country:
                                                id_country[0].send_keys(item.origin_country)
                                        
                                        id_country = driver.find_elements_by_XPATH(by=By.XPATH, value='//*[@id="txtPaisNac"]') 
                                        if id_country:
                                                id_country[0].send_keys(item.origin_country)
                                        
                                        
                                        id = driver.find_elements(by=By.XPATH, value='txtPaisNac')
                                        print(province_select)
                                        if id:
                                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                                if province_select:
                                                        for option in tag_options:
                                                                if option.text == item.origin_country:
                                                                        option.click()
                                                                        break               
                                                
                                
                                elif item.passport != "" or passport1!="":
                                        passport[0].click()
                                        
                                        passport_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
                                        if passport_select:
                                                passport_select[0].send_keys(item.passport)
                                        
                                        passport_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')        
                                        if passport_name:
                                                passport_name[0].send_keys(item.name)     
                                        
                                        nie_year = driver.find_elements(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
                                        if nie_year:
                                                nie_year[0].send_keys(item.birth_year) 
                                                        
                                        passport_country = driver.find_elements(by=By.XPATH, value='//*[@id="txtPaisNac"]') 
                                        if passport_country:
                                                passport_country[0].send_keys(item.origin_country)
                                        
                                        id = driver.find_elements(by=By.XPATH, value='txtPaisNac')
                                        print(province_select)
                                        if id:
                                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                                if province_select:
                                                        for option in tag_options:
                                                                if option.text == item.origin_country:
                                                                        option.click()
                                                                        break          
                                
                                elif passport1!="":
                                        passport1[0].click()
                                        
                                        passport_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtIdCitado"]')
                                        if passport_select:
                                                passport_select[0].send_keys(item.passport)
                                        
                                        passport_name = driver.find_elements(by=By.XPATH, value='//*[@id="txtDesCitado"]')        
                                        if passport_name:
                                                passport_name[0].send_keys(item.name)     
                                        
                                        nie_year = driver.find_elements(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
                                        if nie_year:
                                                nie_year[0].send_keys(item.birth_year) 
                                                        
                                        passport_country = driver.find_elements(by=By.XPATH, value='//*[@id="txtPaisNac"]') 
                                        if passport_country:
                                                passport_country[0].send_keys(item.origin_country)
                                        
                                        id = driver.find_elements(by=By.XPATH, value='txtPaisNac')
                                        print(province_select)
                                        if id:
                                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                                if province_select:
                                                        for option in tag_options:
                                                                if option.text == item.origin_country:
                                                                        option.click()
                                                                        break         
                                                                                                
                                accept_button = driver.find_elements(By.XPATH, '//*[@id="btnEnviar"]')        
                                accept_button[0].click()   
                                
                                
                                
                                request_button = driver.find_elements(By.XPATH, '//*[@id="btnEnviar"]')        
                                request_button[0].click()   
                                                        

                                next_buton = driver.find_elements(By.XPATH, '//*[@id="btnSiguiente"]')        
                                next_buton[0].click()    
                                
                                
                                telephone_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtTelefonoCitado"]')
                                if telephone_select:
                                        telephone_select[0].send_keys(item.phone)

                                email_select = driver.find_elements(by=By.XPATH, value='//*[@id="emailUNO"]')
                                if email_select:
                                        email_select[0].send_keys("timesaver459@gmail.com")
                                                
                                email_select_repeat = driver.find_elements(by=By.XPATH, value='//*[@id="emailDOS"]')
                                if email_select_repeat:
                                        email_select_repeat[0].send_keys("timesaver459@gmail.com")
                                                
                                Reason_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtObservaciones"]')
                                if Reason_select:
                                        Reason_select[0].send_keys("Many Reasons")
                                        
                                        
                                Next_button = driver.find_elements(By.XPATH, '//*[@id="btnSiguiente"]')
                                Next_button[0].click()        
                                                
                                ap1  = driver.find_elements(by=By.XPATH, value='//*[@id="cita2"]') 
                                if ap1:
                                        ap1[0].click()   
                                import requests
                                import time

                                # Replace YOUR_API_KEY with your actual 2captcha API key
                                api_key = "87c7a62b9d6344c63e3d6a5c2c794018"

                                import sys
                                import os
                                captcha_elements = driver.find_elements(by=By.XPATH, value='//*[@id="comp19_captcha"]/div/div[1]/div[2]/img')
                                if captcha_elements:
                                        captcha_img = driver.find_element(by=By.XPATH, value='//*[@id="comp19_captcha"]/div/div[1]/div[2]/img')
                                        captcha_src = captcha_img.get_attribute('src')


                                        from twocaptcha import TwoCaptcha

                                        solver = TwoCaptcha(api_key)

                                        try:
                                                result = solver.normal(captcha_src)

                                        except Exception as e:
                                                sys.exit(e)

                                        else:
                                                print(result)
                                                code = result['code']
                                                print(code)
                                        
                                        scaptha  = driver.find_elements(by=By.XPATH, value='//*[@id="captcha"]')
                                        scaptha[0].send_keys(code) 
                                
                                table1  = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]')
                                if table1:
                                        
                                        try:
                                                tb1  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575581"]');
                                                tb1.click()
                                                driver.switch_to.alert.accept()
                                                
                                        except:
                                                print("not found")
                                                try:
                                                        tb2  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575562"]');
                                                        tb2.click()
                                                        driver.switch_to.alert.accept() 
                                                        
                                                except:
                                                        print("not found")
                                                        try:
                                                                tb3  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575581"]');
                                                                tb3.click()
                                                                driver.switch_to.alert.accept() 
                                                                
                                                        except:
                                                                print("not found")
                                                                try:
                                                                        tb4  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575582"]');
                                                                        tb4.click()
                                                                        driver.switch_to.alert.accept() 
                                                                        
                                                                        
                                                                except:
                                                                        print("not found")
                                                                        try:
                                                                                tb5  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575575"]');
                                                                                driver.switch_to.alert.accept() 
                                                                                
                                                                        except:
                                                                                print("not found")
                                                                                try:
                                                                                        tb6  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575576"]')
                                                                                        driver.switch_to.alert.accept() 

                                                                                except:
                                                                                        print("not found")
                                                                                        try:
                                                                                                tb1  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575586"]')
                                                                                                tb1.click()
                                                                                                driver.switch_to.alert.accept()  
                                                                                        except:
                                                                                                print("not found")
                                                                                                try:
                                                                                                        tb2  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575587"]')
                                                                                                        tb2.click()
                                                                                                        driver.switch_to.alert.accept() 
                                                                                                        
                                                                                                except:
                                                                                                        print("not found")
                                                                                                        try:
                                                                                                                tb3  = driver.find_element(By.XPATH,value='//*[@id="HUECO62575578"]')
                                                                                                                tb3.click()
                                                                                                                driver.switch_to.alert.accept() 
                                                                                                                
                                                                                                        except:
                                                                                                                print("Appointment not found")                                              
                                
                                province_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtHora"]')
                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                if province_select:
                                        for option in tag_options:
                                                if option.text == "a partir de las 09:00":
                                                        option.click()
                                                        break
                                        

                                Next_button = driver.find_elements(By.XPATH, '//*[@id="btnSiguiente"]')
                                if Next_button:
                                        Next_button[0].click()
                                        driver.switch_to.alert.accept()
                                        
                                        
                                time.sleep(3)
                                driver.find_element(By.ID, value='chkTotal').click()
                                driver.find_element(By.ID, value='enviarCorreo').click()
                                time.sleep(60)
                                #credentials
                                username ="timesaver459@gmail.com"
                                #generated app password
                                app_password= "espmvyyylhqtbfma"
                                # https://www.systoolsgroup.com/imap/
                                gmail_host= 'imap.gmail.com'
                                #set connection
                                mail = imaplib.IMAP4_SSL(gmail_host)
                                #login
                                mail.login(username, app_password)
                                #select inbox
                                mail.select("INBOX")
                                #select specific mails
                                _, selected_mails = mail.search(None, '(FROM "no-conteste-a-esta-direccion@correo.gob.es")')
                                #total number of mails from specific user
                                print("Total Messages from no-conteste-a-esta-direccion@correo.gob.es" , len(selected_mails[0].split()))
                                for num in selected_mails[0].split():
                                        _, data = mail.fetch(num , '(RFC822)')
                                        _, bytes_data = data[0]
                                        #convert the byte data to message
                                        email_message = email.message_from_bytes(bytes_data)
                                        print("\n===========================================")
                                        #access data
                                        print("Subject: ",email_message["subject"])
                                        print("To:", email_message["to"])
                                        print("From: ",email_message["from"])
                                        print("Date: ",email_message["date"])
                                        for part in email_message.walk():
                                                if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                                                        message = part.get_payload(decode=True)
                                                        print("Message: \n", message.decode())
                                                        print("==========================================\n")
                                                        break          
                                code = message[72:77]
                                z=code.decode("utf-8")
                                code = driver.find_elements(by=By.XPATH, value='//*[@id="txtCodigoVerificacion"]')
                                if code:
                                        code[0].send_keys(z)

                                confirm = driver.find_elements(By.XPATH, '//*[@id="btnConfirmar"]')
                                if confirm:
                                        confirm[0].click()                                 
                                time.sleep(60)
                                proof = driver.find_elements(By.XPATH, '//*[@id="justificanteFinal"]')
                                direction = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div[7]/fieldset/div[1]/span[2]')
                                Appointmentday = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div[7]/fieldset/div[2]/span[2]')
                                Appointmenttime = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div[7]/fieldset/div[3]/span[2]')
                                Desk = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div[7]/fieldset/div[4]/span[2]')
                                
                                Detail  = f"Direction : {direction[0].text} \n Appointmentday : {Appointmentday[0].text} \n Appointment Time : {Appointmenttime[0].text} \n Desk :{Desk[0].text}  \n"
                                message = f"Proof of Appointment : {proof[0].text} \n Name : {item.name} \n Nie : {item.nie} \n Dni : {item.dni} \n Passport : {item.passport} \n Phone : {item.phone} \n Email : {item.email} \n {Detail}"                                 
                                
                                send_mail(
                                'Appointment Details',
                                message,
                                'timesaver459@gmail.com',
                                [item.email],
                                fail_silently=False,
                                )
        
                                item.appointment = "Approved"
                                item.save()        
                                return HttpResponse("Appointment booked")                  
                                        
                        except Exception as e:
                                print("Block By Website",e) 
                                