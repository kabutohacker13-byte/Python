'''Exercício Python 082: 
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''
par = []
impar = []
numero = []
while True:
    num = int(input('Digite 0 para parar ou digite um numero: '))
    if num == 0:
        break
    numero.append(num)
    
for num in numero:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num) 
print(f'Numeros digitados: {sorted(numero)}')
print(f'Numeros pares: {sorted(par)}')
print(f'Numeros impares: {sorted(impar)}')