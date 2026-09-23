numero = []
while True:
    num = int(input('Digite 0 para parar digite um numero: '))
    if num == 0:
        break
    numero.append(num)
print(numero)

if len(numero) > 0:
    maior = max(numero)
    menor = min(numero)
print(f'O numero maior é: {maior}')
print(f'Numero menor é : {menor}')