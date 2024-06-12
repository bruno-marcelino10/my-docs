#CÁLCULO DA FORÇA DA TACADA

'''
força final = dist +- altura real +- vento real

altura real = H+ ou H- da dist x altura 

vento real = seno do angulo do vento (influência vertical) x (altura/100 + HWI da dist) x vento 

'''

import math

def altura_real(H, altura_inicial):
    return H*altura_inicial

def vento_real(angulo_do_vento,hwi_inicial,vento_inicial):
    return math.sin(angulo_do_vento/math.pi*180)*vento_inicial*hwi_inicial

def forca(distancia,height,wind):
    return distancia+height+wind

#CÁLCULO DO DESVIO 

'''
hwi_desvio = altura/100 + hwi da dist
desvio = cosseno do angulo x vento x hwi_desvio
desvio em pb = desvio / 0.216

'''

def calc_hwi_desvio(hwi_inicial, altura):
    return (altura/100)+hwi_inicial

def calc_desvio(angulo_do_vento, vento_inicial, hwi_desvio):
    return math.cos(angulo_do_vento)*vento_inicial*hwi_desvio

continuar = True
while continuar:
    H = float(input("Digite o H+/H- sem sinal: "))
    altura = float(input("Digite a altura com sinal: "))

    hwi = float(input("Digite o HWI: "))
    angulo = int(input("Digite o ângulo: "))
    vento = int(input("Digite o valor do vento em m: "))

    distancia_inicial = float(input("Digite a distância do buraco em y: "))

    desvio_em_pb = calc_desvio(angulo,vento,calc_hwi_desvio(hwi,altura))/0.216
    print("O desvio da tacada, em Power Bars, é: ",desvio_em_pb)

    forca_final = forca(distancia_inicial,altura_real(H, altura),vento_real(angulo,hwi,vento))
    print("A força necessária para a tacada é ",forca_final)

    print("OBS.: Favor olhar a força dada na tabela. Para tacar, deve-se colocar um pouco mais")

    if input("Fechar programa? (s/n): ").lower() == "s":
        continuar = False
