# ================================================
# PROGRAMA: Conversor de Moedas
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 18/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: Converte outras moedas em real
# ================================================

print('=' * 30)
print('Conversor de Moedas'.center(30))
print('=' * 30)

valor = float(input('Digite o valor converter R$: '))
dolar = valor / 5.32
print(f'Com R${valor} você compra ${dolar:.2f} dolares')
