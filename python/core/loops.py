# FOR LOOP
print("começando for")

clientes = ["Bruno", "Lucas", "Samuel"]

for j in clientes: # for: aplica uma função a cada termo de uma lista, separadamente
    print(j)       # j =  variável temporária, só existe dentro do for

for i in range(2, 10, 2): # range: cria uma lista de números naturais a partir do 2 até 10 (sem incluir 10), dois a dois
    print(i)
    print("Rodando for") # Vai rodar 5 vezes

print("Fora do for") # vai rodar 1 vez

print(range(20) == range(0, 20, 1)) # range(x) = começa do zero, de um a um até 20

# WHILE LOOP: roda enquanto a expressão for verdade
print("começando while")

i = 0
while i < 6:
    i = i+1 # 1, 2, 3, 4
    if i != 5:
        print(i)
        continue # continue: volta ao topo do loop
        print("fui pulado")
    else: 
        print("parou no 5")
        break # break: finaliza o loop
