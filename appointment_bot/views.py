from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import data_model
import time
from django.http import HttpResponse
import django
django.setup()
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from appointment_bot.models import data_model
import time
import time
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
from selenium import webdriver
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import time
import schedule    
from apscheduler.schedulers.background import BackgroundScheduler
import time

# Create your views here.

def base(request):
        
        '''
        province = request.POST.get("province")
        procedure = request.POST.get("procedure")
        nie = request.POST.get("nie")
        dni = request.POST.get("dni")
        passport = request.POST.get("passport")
        name = request.POST.get("name")
        birth_year = request.POST.get("birth_year")
        origin_country = request.POST.get("country_of_birth")
        expiration_date = request.POST.get("expirate_date")
        email = request.POST.get("email")
        country = request.POST.get("country")
        phone = request.POST.get("phone")
        print(province)
        print(phone)
        '''
        if request.method == "POST":

                model_instance = data_model()
                model_instance.province = request.POST.get("province")
                model_instance.procedure = request.POST.get("procedure")
                model_instance.nie = request.POST.get("nie")
                model_instance.dni = request.POST.get("dni")
                model_instance.passport = request.POST.get("passport")
                model_instance.name = request.POST.get("name")
                model_instance.birth_year = request.POST.get("birth_year")
                model_instance.origin_country = request.POST.get("country_of_birth")
                model_instance.expiration_date = request.POST.get("expirate_date")
                model_instance.email = request.POST.get("email")
                model_instance.country = request.POST.get("country")
                model_instance.phone = request.POST.get("phone")
                model_instance.reason = request.POST.get("reason")
                message = f"Your appointment form is submitted successfully. \n We’ll share the appointment details soon! \n DATA OF THE QUOTED \n Name : {model_instance.name} \n Nie : {model_instance.nie} \n Dni : {model_instance.dni} \n Passport : {model_instance.passport} \n Phone : {model_instance.phone} \n Email : {model_instance.email} \n "
                send_mail(
                'Appointment Form Successfull',
                message,
                'abdullah.qfnetwork@gmail.com',
                [model_instance.email],
                fail_silently=False,
                )
                messages.success(request, 'Your form is submitted successfully')
                print("Message Save") 

                # Save the model instance to the database
                model_instance.save()
                                                           
        return render(request, 'base.html')

