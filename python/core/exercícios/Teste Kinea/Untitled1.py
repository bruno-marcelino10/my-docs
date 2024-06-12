#!/usr/bin/env python
# coding: utf-8

# In[2]:


continuar = True
jogadores = []

while continuar:
    jogador = str(input("Digite um Jogador: "))
    jogadores.append(jogador)
    
    fechar = str(input("Deseja continuar? (s/n)"))
    if fechar == "n":
        continuar = False

print("")
print("Os jogadores cadastrados são:", jogadores)

