import time, sys
from multiprocessing import Process,Queue,Pipe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


##############################################################################
#descargar archivo de Bancop
# def bot(Intermediary):
def bot(cedula, pword, ruc, option, fechain, fechafin, Intermediary):

    # ################
    #      BORRAR AL TERMINAR DE HACER TESTING, ESCENCIAL
    cedula = '2124028'
    pword = 'Verti2011'
    ruc = '80101558-8'
    option = 'sms'

    ################

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

############################################################
#TESTING
    #input para el 2fa
    while (Intermediary.getflag()):
        pass

    twofa = Intermediary.get2fa()
    print(twofa)
    exit(code=1)
###########################################################



    if option == 'email':
        Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CLASS_NAME,'text-option-send-email')))
        Esperar.click()
    else:
        Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.XPATH,"//label[@for ='sms']")))
        Esperar.click()

    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,"buttonCanalSend")))
    Esperar.click()

    #input para el 2fa
    while (Intermediary.getflag()):
        pass

    twofa = Intermediary.get2fa()
    print(twofa)
    exit(code=1)

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
    driver.quit()

if __name__ == "__main__":
    try:
        ruc = sys.argv[1]
        cedula = sys.argv[2]
        pword = sys.argv[3]
        option = sys.argv[4]
        fromd = sys.argv[5]
        to = sys.argv[6]
    except IndexError:
        ruc = None
        cedula = None
        pword = None
        option = None
        fromd = None
        to = None

    bot(cedula, pword, ruc, option, fromd, to)
    # bot2(fromd, to)
    # mover.move(fromd, to)
