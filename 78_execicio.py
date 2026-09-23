# ================================================
# PROGRAMA: MAIOR E MENOR
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 23/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: identifica o maior e menor numero de uma lista
# ================================================

print('=' * 30)
print('maior  menro'.upper().center(30))
print('=' * 30)

numero = []
for num in range(0, 5):
    num = int(input('Digite um numero:'))
    numero.append(num)
print(numero)
if len(numero) > 0:
    maior = max(numero)
    menor = min(numero)
    posicao_maior = numero.index(maior)
    posicao_menor = numero.index(menor)
    print(f"Maior: {maior} - Posição: {posicao_maior}")
    print(f"Menor: {menor} - Posição: {posicao_menor}")


'''valores = []
valores.append(9)
valores.append(4)
valores.append(5)
for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')'''

'''numero = [] #cria uma lista vazia para receber o dados depois de inserido
while True: #cria um laço que enquanto nao digitar 0 o usuario continua 
    num = int(input('Digite 0 para parar digite um numero: ')) #entrada de dados pelo usuario 
    if num == 0: # condição ao numero 0 para o loop
        break
    numero.append(num) #inseri os dados digitado pelo usuario na lista que estava vazia
print(numero) #Exibe os numeros digitados

if len(numero) > 0: #define se o numero maior que zero 
    maior = max(numero) #verifica qual o numero maior e adiciona na variavel maior
    menor = min(numero) #verifica qual o numero menor e adiciona na variavel mmenor
    print(f'O numero maior é: {maior}') #Exibe o numero maior
    print(f'Numero menor é : {menor}') #Exibe o numero menor
else:
    print('Nenhum numero foi digitado!')'''