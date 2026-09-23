numero = []

while True:
    num = int(input('Digite um numero: '))
    if num in numero:
        print(f'Numero {num}ja foi digitado tente outro')
    else:
        numero.append(num)
        print(f'Numero {num} adicionado')

    continuar = input('Quer continuar? (s/n): ')
    if continuar.lower() == 'n':
        break
print(f'lista final {sorted(numero)}')