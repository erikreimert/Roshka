import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def bot(useri, pwordi, ruci):
    user = useri
    pword = pwordi
    ruc = ruci

    browser = webdriver.Chrome()
    browser.get(('https://www.bancop.com.py:8443/bancop/login'))


    # nextButton = browser.find_element_by_id('title-selec-login')
    # nextButton.click()
    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,'title-second-login')))
    Esperar.click()

    time.sleep(1)
    ##Log in Portion
    username = browser.find_element_by_id('numberRuc')
    username.send_keys(ruc)
    username = browser.find_element_by_id('userName')
    username.send_keys(user)
    username = browser.find_element_by_id('password')
    username.send_keys(pword)
    nextButton = browser.find_element_by_id('button-login')
    nextButton.click()

#TIEMPO DE ESPERA PARA CONFIRMACION DE TELEFONO, INCREMENTAR SI FALTA MAS
    time.sleep(30)

    # Esperar = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='icon-close-white']")))
    # Esperar.click()

    ##Esperar a que la pagina cargue y despues entrar a pagina para descarga
    Esperar = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID,'accountPage')))
    Esperar.click()

    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.LINK_TEXT,'Movimientos')))
    Esperar.click()

    descargar = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@value='0410140929']")))
    descargar.click()

    descargar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,'dataMovementAccountSelected')))
    descargar.click()

    descargar = WebDriverWait(browser, 80).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='icon-download']")))
    descargar.click()


    time.sleep(50)



if __name__ == "__main__":
    ruc = input("Ingresar RUC: \n")
    user = input("Ingresar Cedula: \n")
    pword = input("Ingresar password: \n")

    bot(user, pword, ruc)

    os.system('python mover.py')
