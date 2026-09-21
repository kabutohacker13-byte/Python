# ================================================
# PROGRAMA: Primeira e última ocorrência de uma string
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 21/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: Faça um programa que leia uma 
# frase pelo teclado e mostre quantas vezes aparece 
# a letra “A”, em que posição ela aparece a primeira
# vez e em que posição ela aparece a última vez.
# ================================================

print('=' * 30)
print('NOME DO PROGRAMA'.upper().center(30))
print('=' * 30)

frase = input('Digite uma frase: ')
nova = frase.lower().count('a')
sem_espaco = frase.replace(' ', '')
novo = len(sem_espaco)
nov  = sem_espaco.index('a')
novo2 = sem_espaco.index('a', -1)
print(f'A altima letra a se encontra na possição {novo2}')
print(f'A primeira letra a se encontra na posição {nov}')
