# MÓDULOS: outros códigos python já existentes que possuem funções novas

# import 
import math #importa o código

x = 16
print("import normal", math.sqrt(x)) # acessa a função dentro da biblioteca que já foi importada

# from
from math import sqrt # importa a função que pode ser usada como se estivesse no seu código
print("usando from", sqrt(x))

# from as
from math import sqrt as raiz_quad # importa a função e muda seu nome, sendo usada como se fosse sua também
print("usando from as", raiz_quad(4))
