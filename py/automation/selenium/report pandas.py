import pandas as pd 

url = "https://sistemaswebb3-listados.b3.com.br/investorProfilePage/range?language=pt-br"
pd.read_html(url)[0]