def scrap(request):        
        data_model1 = data_model.objects.all()
        for item in data_model1:
                if item.appointment == "NotApproved":
                        try:
                                import time
                                from selenium.webdriver.firefox.options import Options
                                options = Options()
                                #options.add_argument('--headless')
                                driver = webdriver.Firefox(options=options)
                                driver.get("https://icp.administracionelectronica.gob.es/icpplus/index")
                                import time

                                consent_button1 = driver.find_elements(by=By.XPATH,
                                                                       value='//*[@id="cookie-law-info-bar"]')
                                if consent_button1:
                                        consent_button = driver.find_element(by=By.XPATH,
                                                                             value='//*[@id="cookie-law-info-bar"]')
                                        print("Accept")
                                        if consent_button:
                                                print("Accept")
                                                consent_button1 = driver.find_element(by=By.XPATH,
                                                                                      value='//*[@id="cookie_action_close_header"]')
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

                                        id = driver.find_elements(by=By.XPATH, value='//*[@id="txtPaisNac"]')
                                        print(province_select)
                                        tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                        if province_select:
                                                for option in tag_options:
                                                        if option.text == item.country.upper():
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

                                        id = driver.find_elements(by=By.XPATH, value='//*[@id="txtPaisNac"]')
                                        print(province_select)
                                        if id:
                                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                                if province_select:
                                                        for option in tag_options:
                                                                if option.text == item.country.upper():
                                                                        option.click()
                                                                        break


                                elif item.passport != "":
                                        passport[0].click()

                                        passport_select = driver.find_elements(by=By.XPATH,
                                                                               value='//*[@id="txtIdCitado"]')
                                        if passport_select:
                                                passport_select[0].send_keys(item.passport)

                                        passport_name = driver.find_elements(by=By.XPATH,
                                                                             value='//*[@id="txtDesCitado"]')
                                        if passport_name:
                                                passport_name[0].send_keys(item.name)

                                        nie_year = driver.find_elements(by=By.XPATH, value='//*[@id="txtAnnoCitado"]')
                                        if nie_year:
                                                nie_year[0].send_keys(item.birth_year)

                                        print("Country", item.country.upper())

                                        province_select = driver.find_elements(by=By.XPATH,
                                                                               value='//*[@id="txtPaisNac"]')
                                        tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                        if province_select:
                                                for option in tag_options:
                                                        if option.text == item.country.upper():
                                                                option.click()
                                                                break

                                accept_button = driver.find_elements(By.XPATH, '//*[@id="btnEnviar"]')
                                accept_button[0].click()

                                request_button = driver.find_elements(By.XPATH, '//*[@id="btnEnviar"]')
                                request_button[0].click()

                                next_buton = driver.find_elements(By.XPATH, '//*[@id="btnSiguiente"]')
                                next_buton[0].click()

                                time.sleep(20)
                                telephone_select = driver.find_elements(by=By.XPATH,
                                                                        value='//*[@id="txtTelefonoCitado"]')
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

                                ap1 = driver.find_elements(by=By.XPATH, value='//*[@id="cita2"]')
                                if ap1:
                                        ap1[0].click()
                                import requests
                                import time

                                # Replace YOUR_API_KEY with your actual 2captcha API key
                                api_key = "87c7a62b9d6344c63e3d6a5c2c794018"

                                import sys
                                import os
                                import requests
                                import base64
                                from PIL import Image
                                
                                captcha_elements = driver.find_elements(by=By.XPATH, value='//*[@id="comp19_captcha"]/div/div[1]/div[2]/img')
                                if captcha_elements:
                                        captcha_img = driver.find_element(by=By.XPATH,value='//*[@id="comp19_captcha"]/div/div[1]/div[2]/img')
                                        captcha_src = captcha_img.get_attribute('src')
                                        img = Image.open(requests.get(captcha_src, stream=True).raw)
                                        img.show()
                                        
                                        api_key = "87c7a62b9d6344c63e3d6a5c2c794018"
                                        from twocaptcha import TwoCaptcha

                                        solver = TwoCaptcha(api_key)

                                        try:
                                                result = solver.normal(img)

                                        except Exception as e:
                                                print("Captha Error", e)

                                        else:
                                                try:
                                                        print(result)
                                                        code = result['code']
                                                        print(code)
                                                except Exception as e:
                                                        print("Captha Error", e)   
                                        
                                           
                                        scaptha = driver.find_elements(by=By.XPATH, value='//*[@id="captcha"]')
                                        if scaptha:
                                                scaptha[0].send_keys(code)
                                                
                                                
                                                
                                                
                                                
                                table1 = driver.find_elements(by=By.XPATH, value='//*[@id="VistaMapa_Datatable"]')
                                if table1:

                                        try:
                                                tb1 = driver.find_element(By.XPATH, value='//*[@id="HUECO62575581"]');
                                                tb1.click()
                                                driver.switch_to.alert.accept()

                                        except:
                                                print("not found")
                                                try:
                                                        tb2 = driver.find_element(By.XPATH,
                                                                                  value='//*[@id="HUECO62575562"]');
                                                        tb2.click()
                                                        driver.switch_to.alert.accept()

                                                except:
                                                        print("not found")
                                                        try:
                                                                tb3 = driver.find_element(By.XPATH,
                                                                                          value='//*[@id="HUECO62575581"]');
                                                                tb3.click()
                                                                driver.switch_to.alert.accept()

                                                        except:
                                                                print("not found")
                                                                try:
                                                                        tb4 = driver.find_element(By.XPATH,
                                                                                                  value='//*[@id="HUECO62575582"]');
                                                                        tb4.click()
                                                                        driver.switch_to.alert.accept()


                                                                except:
                                                                        print("not found")
                                                                        try:
                                                                                tb5 = driver.find_element(By.XPATH,
                                                                                                          value='//*[@id="HUECO62575575"]');
                                                                                driver.switch_to.alert.accept()

                                                                        except:
                                                                                print("not found")
                                                                                try:
                                                                                        tb6 = driver.find_element(
                                                                                                By.XPATH,
                                                                                                value='//*[@id="HUECO62575576"]')
                                                                                        driver.switch_to.alert.accept()

                                                                                except:
                                                                                        print("not found")
                                                                                        try:
                                                                                                tb1 = driver.find_element(
                                                                                                        By.XPATH,
                                                                                                        value='//*[@id="HUECO62575586"]')
                                                                                                tb1.click()
                                                                                                driver.switch_to.alert.accept()
                                                                                        except:
                                                                                                print("not found")
                                                                                                try:
                                                                                                        tb2 = driver.find_element(
                                                                                                                By.XPATH,
                                                                                                                value='//*[@id="HUECO62575587"]')
                                                                                                        tb2.click()
                                                                                                        driver.switch_to.alert.accept()

                                                                                                except:
                                                                                                        print("not found")
                                                                                                        try:
                                                                                                                tb3 = driver.find_element(
                                                                                                                        By.XPATH,
                                                                                                                        value='//*[@id="HUECO62575578"]')
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
                                # credentials
                                username = "abdullah.qfnetwork@gmail.com"
                                # generated app password
                                app_password = "coquekobqyakqwkq"
                                # https://www.systoolsgroup.com/imap/
                                gmail_host = 'imap.gmail.com'
                                # set connection
                                mail = imaplib.IMAP4_SSL(gmail_host)
                                # login
                                mail.login(username, app_password)
                                # select inbox
                                mail.select("INBOX")
                                # select specific mails
                                _, selected_mails = mail.search(None,
                                                                '(FROM "no-conteste-a-esta-direccion@correo.gob.es")')
                                # total number of mails from specific user
                                print("Total Messages from no-conteste-a-esta-direccion@correo.gob.es",
                                      len(selected_mails[0].split()))
                                for num in selected_mails[0].split():
                                        _, data = mail.fetch(num, '(RFC822)')
                                        _, bytes_data = data[0]
                                        # convert the byte data to message
                                        email_message = email.message_from_bytes(bytes_data)
                                        print("\n===========================================")
                                        # access data
                                        print("Subject: ", email_message["subject"])
                                        print("To:", email_message["to"])
                                        print("From: ", email_message["from"])
                                        print("Date: ", email_message["date"])
                                        for part in email_message.walk():
                                                if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                                                        message = part.get_payload(decode=True)
                                                        print("Message: \n", message.decode())
                                                        print("==========================================\n")
                                                        break
                                code = message[72:77]
                                z = code.decode("utf-8")
                                code = driver.find_elements(by=By.XPATH, value='//*[@id="txtCodigoVerificacion"]')
                                if code:
                                        code[0].send_keys(z)

                                confirm = driver.find_elements(By.XPATH, '//*[@id="btnConfirmar"]')
                                if confirm:
                                        confirm[0].click()
                                time.sleep(2)

                                page_height = driver.execute_script("return document.body.scrollHeight")
                                # Set the height of the browser window to the height of the entire page
                                driver.set_window_size(1720, page_height)
                                screenshot = driver.save_screenshot("screenshot.png")
                                # Create the email
                                msg = MIMEMultipart()
                                text = MIMEText(
                                        f"Hi {item.name}, \n Please find attached details for your appointment. ")
                                msg.attach(text)
                                msg['Subject'] = "Appointment details"
                                # Attach the screenshot to the email
                                with open("screenshot.png", "rb") as f:
                                        img = MIMEImage(f.read())
                                        msg.attach(img)

                                # Send the email
                                smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
                                smtp_server.ehlo()
                                smtp_server.starttls()
                                smtp_server.ehlo()
                                smtp_server.login("abdullah.qfnetwork@gmail.com", "coquekobqyakqwkq")
                                smtp_server.sendmail("abdullah.qfnetwork@gmail.com", item.email, msg.as_string())
                                smtp_server.quit()

                                item.appointment = "Approved"
                                item.save()
                        except Exception as e:
                                print("Block By Website", e)
                                