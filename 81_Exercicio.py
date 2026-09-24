'''Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.                                                                                      
C) Se o valor 5 foi digitado e está ou não na lista.'''

num1 = 0
numero = []
while True:

    num = int(input('DIGITE 0 PARA PARAR ou Digite um numero: '))

    if num == 0:
        break
    numero.append(num)
    
    num1 += 1
if 5 in numero:
    print('O numero 5 foi digitado')
else:
    print('numero 5 não foi digitado')    
print(f'Foi digitado {num1} numeros {sorted(numero, reverse=True)}')    