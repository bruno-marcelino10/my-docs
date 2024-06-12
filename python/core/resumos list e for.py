#LIST

clientes = ["Joao", "Pedro", "Marcelo"] #list: concatena os elementos em ordem
print(clientes)

print(clientes[0]) #seleciona o elemento de índice 0 (índices variam em 0,1,2,3,...)

clientes.append("Rafael") #append: acrescenta um elemento no final da lista. O ponto mostra que a função se refere a uma lista
print(clientes)

print(len(clientes)) #len: mostra a quantidade de elementos numa lista

clientes.insert(2, "Milton") #acrescenta um termo em um determinado índice

clientes.remove("Marcelo") #remove: remove o termo especificado 
print(clientes)

print(clientes.index("Milton")) #index: mostra o índice onde está o elemento

#FOR

for j in clientes: #for: aplica uma função a cada termo de uma lista, separadamente
    print(j)       #j =  variável temporária, só existe dentro do for

for i in range(2, 10, 2): #range: cria uma lista de números naturais a partir do 2 até 10 (sem incluir 10), dois a dois
    print(i)
    print("Rodando for") # Vai rodar 5 vezes

print("Fora do for") #Vai rodar 1 vezes

print(range(20) == range(0, 20, 1)) #range(x) = começa do zero, de um a um até 20