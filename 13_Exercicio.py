# ================================================
# PROGRAMA: Reajuste Salarial
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 19/09/2016
# VERSÃO: 1.0
# DESCRIÇÃO: Faz o reajuste de salario
# ================================================

print('=' * 30)
print('Reajuste Salarial'.center(30))
print('=' * 30)

salario = float(input('Digite o valor do salario:R$ '))
reajuste = float(input('Digite o reajuste: '))
novo = salario * (reajuste / 100)
novo2 = salario + novo
print(f'R${novo2:.2f}')