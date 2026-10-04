'''Exercício Python 084: 
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.                                              
C) Uma listagem com as pessoas mais leves.'''

nome = []
peso = []
total = 0
pessoas = []
dado = []

while True:
    pessoas.append(str(input('Digite um nome: ')))
    pessoas.append(int(input('Digite o peso: ')))
    dado.append(pessoas[:])
    pessoas.clear()
    continuar = input('\nDeseja continuar? (s/n): ')
    if continuar.lower() == 'n':
        break

print(f'\n===== {len(dado)} PESSOAS CADASTRADAS =====')
for i, p in enumerate(dado, 1):
    print(f'{i}º - {p[0]} - {p[1]}kg')
maior_peso = max(dado, key=lambda x: x[1])
menor_peso =min(dado, key=lambda x: x[1])

print(f'\n===== ESTATÍSTICAS =====')
print(f'Maior peso: {maior_peso[0]} com {maior_peso[1]}kg')
print(f'Menor peso: {menor_peso[0]} com {menor_peso[1]}kg')
    
    


                                                       
                                                       
                                                       
                                                       
                                                       
                                                       
        