#FUNÇÃO: realiza determinada operação quando chamada

def somar(x, y): #def: define uma função e seus parâmetros (temporários, só existem dentro dela)
    return(x+y) #return: faz com que a função gere em um resultado manipulável. Só existe dentro da função, e faz ela terminar nesse ponto

x = 5
y = 6

print(somar(x,y))

z = somar(10,5) #funções podem ser tratadas como variáveis 
print(z+y)

#MÓDULOS: códigos já existentes que possuem funções novas

import math #importa o código

x = 16
raiz_quadrada = math.sqrt(x) #acessa a função dentro da biblioteca que já foi importada


from math import sqrt #importa a função que pode ser usada como se estivesse no seu código
print(sqrt(x))

from math import sqrt as raiz_quadrada #importa a função e muda seu nome, sendo usada como se fosse sua também