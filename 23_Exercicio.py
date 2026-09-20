# ================================================
# PROGRAMA: Separando dígitos de um número
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: DD/MM/YYYY
# VERSÃO: 1.0
# DESCRIÇÃO: programa lê um digito de 0 9999 e exibe os digitos separados
# ================================================

print('=' * 30)
print('Separando dígitos de um número'.upper().center(30))
print('=' * 30)

numero = int(input('Digite um numero de 0 a 9999 : '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {}'.format(numero))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

