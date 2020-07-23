import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
##############################################################################
#descargar archivo de Bancop
# def bot(Intermediary):
def bot(cedula, pword, ruc, option, fechain, fechafin):



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
    username.send_keys(cedula)
    username = browser.find_element_by_id('password')
    username.send_keys(pword)
    nextButton = browser.find_element_by_id('button-login')
    nextButton.click()

    if option == 'email':
        Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CLASS_NAME,'text-option-send-email')))
        Esperar.click()
    else:
        Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,"//label[@for ='sms']")))
        Esperar.click()

    exit(code=1)
    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,"buttonCanalSend")))
    Esperar.click()

    #input para el 2fa
    while (False == os.path.isfile('./2fa.txt')):
        pass
    time.sleep(.01)
    file = open('2fa.txt', 'r')
    twofa = file.read()
    file.close()

    username = browser.find_element_by_id('token')
    username.send_keys(twofa)
    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,"//div[@class = 'col-xs-12 col-sm-12 button-access style-button-access']/button[@class = 'button-white']")))
    Esperar.click()

############################################################################
####Esperar a que la pagina cargue y despues entrar a pagina para descarga
    Esperar = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID,'accountPage')))
    Esperar.click()

    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.LINK_TEXT,'Movimientos')))
    Esperar.click()

    #TODO Este es el que falla
    time.sleep(1)
    descargar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,"//form[@id='form-movement-account']/div[@class = 'radio col-md-12 col-sm-12 col-xs-12'/label[@for='041014092']")))
    descargar.click()

    descargar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,'dataMovementAccountSelected')))
    descargar.click()

    descargar = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='icon-download']")))
    descargar.click()

    bot2(fechain, fechafin)
    mover.move(fechain, fechafin)
###########################################################################


#descargar archivo de brosco
def bot2(fromd, to):
    link = 'https://iapi.brosco.com.py/brosco-api/aurora/conciliation/list/export?from=' + fromd + '&to=' + to + '&affiliateId=EDUC'
    # link1 = 'https://phoebe.roshka.com.py/brosco-api/aurora-api/conciliation/list/export?from=2020-06-25&to=2020-06-30&affiliateId=EDUC'
    browser = webdriver.Chrome()
    browser.get((link))

    #TIEMPO DE ESPERA PARA QUE SE DESCARGUE EL ARCHIVO DE BANCOP Y BROSCO, INCREMENTAR SI FALTA TIEMPO
    time.sleep(120)
    browser.quit()
