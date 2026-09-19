# ================================================
# PROGRAMA: Conversor de Temperaturas
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 19/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: converte graus Celsius e converta para graus Fahrenheit.
# ================================================

print('=' * 30)
print('Conversor de Temperaturas'.center(30))
print('=' * 30)
celsius = float(input('Digite a temperatura em celsiuos: '))
temp = (celsius * 1.8) + 32
print(f'A temperatura em c {celsius} convertida para f é {temp}')