#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Input
lista = [5,2,4,3,1]

#Script
for i in range(1, len(lista)):

    # subconjunto com valores anteriores a i
    sub = lista[:i]
    maiores_que_i = list() 
        
    # separa os valores maiores que i    
    for j in sub:
        if j > lista[i]:
                maiores_que_i.append(j)
        
    # caso o elemento i seja maior que todos os anteriores
    if len(maiores_que_i) > 0:
        # acrescenta i no lugar do menor valor ENTRE os que são maiores que i, movendo os próximos para a frente 

        menor_valor = min(maiores_que_i)
        pos_menor_valor = lista.index(menor_valor)
        lista.insert(pos_menor_valor, lista[i])
        
        # apagar o elemento (i) remanescente na posição antiga
        lista.pop(i+1)
        
    print("situação atual da lista: ", lista)


# In[ ]:




