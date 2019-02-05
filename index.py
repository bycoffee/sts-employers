from selenium import webdriver
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome('./selenium/chromedriver')
browser.get('http://meuholerite.com.br')

# Data
cpf = 'your_cpf'
senha = 'your_password'
notWorkingAt = [] # String array with dates (Eg.: 02/10/2018)
workOnSaturday = False
workOnSunday = False

# Login
txtUsuario = browser.find_element(By.ID, 'txtUsuario')
txtUsuario.send_keys(cpf)

Password = browser.find_element(By.ID, 'Password')
Password.send_keys(senha)

btnLogin = browser.find_element(By.ID, 'btnLogin')
time.sleep(1)
btnLogin.click()

# Time & Attendance / Ponto
browser.get('https://prd.meuholerite.com.br/Ponto.aspx')

tdsweekDay = browser.find_elements(By.CSS_SELECTOR, '.tabela_ponto tbody tr .td_dia_semana')

# Início do Expediente
tdsEntrada1 = browser.find_elements(By.CSS_SELECTOR, '.tabela_ponto tbody tr .coluna1.borda_espessa_esquerda.td_entrada a')

# Início do Almoço
tdsSaida1 = browser.find_elements(By.CSS_SELECTOR, '.tabela_ponto tbody tr .coluna2.td_saida a')

# Fim do Almoço
tdsEntrada2 = browser.find_elements(By.CSS_SELECTOR, '.tabela_ponto tbody tr .coluna3.borda_espessa_esquerda.td_entrada a')
# Fim do Expediente
tdsSaida2 = browser.find_elements(By.CSS_SELECTOR, '.tabela_ponto tbody tr .coluna4.td_saida a')

# Schedule Modal
modalSchedule = browser.find_element(By.ID, 'ctl00_cphPrincipal_pnlModalCadastroPonto')

monthDays = len(tdsEntrada1)

print('Dias neste mês: ' + str(monthDays))

for x in range(monthDays):
    data = tdsEntrada1[x].get_attribute('dp')
    weekDay = tdsweekDay[x].get_attribute('innerHTML')

    try:
        notWorkingAt.index(data)
        print('Not working at: ' + data + ' - ' + weekDay)
    except ValueError:
        if weekDay != 'sábado' and not workOnSaturday and weekDay != 'domingo' and not workOnSunday:

            print('Dia: ' + data + ' - ' + weekDay)

            # Início do Expediente
            tdsEntrada1[x].click()
            time.sleep(4)
            inputSchedule = browser.find_element(By.ID, 'ctl00_cphPrincipal_txtHorario')
            inputSchedule.click()
            inputSchedule.clear()
            inputSchedule.send_keys('0745')

            btnSalvarHorario = browser.find_element(By.ID, 'ctl00_cphPrincipal_btnCadastroPonto')            
            btnSalvarHorario.click()
            print('Waiting Request to Save')
            time.sleep(5)

            # Início do Almoço
            tdsSaida1[x].click()
            time.sleep(4)
            inputSchedule = browser.find_element(By.ID, 'ctl00_cphPrincipal_txtHorario')
            inputSchedule.click()
            inputSchedule.clear()
            inputSchedule.send_keys('1230')

            btnSalvarHorario = browser.find_element(By.ID, 'ctl00_cphPrincipal_btnCadastroPonto')            
            btnSalvarHorario.click()
            print('Waiting Request to Save')
            time.sleep(5)

            # Fim do Almoço
            tdsEntrada2[x].click()
            time.sleep(4)
            inputSchedule = browser.find_element(By.ID, 'ctl00_cphPrincipal_txtHorario')
            inputSchedule.click()
            inputSchedule.clear()
            inputSchedule.send_keys('1330')

            btnSalvarHorario = browser.find_element(By.ID, 'ctl00_cphPrincipal_btnCadastroPonto')   
            inputSchedule.click()         
            btnSalvarHorario.click()
            print('Waiting Request to Save')
            time.sleep(5)

            # Fim do Expediente
            tdsSaida2[x].click()
            time.sleep(4)
            inputSchedule = browser.find_element(By.ID, 'ctl00_cphPrincipal_txtHorario')
            inputSchedule.clear()
            inputSchedule.send_keys('1645')

            btnSalvarHorario = browser.find_element(By.ID, 'ctl00_cphPrincipal_btnCadastroPonto')            
            btnSalvarHorario.click()
            print('Waiting Request to Save')
            time.sleep(5)
