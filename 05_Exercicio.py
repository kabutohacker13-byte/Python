# Programa para saber qual o sucessor e o antecessor de um numero
# Programador: Antonio Claudio
# contato: kabutohacker13@gmail.com
print('#' * (30))
print('Antecessor e Sucessor' .center(30))
print('#' * (30))
mais = 0
menos = 0
numero = int(input('Digite um numero: '))
mais = numero + 1
menos = numero - 1
print(f'O {menos} é o antecessor do {numero} e {mais} é o sucessor do {numero}')