# ================================================
# PROGRAMA: Sorteando um item na lista
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 20/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: Faz um sorteio aleatorio
# ================================================

import random

print('=' * 30)
print('Sorteando um item na lista'.upper().center(30))
print('=' * 30)

nomes = ['Ana', 'Cristiane', 'Lucas', 'Kabuto', 'Claudio']
sorteado = random.choice(nomes)
print(f'E o escolhido foi: {sorteado}')




