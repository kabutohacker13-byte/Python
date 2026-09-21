# ================================================
# PROGRAMA: Verificando se tem santo no nome
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 21/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: leia o nome de uma cidade diga
# se ela começa ou não com o nome “SANTO”.
# ================================================

print('=' * 30)
print('NOME DO PROGRAMA'.upper().center(30))
print('=' * 30)

#1- entrada de dados na variavel com input
cidade = input('Digite o nome da cidade: ')

#2- criar a palavra que quer que seja identificada
nome = 'santo'

#- 3 fazer todos os textos ficarem minusculo e 
# identificar se tem o nome que foi definido ou não 
if nome.lower() in cidade.lower():
    #Depois de vericado o nome caso encontre sera exibido nesse prmeiro
    print('Contem SANTO no nome dessa cidade')
    
else:
    # Senao tiver o nome sera exibido aqui
    print('Não contem Santo no nome dessa cidade')
 