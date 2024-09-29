from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

opcoes = Options()
opcoes.add_argument("--headless=old")
opcoes.add_argument("--disable-gpu")
#não mostrar blank page
opcoes.add_argument("--window-position=-2400,-2400")

driver = webdriver.Chrome(options=opcoes)

# Abrir o site com o formulário
driver.get("https://servicos.receita.fazenda.gov.br/Servicos/CPF/InscricaoPublica/inscricao.asp")


# Espera carregar o elemento
elemento = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'txtNascimento'))
)

# Selecionar o campo "dia" e escolher um valor
day_select = driver.find_element(By.ID, 'txtNascimento')
day_select.send_keys('25/12/2025')  # Seleciona o dia 25/12/2025
print(driver.page_source)

# Fechar o driver após completar as ações
driver.quit()
