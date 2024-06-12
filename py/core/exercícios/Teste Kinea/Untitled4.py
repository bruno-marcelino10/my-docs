#!/usr/bin/env python
# coding: utf-8

# In[5]:


# RECURSÃO:
def fibonacci_recursivo(n):

    if n < 0:
        resultado = None
    elif n == 0:
        resultado = 0
    elif n == 1:
        resultado = 1
    else:
        resultado = fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
        
    return(resultado)

# PROGRAMAÇÃO DINÂMICA: (usa lista)
def fibonacci_iterativo(n):
    
    if n < 0:
        resultado = None
    elif n == 0:
        resultado = 0
    elif n == 1:
        resultado = 1
    else:
        i = 2
        lista = [0,1]
        while i <= n:
            lista.append(lista[i-1] + lista[i-2])
            i = i + 1
    return(lista[n])

print(fibonacci_recursivo(10)) # décimo elemento
print(fibonacci_iterativo(10))


# In[ ]:




