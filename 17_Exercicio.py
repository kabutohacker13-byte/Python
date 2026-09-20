# ================================================
# PROGRAMA: Catetos e Hipotenusa
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 20/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: calcula os catetos e acha a hipotenusa
# ================================================
from math import sqrt
print('=' * 30)
print('Catetos e Hipotenusa'.upper().center(30))
print('=' * 30)

cateto_1 = int(input('Digite o primeiro cateto: '))
cateto_2 = int(input('Digite o segundo catato: '))  
hipotenusa = sqrt(cateto_1*cateto_1+cateto_2*cateto_2) #((cateto_1 ** 2) + (cateto_2 ** 2)) ** (1/2)
print(f' A soma dos catetos elevado ao quadrado é: {hipotenusa:.2f}')
print('Fim do programa!')