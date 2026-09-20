# ================================================
# PROGRAMA: Analisador de Textos
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: DD/MM/YYYY
# VERSÃO: 1.0
# DESCRIÇÃO: leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
# ================================================

print('=' * 30)
print('Analisador de Textos'.upper().center(30))
print('=' * 30)

nome = input('Digite seu nome: ')
titulo = nome.title()
print(titulo)
print('nome em maiusculo é: ',nome.upper())
print('nome em minusculo é : ',nome.lower())
total = len(nome.replace(" ", ""))
print(f'O total de letras no nome sem espaços é : {total}')
primeiro = nome.split()[0]
quantidade = len(primeiro)
print(f'O primeiro nome tem : {quantidade} letras')


