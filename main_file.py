from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time
import docx
import eel

eel.init("web")
@eel.expose
def send_status():
    print("begin")
    with open("passw.txt", "r") as file:
     doc = docx.Document()
    doc.add_heading('Статусы')
    for item in file:
        
        p_list = item.split()
        print("L: "+ p_list[0]+" P: "+p_list[1])
        options_of_driver = webdriver.ChromeOptions()
        options_of_driver.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options_of_driver)
        driver.get("https://портал-тп.рф/platform/portal/tehprisEE_profileMyMsg")
        wait1 = WebDriverWait(driver, 2)
        #driver.set_window_size(1920, 1080)
        email_int = driver.find_element(By.ID, "workplaceTopForm:j_mail_login")
        email_int.clear()
        email_int.send_keys(p_list[0])
        passw_int = driver.find_element(By.ID, "workplaceTopForm:j_password")
        passw_int.clear()
        passw_int.send_keys(p_list[1])
        driver.find_element(By.ID, "workplaceTopForm:loginBtn").click()
        time.sleep(5) # Даем время на загрузку сайта
      #Окончание входа

      #Считывание данных
        status = driver.find_element(By.CLASS_NAME,"answer-status-in-list").text
        status_num = driver.find_element(By.CLASS_NAME,"item-message__next-id").text
        fio = driver.find_element(By.ID, "workplaceForm:fioLabel").text
        date = driver.find_element(By.CLASS_NAME,"item-message__option-value").text
        status_itog = "<p>"+fio +" "+ status_num +" "+date +" "+ status+ "</p>"
        print(status_itog)        
        stat_in_doc = doc.add_paragraph(fio +" "+ status_num +" "+date +" "+ status)
        driver.quit()
        doc.save("output.docx") 
        return status_itog
eel.start("index.html", size = (200,300))
