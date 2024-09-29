import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do WebDriver
driver = webdriver.Chrome()

# Abrir o site com o formulário
driver.get("https://servicos.receita.fazenda.gov.br/Servicos/CPF/InscricaoPublica/inscricao.asp")

# Espera carregar o elemento
elemento = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'txtNascimento'))
)

# Selecionar o campo "dia" e escolher um valor
day_select = driver.find_element(By.ID, 'txtNascimento')
day_select.send_keys('25/12/2025')  # Seleciona o dia 25/12/2025

time.sleep(10)

# Fechar o driver após completar as ações
driver.quit()
