import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "icp_appointment.settings")
import django
django.setup()
from appointment_bot.models import data_model
import time
import time
from django.core.mail import send_mail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import schedule
from twocaptcha import TwoCaptcha
import requests
from PIL import Image

print("Code Run --")

def run_code():
        print("Geting Data From DataBase")
        data_model1 = data_model.objects.all()
        print("starting Loop")
        for item in data_model1:
                if item.appointment == "NotApproved":
                        try:
                                print("Selenium Starting")
                                
                                options = Options()
                                print("Open Driver")
                                
                                #options.add_argument('--headless')
                                driver = webdriver.Firefox(options=options)
                                print("Open Window")
                                driver.get("https://icp.administracionelectronica.gob.es/icpplus/index")
                                
                                print("Accept Cookie")
                                
                                consent_button1 = WebDriverWait(driver, 300).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="cookie-law-info-bar"]'))
                                )
                                time.sleep(3)
                                if consent_button1:
                                        consent_button = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookie-law-info-bar"]')))
                                        print("Accept")
                                        time.sleep(3)
                                        if consent_button:
                                                print("Accept")
                                                consent_button2 = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookie_action_close_header"]')))
                                                time.sleep(3)
                                                if consent_button2:
                                                        consent_button2.click()
                                                        print("Accept")
                                                        
                                
                                print("Accept by Cookie")
                                province_select = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="form"]')))
                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                if province_select:
                                        for option in tag_options:
                                                if option.text == item.province:
                                                        print("Province Accept")
                                                        option.click()
                                                        break
                                                
                                accept_button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btnAceptar"]')))
                                if accept_button:
                                        print("Accept Button")
                                        accept_button[0].click()
                                        
                                time.sleep(10)
                                Forign_select = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="tramiteGrupo[0]"]')))
                                tag_options = driver.find_elements(By.TAG_NAME, 'option')
                                if Forign_select:
                                        for option in tag_options:
                                                if option.text == item.procedure:
                                                        print("Office Select")
                                                        option.click()
                                                        break

                                time.sleep(3)
                                accept_button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btnAceptar"]')))
                                if accept_button:
                                        print("Accept Button")
                                        accept_button[0].click()   
                                time.sleep(3)    
                                Enter = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.ID, 'btnEntrar')))
                                if Enter:
                                        Enter[0].click()
                                        print("Press Enter")
                                
                                nie = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="rdbTipoDocNie"]')))
                                id = driver.find_elements(by=By.XPATH, value='//*[@id="rdbTipoDocDni"]')
                                passport = driver.find_elements(by=By.XPATH, value='//*[@id="rdbTipoDocPas"]')
                                time.sleep(3)
                                if item.nie != "":
                                        print("User Information")
                                        time.sleep(7)
                                        print("Nie")
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
                                        print("User Information")
                                        time.sleep(7)
                                        print("Dni")
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
                                        time.sleep(3)
                                        print("User Information")
                                        time.sleep(3)
                                        print("Passport")
                                        passport[0].click()
                                        time.sleep(3)
                                        print("Done")
                                        passport_select = driver.find_elements(by=By.XPATH,value='//*[@id="txtIdCitado"]')
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
                                accept_button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btnEnviar"]')))
                                accept_button[0].click()
                                time.sleep(3)
                                request_button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btnEnviar"]')))
                                request_button[0].click()
                                time.sleep(3)
                                next_buton = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btnSiguiente"]')))
                                next_buton[0].click()
                                time.sleep(3)
                                telephone_select = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="txtTelefonoCitado"]')))
                                if telephone_select:
                                        print("Telephone")
                                        telephone_select[0].send_keys(item.phone)

                                email_select = driver.find_elements(by=By.XPATH, value='//*[@id="emailUNO"]')
                                if email_select:
                                        print("Email")
                                        email_select[0].send_keys("dtox142@gmail.com")

                                email_select_repeat = driver.find_elements(by=By.XPATH, value='//*[@id="emailDOS"]')
                                if email_select_repeat:
                                        email_select_repeat[0].send_keys("dtox142@gmail.com")

                                Reason_select = driver.find_elements(by=By.XPATH, value='//*[@id="txtObservaciones"]')
                                if Reason_select:
                                        Reason_select[0].send_keys("Many Reasons")
                                time.sleep(3)
                                Next_button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btnSiguiente"]')))
                                Next_button[0].click()
                                
                                time.sleep(3)
                                print("Appointment")
                                ap1 = driver.find_elements(by=By.XPATH, value='//*[@id="cita1"]')
                                if ap1:
                                        ap1[0].click()

                                # Replace YOUR_API_KEY with your actual 2captcha API key
                                api_key = "87c7a62b9d6344c63e3d6a5c2c794018"

                                captcha_elements = driver.find_elements(by=By.XPATH, value='//*[@id="comp19_captcha"]/div/div[1]/div[2]/img')
                                if captcha_elements:
                                        print("Captha")
                                        try:
                                            captcha_img = driver.find_element(by=By.XPATH,value='//*[@id="comp19_captcha"]/div/div[1]/div[2]/img')
                                            captcha_src = captcha_img.get_attribute('src')
                                            
                                        except Exception as e:
                                                print("Captha Error", e)
                                        
                                        api_key = "5f1392c749eba289f63318932bb3f966"
                                        

                                        solver = TwoCaptcha(api_key)

                                        try:
                                                result = solver.normal(captcha_src)

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
                                        print("Table")

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
                                print("Code Send")
                                time.sleep(20)
                                
                                check1 = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.ID, 'chkTotal')))
                                check2 = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.ID, 'enviarCorreo')))
                                
                                if check1:
                                        check1[0].click()
                                if check2:
                                        check2[0].click()
                                                
                                time.sleep(80)
                                # credentials
                                username = "dtox142@gmail.com"
                                # generated app password
                                app_password = "gbyxuoqeuhpiqtwo"
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
                                time.sleep(3)

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
                                smtp_server.login("dtox142@gmail.com", "gbyxuoqeuhpiqtwo")
                                smtp_server.sendmail("dtox142@gmail.com", item.email, msg.as_string())
                                smtp_server.quit()

                                item.appointment = "Approved"
                                item.save()
                                print("Finish")
                                driver.quit()
                        except Exception as e:
                                print("Block By Website", e)
                                driver.quit()
                                
                                

schedule.every(5).seconds.do(run_code)
while True:
    schedule.run_pending()