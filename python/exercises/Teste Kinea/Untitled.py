#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class SimpleQueue: 
    
    def __init__(self, pos_1, pos_2, pos_3):

        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.pos_3 = pos_3

    def Tamanho(self): # pode-se definir MÉTODOS que são funções cujos argumentos já foram definidos na classe

        print(len([self.pos_1, self.pos_2, self.pos_3]))

    def MostrarFila(self): 

        print(self.pos_1, self.pos_2, self.pos_3)

    def AdicionarObjeto(self, num):

        print(self.pos_1, self.pos_2, self.pos_3, num) 
        
    #def RemoverObjeto(self, num):
       # Não tive tempo :(

fila = SimpleQueue(1,2,3)        
             
print(fila.Tamanho())
print(fila.AdicionarObjeto())
print(fila.MostrarFila())
print(fila.RemoverObjeto())

