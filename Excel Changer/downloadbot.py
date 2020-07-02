import time, os, mover
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#descargar archivo de Bancop
def bot(user, pword, ruc):

    #init el driver y chrome
    browser = webdriver.Chrome()
    browser.get(('https://www.bancop.com.py:8443/bancop/login'))


    #cambia a pagina de Enterprise
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

############################################################################
####Esperar a que la pagina cargue y despues entrar a pagina para descarga
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
############################################################################

#descargar archivo de broscop
def bot2():

    browser = webdriver.Chrome()
    browser.get((''))

    #TIEMPO DE ESPERA PARA QUE SE DESCARGUE EL ARCHIVO DE BANCOP Y BROSCO, INCREMENTAR SI FALTA TIEMPO
    time.sleep(50)


if __name__ == "__main__":
    ruc = input("Ingresar RUC: \n")
    user = input("Ingresar Cedula: \n")
    pword = input("Ingresar password: \n")
    # ruc =
    # user =
    # pword =


    bot(user, pword, ruc)
    bot2()
    os.system('python my_file.py')
