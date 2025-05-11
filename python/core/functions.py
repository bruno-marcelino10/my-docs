# FUNÇÃO: realiza determinada operação quando chamada

def somar(x, y): #def: define uma função e seus parâmetros (temporários, só existem dentro dela)
    return(x+y) # return: faz com que a função gere em um resultado manipulável. Só existe dentro da função, e faz ela terminar nesse ponto

x = 5
y = 6

print(somar(x,y))

z = somar(10,5) #funções podem ser tratadas como variáveis 
print(z+y)

# lambda

# São funções que o usuário não precisa definir previamente para utilizar. 
# Funcionam bem em casos que a função pode ser descrita em uma linha. 
# São descritas como "funções anônimas", ou seja, funções não identificada, sem um “nome”, no caso, não há uma forma de se referir a elas.
# A sua maior utilidade se deve como forma de aplicar uma mesma função de forma vetorizada (iterando em uma lista, por exemplo), como argumento para a função `map()`. 

# Exemplo 1:
print("passando argumentos", (lambda x, y: x**y)(3, 2))

# Exemplo 2:
potencia = lambda x, y: x**y
print("definindo e passando argumentos", potencia(3, 2))

# Exemplo 3:
funcao_soma = (lambda *args: sum(args))
print("passando argumentos indefinidos", funcao_soma(1, 2, 3, 4, 5))

# Exemplo 4:
precos = [5, 4, 3, 2, 1]
print("usando map", list(map(lambda x: x**2, precos)))

# Exemplo 5:
lista = [5, 4, 3, 2, 1]
print("usando filter", list(filter(lambda x: x % 2 != 0, lista)))
