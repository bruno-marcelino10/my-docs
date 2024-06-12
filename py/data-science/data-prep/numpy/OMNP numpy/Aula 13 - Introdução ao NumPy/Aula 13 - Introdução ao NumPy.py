#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando a bibliteca

import numpy as np


# In[2]:


from numpy import doc

help(doc)


# In[3]:


help(np.doc.indexing)


# In[4]:


list(range(1,10))


# In[5]:


# Criando um array

v1 = np.array(list(range(1,10)))

v1


# In[6]:


# Um array é mais poderoso do que imaginamos
v2 = np.array([100,list(range(1,10))])

v2


# In[7]:


# Com muitos modos de acessar os seus elementos

print(v2[0])
print(v2[1])
print(v2[1][2])


# In[8]:


# E mudar a sua forma

print(np.vstack(v2[1]))

print(np.hstack(v2[1]))


# In[9]:


v1


# In[12]:


v1.reshape(3,3)


# In[14]:


v3 = np.array(list(range(1,11)))

v3


# In[15]:


v3.reshape(2,5)


# In[16]:


v3.reshape(5,2)


# In[17]:


# Tipos de dados
# Lembre-se que uma matriz também é chamada de array multidimensional
m1 = np.array([(1.5,2,3), (4,5,6), (3,2,1), (4,5,6)])

m1


# In[18]:


# Tipos de dados - devem ser definidos, se preciso, no momento da criacao do array

m2 = np.array([(1.5,2,3), (4,5,6), (3,2,1), (4,5,6)], dtype = int)

m2


# In[22]:


# Criando arrays predefinidos

print("Array preenchido com zeros")
print(np.zeros(15, dtype = int))
print()
print("Array preenchido com 1")
print(np.ones(5))
print()
print("Matriz 5x5 preenchida com 1")
print(np.ones((5,5)))
print()
print("Matriz ou vetor com numeros iguais")
print(np.full((3,2), 42))
print()
print("Matriz identidade")
print(np.eye(5,5))
print()
print("Arrays sequenciais - com a sequencia definida por voce")
print(np.arange(100,122,2))
print()
print("Ou com a sequencia definida pelo NumPy")
print(np.linspace(0,10,5)) 


# In[25]:


# Criando arrays com numeros aleatorios

print("Matriz com numeros aleatorios entre 0 e 1")
print(np.random.random((2,2)))
print()
print("Numeros inteiros aleatorios")
print(np.random.randint(1, 60, size=6))
print()
print("Numero aleatorio da distribuicao normal")
print(np.random.normal())
print()
print("Numeros aleatorios da distribuicao normal")
print(np.random.randn(3))
print()
print("Numero aleatorio da distribuicao uniforme")
print(np.random.uniform())
print()
print("Numeros aleatorios da distribuicao uniforme")
print(np.random.uniform(size=5))
print()
print("Lembre-se que voce pode criar matrizes de numeros aleatorios da distribuicao normal com reshape")
print(np.random.randn(8).reshape(4,2))
print()


# In[26]:


# Mas para o que serve mesmo tudo isso?
# Vamos ver no grafico

get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# In[27]:


data = np.random.randn(50000)

data


# In[28]:


hx, hy, _ = plt.hist(data, bins=25, density=1, color="blue")

plt.ylim(0.0,max(hx)+0.05)
plt.title('Numeros aleatorios da distribuicao normal')
plt.grid()

