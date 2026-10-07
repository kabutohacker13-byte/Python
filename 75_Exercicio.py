# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


num = []

for i in range(4):
       valor = int(input('Digite 4 numeros: '))
       num.append(valor)
num = tuple(num)
print(f'Voce digitou os numeros {num}')
print(f'O numero 9 aparece {num.count(9)} vezes')
if 3 in num:
       print(f'O numero 3 aparece na posição {num.index(3)}')
else:
       print('Voce nao digitou o numero 3')
for n in num:
       if n % 2 == 0:
              print(f'Os numros {n} é par')





