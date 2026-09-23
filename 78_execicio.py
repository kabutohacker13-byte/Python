# ================================================
# PROGRAMA: MAIOR E MENOR
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 23/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: identifica o maior e menor numero de uma lista
# ================================================

print('=' * 30)
print('maior  menro'.upper().center(30))
print('=' * 30)
numero = []
while True:
    num = int(input('Digite 0 para parar digite um numero: '))
    if num == 0:
        break
    numero.append(num)
print(numero)

if len(numero) > 0:
    maior = max(numero)
    menor = min(numero)
print(f'O numero maior é: {maior}')
print(f'Numero menor é : {menor}')