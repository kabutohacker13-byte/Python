# Programa Tabuada
# Programador: Antonio Claudio
# Contato: kabutohacker13@gmail.com
# Data: 17/09/2026
print('-' * 30)
print('Tabuada'.center(30))
print('-' * 30)

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print('Programa finalizado. Volte sempre!')
print