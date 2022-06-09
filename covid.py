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

        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdU3SvhuMTIx4rbSHoLLoZ8PmVcMMse2LdCbVgLsNB9Z8r4vQ/viewform')

        login_attempt = driver.find_element_by_xpath("//*[@id='SMMuxb']/a[1]")
        login_attempt.click()
        driver.switch_to.window(driver.window_handles[1])
        campo_login = driver.find_element_by_xpath("//*[@id='identifierId']")
        campo_login.send_keys("csi1@grupogema.com.co")
        campo_login.send_keys(Keys.RETURN)
        time.sleep(3)
        campo_clave = driver.find_element_by_name("password")
        campo_clave.send_keys("GG%2021abc")
        campo_clave.send_keys(Keys.RETURN) 
        time.sleep(2)
        nombre = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        nombre.send_keys("William Acosta Mosquera")
        nombre.send_keys(Keys.RETURN) 
        documento = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        documento.send_keys("1014302619")
        documento.send_keys(Keys.RETURN)
        cargo = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        cargo.send_keys("webmaster")
        documento.send_keys(Keys.RETURN)
        ciudad = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
        ciudad.send_keys("Bogota")
        documento.send_keys(Keys.RETURN)
        fecha = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        fecha1 = datetime.datetime.now()
        fecha.send_keys(f"{fecha1.day}-{fecha1.month}-{fecha1.year}")
        documento.send_keys(Keys.RETURN)
        eps = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        eps.send_keys("Compensar")
        eps.send_keys(Keys.RETURN)
        p1 = driver.find_element_by_xpath('//*[@id="i33"]/div[3]/div')
        p1.click()
        p2 = driver.find_element_by_xpath('//*[@id="i43"]/div[3]/div')
        p2.click()
        p3 = driver.find_element_by_xpath('//*[@id="i53"]/div[3]/div')
        p3.click()
        p4 = driver.find_element_by_xpath('//*[@id="i63"]/div[3]/div')
        p4.click()
        p5 = driver.find_element_by_xpath('//*[@id="i73"]/div[3]/div')
        p5.click()
        p6 = driver.find_element_by_xpath('//*[@id="i83"]/div[3]/div')
        p6.click()
        p7 = driver.find_element_by_xpath('//*[@id="i93"]/div[3]/div')
        p7.click()
        p8 = driver.find_element_by_xpath('//*[@id="i103"]/div[3]/div')
        p8.click()
        p9 = driver.find_element_by_xpath('//*[@id="i113"]/div[3]/div')
        p9.click()
        p10 = driver.find_element_by_xpath('//*[@id="i123"]/div[3]/div')
        p10.click()
        p10_1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div[1]/div/div[1]/input')
        p10_1.send_keys("N/A")
        p10_1.send_keys(Keys.RETURN)
        p11 = driver.find_element_by_xpath('//*[@id="i137"]/div[3]/div')
        p11.click()
        p12 = driver.find_element_by_xpath('//*[@id="i147"]/div[3]/div')
        p12.click()
        p12_1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div[1]/div/div[1]/input')
        p12_1.send_keys("N/A")
        p12_1.send_keys(Keys.RETURN)
        p13 = driver.find_element_by_xpath('//*[@id="i161"]/div[3]/div')
        p13.click()
        p13_1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/div[1]/div/div[1]/input')
        p13_1.send_keys("N/A")
        p13_1.send_keys(Keys.RETURN)
        p14 = driver.find_element_by_xpath('//*[@id="i175"]/div[3]/div')
        p14.click()
        p14_1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[24]/div/div/div[2]/div/div[1]/div/div[1]/input')
        p14_1.send_keys("N/A")
        p14_1.send_keys(Keys.RETURN)
        p15 = driver.find_element_by_xpath('//*[@id="i189"]/div[3]/div')
        p15.click()
        p15_1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[26]/div/div/div[2]/div/div[1]/div[2]/textarea')
        p15_1.send_keys("N/A")
        p15_1.send_keys(Keys.RETURN)
        p15 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        p15.click()
i = 1
while i < 6:
  times = datetime.datetime.now()
  time1 = times.hour 
  minutos = times.minute
  respuesta = WebDriver() 
  if time1 == 8:
      if minutos ==  7:
        respuesta.pagina()      
        while minutos == 7:
            time.sleep(60)
            break
            
