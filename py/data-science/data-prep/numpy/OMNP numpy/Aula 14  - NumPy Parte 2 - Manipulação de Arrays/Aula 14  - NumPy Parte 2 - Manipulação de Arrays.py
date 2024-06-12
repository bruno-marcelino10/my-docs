#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


# Outros formas de manipulaçao de arrays

print("Numeros inteiros aleatorios")

int_numbers = np.random.randint(1, 200, size=50)
int_numbers


# In[ ]:


# Ordenado um array

int_numbers.sort()

int_numbers


# In[ ]:


# Selecionando elementos de um array com base no indice

# Primeiros 10 elementos

int_numbers[:10]


# In[ ]:


# Tudo o que vem depois dos 15 primeiros elementos

int_numbers[15:]


# In[ ]:


int_numbers[15:20]


# In[ ]:


# Selecionando os elementos de 2 em 2

int_numbers[::4]


# In[ ]:


# Sort decrescente

int_numbers[::-1]


# In[ ]:


int_numbers


# In[ ]:


# Selecionando os elementos de 2 em 2, começando do indice 5

int_numbers[5::2]


# In[ ]:


int_numbers


# In[ ]:


np.cumsum(int_numbers)


# In[ ]:


# Mas para o que serve mesmo tudo isso?

# Vamos calcular a media movel de uma sequencia de precos

def media_movel(seu_array, n = 5):
    valores = np.cumsum(seu_array, dtype=float)
    valores[n:] = valores[n:] - valores[:-n]
    return valores[n - 1:] / n


# In[ ]:


# Simulando um array de precos

precos = np.random.uniform(10,10000, size=100).round(2)

precos


# In[ ]:


# Ajustando o array
precos.sort()

precos


# In[ ]:


# Escolhendo o periodo da média movel

p = 8


# In[ ]:


mm = media_movel(precos, n = p).round(2)

mm


# In[ ]:


# Vamos ver no grafico

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# In[ ]:


plt.plot(precos, label = "Precos")
plt.plot(range(p ,p +len(mm)),mm, label = 'Media Movel')


# In[ ]:


range(p ,p +len(mm))


# In[ ]:


plt.plot(range(p ,p + len(mm)), mm, label = 'Media Movel')
plt.plot(precos, label = "Precos")
plt.title('Media Mòvel de 5 periodos da série simulada')
plt.xlabel("Periodo")
plt.ylabel("Preço");
plt.grid()
plt.legend()


# In[ ]:


# Concatenando arrays

a1 = np.array([10, 20, 30, 40])
a2 = np.array([7, 8, 9, 10])
a3 = np.array([1, 2, 3, 4])

a4 = np.concatenate([a1, a3, a2])

a4


# In[ ]:


# Concatenando arrays multidimensionais (as matrizes)

m1 = np.array([[10, 20], [30, 40]])
m2 = np.array([[7, 8], [9, 10]])
m3 = np.array([[1, 2], [3, 4]])

np.concatenate([m1, m2, m3])


# In[ ]:


# E também fazer a concatenaçao por linha

np.concatenate([m1, m2, m3], axis = 1)


# In[ ]:


# Adicionar e remover elementos

lista_produtos = np.array(["Notebook","Microfone","Game"])

lista_produtos


# In[ ]:


# Append adiciona um novo item sempre no final do array

lista_produtos = np.append(lista_produtos, "Livro")

lista_produtos


# In[ ]:


# Insert adiciona um novo item na posicao desejada

lista_produtos = np.insert(lista_produtos,1,"Celular")

lista_produtos


# In[ ]:


# Remover um elemento

lista_produtos = np.delete(lista_produtos,[0]) 

lista_produtos

