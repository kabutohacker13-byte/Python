# ================================================
# PROGRAMA: Procurndo por um nome
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 21/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: programa procura se a um nome em uma frase
# ================================================

print('=' * 30)
print('Procurndo por um nome'.upper().center(30))
print('=' * 30)

# 1 primeiro entra com o nome usando input em uma variavel
nome = input('Digite o nome: ')
texto = 'silva'

# 2 segundo fazer a verificação e dexar todas os caracteres em minusculo 
# para fazer a identicação
if texto.lower() in nome.lower():
    print('Esse nome tem Silva ')
else:
    print('Esse nome nao tem Silva')