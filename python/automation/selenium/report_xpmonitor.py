from selenium import webdriver
import pandas as pd
from time import sleep

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/perfil-pessoas-fisicas/faixa-etaria/")

html = driver.find_element_by_class_name('primary-text').click()
        
sleep(3)
    

    
df = pd.read_html(html)[0]

print(df)

driver.quit()
