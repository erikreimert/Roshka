import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user = 'erikreimert'
pword = 'Alemania1968$'

browser = webdriver.Chrome()
browser.get(('https://github.com/login'))

#TODO
username = browser.find_element_by_id('login_field')
username.send_keys(user)
username = browser.find_element_by_id('password')
username.send_keys(pword)
nextButton = browser.find_element_by_name('commit')
nextButton.click()

Esperar = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,"//span[@title='Machine-Learning']")))
Esperar.click()

Esperar = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH,"//summary[@class='btn  ml-2 btn-primary']")))
Esperar.click()

descargar = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.LINK_TEXT,'Download ZIP')))
descargar.click()

time.sleep(15)

os.system('python mover.py')
