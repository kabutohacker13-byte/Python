'''Exercício Python 083: 
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos e fechados 
na ordem correta.'''

expressao = input('Digite uma expressão: ')

abertos = 0

for caractere in expressao:
    if caractere == '(':
        abertos += 1
    elif caractere == ')':
        abertos -= 1
    
    # Se fecha mais que abre, está errado
    if abertos < 0:
        print('❌ Parênteses incorretos!')
        break
else:
    # Se terminou e está balanceado
    if abertos == 0:
        print('✅ Parênteses corretos!')
    else:
        print('❌ Parênteses não balanceados!')