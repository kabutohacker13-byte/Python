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
ordem = random.sample(nomes, len(nomes))
for posicao, nome in enumerate(ordem, start=1):
    print(f'{posicao}º o escolhido foi: {nome}')