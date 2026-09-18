# ================================================
# PROGRAMA: Pintando Parede
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 18/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: Calcula o quato de tinta ira gastar
# ================================================

print('=' * 30)
print('Pintando Parede'.center(30))
print('=' * 30)

lado_1 = float(input('Digite a medida de um largura: '))
lado_2 = float(input('Digite a medida da altura: '))
medida = lado_1 * lado_2
tinta = medida / 2
print(f'A medida para pintar é {medida} m2 e precisa de {tinta} litros de tinta')