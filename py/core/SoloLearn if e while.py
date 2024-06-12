1 == 1 # testa se isso ocorre

1 != 1 #diferente

1 >= 3 #testa comparação (maior ou igual)

#IF: se for verdade, a expressão continua. Se não, a expressão termina nesse ponto
x = 4
if x >= 5:
    print(x + 10)
elif x == 4:
    print(x**2)
else: 
    print(x)


1 == 1 and 2 == 2 #and: as duas condições devem ser obedecidas
1 == 1 or 2 == 2 #or: pelo menos uma das condições devem ser obedecidas
not (1 == 1 or 2 == 2) #not: inverte o argumento (not true = false)

#WHILE: roda enquanto a expressão for verdade (loop)
i = 1
while i <= 3:
    print(i)
    i = i + 1

#continue: volta ao topo do loop


