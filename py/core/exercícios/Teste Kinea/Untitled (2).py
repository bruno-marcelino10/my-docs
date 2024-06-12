#!/usr/bin/env python
# coding: utf-8

# In[16]:


class SimpleQueue: 
    
    def __init__(self, pos_1, pos_2, pos_3):

        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.pos_3 = pos_3
        
        lista = [self.pos_1, self.pos_2, self.pos_3].sort()

    def Tamanho(self): # pode-se definir MÉTODOS que são funções cujos argumentos já foram definidos na classe
        return len(lista)

    def MostrarFila(self): 
        return lista

    def AdicionarObjeto(self, num):
        lista.append(num) 
        return lista
        
    def RemoverObjeto(self):
        lista.pop(0) 
        return lista
    
fila = SimpleQueue(1,2,3)        
             
print(fila.Tamanho())
print(fila.AdicionarObjeto(2))
print(fila.MostrarFila())
print(fila.RemoverObjeto())

