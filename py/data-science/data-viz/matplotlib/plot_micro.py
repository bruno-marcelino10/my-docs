import matplotlib.pyplot as plt
import numpy as np


# x -> y nas funções 

def f(x):
    return (50 - (2*x))/5

x = np.arange(0, 1000, 1) #cria uma sequencia de 0 a 60 de 5 em 5
y1 = f(x)
y2 = f(x/2)

plt.plot(x, y2, label = "Reta Orçamentária 2", color = "green", linewidth = 2) 
plt.plot(x, y1, label = "Reta Orçamentária 1", color = "red", linewidth = 2) #x1 = variavel independente, x2 = função
plt.legend()
plt.xlabel("Bem 1", fontsize = 12)
plt.ylabel("Bem 2", fontsize = 12) 
plt.title("Reta Orçamentária - Exercício 4")
plt.axis([0, 60, 0, 30]) #x min, x max, y min, y max (tamanho dos eixos)
plt.grid(True)
plt.text(12, 16, "Conjunto Orçamentário", fontsize = 18)
plt.show()

plt.scatter(x,y) # plotar duas variaveis juntas
plt.show() # mostra o gráfico
'''

class Gráfico:

    x = np.arange(-1000, 1000, 1)
    y = f(x)

    tamanho_eixos = [0,60,0,30]

    def f(self,x):
        return (50 - (2*x))/5

    def plotar(self):
        plt.plot(self.x, self.y, label = "Reta Orçamentária 2", color = "green", linewidth = 2) #x1 = variavel independente, x2 = função
        plt.legend()
        plt.xlabel("Bem 1", fontsize = 12)
        plt.ylabel("Bem 2", fontsize = 12) 
        plt.title("Reta Orçamentária - Exercício 4")
        plt.axis(self.tamanho_eixos) #x min, x max, y min, y max (tamanho dos eixos)
        plt.grid(True)
        plt.text(12, 16, "Conjunto Orçamentário", fontsize = 18)
        plt.show()
    
    def mudar_tamanho_eixos(self, x_min,x_max,y_min,y_max):
        self.tamanho_eixos = [x_min, x_max, y_min, y_max]

meu_grafico = Gráfico()
meu_grafico.mudar_tamanho_eixos(-10, 40, -10, 20)
meu_grafico.plotar()

'''