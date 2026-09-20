# ================================================
# PROGRAMA: Calculando Descontos
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 19/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: Lê um valor e aplica desconto
# ================================================

print('=' * 30)
print('Calculando Descontos'.center(30))
print('=' * 30)

valor = float(input('Digite o valor do produto: R$'))
desconto = float(input('Digite o valor do desconto: '))
desc = (valor / 100) * desconto
valor_final = valor - desc

print(f'O valor do produto é R${valor:.2f}')
print(f'e teve o desconto de {desconto} % ')
print(f'valor final R${valor_final:.2f}')
print('fim do programa')
