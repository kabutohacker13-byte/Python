# ================================================
# PROGRAMA: Seno, Cosseno e Tangente
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: DD/MM/YYYY
# VERSÃO: 1.0
# DESCRIÇÃO: Lê um angulo e calcula o seno, cosseno e tangente 
# ================================================
import math

print('=' * 30)
print('Seno, Cosseno e Tangente'.upper().center(30))
print('=' * 30)

angulo = int(input('Digite um angulo: '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f'Para o grau de {angulo} o seno é: {seno:.2f} o cosseno é: {cosseno:.2f} e a tangente é: {tangente:.2}')