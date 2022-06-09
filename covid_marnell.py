from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

class WebDriver():

    def pagina(self):
        opciones = webdriver.ChromeOptions()
        opciones.add_argument('--star-maximized')
        opciones.add_argument('--disable-extensions')

        driver_path = '/usr/bin/chromedriver'
        driver = webdriver.Chrome(driver_path, chrome_options=opciones)

        driver.set_window_position(2000, 0)
        driver.maximize_window()

        time.sleep(1)

        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfXpJ_OFw01ua-UEjO6YdtObCMAFf9IDbAWYmedVj3i8Ej3Rg/viewform')

        login_attempt = driver.find_element_by_xpath("//*[@id='SMMuxb']/a[1]")
        login_attempt.click()
        driver.switch_to.window(driver.window_handles[1])
        campo_login = driver.find_element_by_xpath("//*[@id='identifierId']")
        campo_login.send_keys("csi1@grupogema.com.co")
        campo_login.send_keys(Keys.RETURN)
        time.sleep(2)
        campo_clave = driver.find_element_by_name("password")
        campo_clave.send_keys("Enero*2022")
        campo_clave.send_keys(Keys.RETURN) 
        time.sleep(2)
        p1 = driver.find_element_by_xpath('//*[@id="i7"]/div[3]/div')
        p1.click()
        fecha = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fecha1 = datetime.datetime.now()
        fecha.send_keys(f"{fecha1.day}-{fecha1.month}-{fecha1.year}")
        ciudad = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ciudad.send_keys("Bogota")
        ciudad.send_keys(Keys.RETURN)
        nombre = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        nombre.send_keys("William De Jesus Acosta Mosquera")
        nombre.send_keys(Keys.RETURN)
        documento = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        documento.send_keys("1014302619")
        documento.send_keys(Keys.RETURN)
        p2 = driver.find_element_by_xpath('//*[@id="i37"]/div[3]/div')
        p2.click()
        telefono = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
        telefono.send_keys("3324356811")
        telefono.send_keys(Keys.RETURN) 
        p3 = driver.find_element_by_xpath('//*[@id="i48"]/div[3]/div')
        p3.click()
        p3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        p3.click()    
            
        

i = 1
while i < 6:
    times = datetime.datetime.now()
    time1 = times.hour 
    minutos = times.minute
    respuesta = WebDriver() 
    if time1 == 8:
       if minutos ==  0:
         respuesta.pagina()      
         while minutos == 0:
             time.sleep(60)
             break
            
