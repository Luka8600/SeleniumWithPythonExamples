from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()



#Apro la pagina di google maps

driver.get("https://www.google.it/maps/@39.7418569,9.1111372,15z")

AcceptCondition = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span' )
AcceptCondition.click()

sleep(5)

def ricercaLuogo () :
        Luogo = driver.find_element(By.ID,'searchboxinput')
        Luogo.send_keys('Nurallao')
        Submit = driver.find_element(By.ID,'searchbox-searchbutton')
        Submit.click()

ricercaLuogo()

def IndicazioniStradali():
     sleep(10)
     IndStradali = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/div[1]')
     IndStradali.click()

IndicazioniStradali()

def SceltaPuntoInizio ():
    sleep(10)
    PuntoInizio = driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
    PuntoInizio.send_keys('Isili')
    sleep(10)
    Cerca = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]')
    Cerca.click()


SceltaPuntoInizio()


def numeroKm ():
    sleep(3)
    TotaleKmAuto = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div')
    print("KM Totali in Auto :", TotaleKmAuto.text)


numeroKm()


def RicercaBenzinai() :
    sleep(3)
    ListBenzinai = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div/button/span[1]')
    ListBenzinai.click()

RicercaBenzinai()

