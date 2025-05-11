# LISTS

clientes = [1, 2, 3, 5, 6] # uma lista concatena os elementos em ordem
print("lista original", clientes)

# Indexação
print("primeiro elemento", clientes[0]) # []: seleciona o elemento de índice 0 (índices variam em 0,1,2,3,...)

# Operações com a lista 
print("tamanho", len(clientes)) # len: mostra a quantidade de elementos numa lista
print("somatório", sum(clientes)) # sum: soma os elementos da lista

# Métodos da lista
clientes.append(4) # append: acrescenta um elemento no final da lista. O ponto mostra que a função se refere a uma lista
print("adicionando 4", clientes)

clientes.remove(2) # remove: remove o termo especificado 
print("removendo 2", clientes)

clientes.insert(2, 10) # insert: acrescenta um termo em um determinado índice
print("inserindo 10", clientes)

print("indice do 10", clientes.index(10)) # index: mostra o índice onde está o elemento

# Funções mais avançadas

print("estado da lista", clientes)

def soma(x): return x+50
print("usando map", list(map(soma, clientes))) # map: aplica uma função a todos os elementos da lista

def filtro(x): 
    if x > 5:
        return True
    else:
        return False

print("usando filter", list(filter(filtro, clientes))) # filter: aplica uma regra de filtragem a todos os elementos da lista

from functools import reduce
def somatorio(x, y): return x+y
print("usando reduce", reduce(somatorio, clientes)) # reduce: reduz a lista a um unico valor