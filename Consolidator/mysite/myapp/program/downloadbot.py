import time, os, glob
from . import folders, mover
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
##############################################################################
#descargar archivo de Bancop
def bot(cedula, pword, ruc, option, fechain, fechafin, corporativa):

    #Run headless
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Chrome(service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    # browser = webdriver.Chrome()

    actions = ActionChains(browser)

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

    Esperar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,"buttonCanalSend")))
    Esperar.click()

    #input para el 2fa
    while (False == os.path.isfile('./2fa.txt')):
        pass
    time.sleep(.1)
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

    time.sleep(1)
    descargar = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID,"modalMovementAccount")))
    actions.send_keys("\t\t\t\t\t\t\t\t\t\t \t ").perform()

    descargar = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='icon-download']")))
    descargar.click()

    bot2(fechain, fechafin, corporativa)
    mover.move(fechain, fechafin, corporativa)
###########################################################################

def count(xls):
    i = 0
    for file in xls:
        i+=1
    return i
#descargar archivo de brosco
def bot2(fromd, to, corporativa):
    link = 'https://iapi.brosco.com.py/brosco-api/aurora-api/conciliation/list/export?from='+ fromd + '&to='+ to +'&affiliateId=' + corporativa
    #Run headless
    display = Display(visible=0, size=(1024, 768))
    display.start()
    browser = webdriver.Chrome(service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    # browser = webdriver.Chrome()
    browser.get(link)
    #Esperar a que los dos archivos existan en la carpeta de descarga
    xlsP =  glob.iglob(os.path.join(folders.dl, "*.xls"))
    xlsxP =  glob.iglob(os.path.join(folders.dl, "*.xlsx"))
    xls = count(xlsP)
    xlsx = count(xlsxP)
    while(xls < 1 ) and (xlsx < 1):
        xlsP =  glob.iglob(os.path.join(folders.dl, "*.xls"))
        xlsxP =  glob.iglob(os.path.join(folders.dl, "*.xlsx"))
        xls = count(xlsP)
        xlsx = count(xlsxP)
        pass
    browser.quit()
