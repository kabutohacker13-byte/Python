# ================================================
# PROGRAMA: Aluguel de Carros
# AUTOR: Antonio Claudio
# EMAIL: kabutohacker13@gmail.com
# DATA: 19/09/2026
# VERSÃO: 1.0
# DESCRIÇÃO: Calcula quanto cobrar de aluguel
# ================================================

print('=' * 30)
print('Aluguel de Carros'.center(30))
print('=' * 30)

dias = int(input('Digite quantos dias usou: '))
km_inicio = int(input('Digite quantos km inicial: '))
km_final = int(input('Digite o km final: '))
total_dias = dias * 60
km_total = km_final - km_inicio
km_valor = km_total * 0.15
valor_final = total_dias + km_valor
print(f'Seu carro foi alugado por {dias} dias x R$60 = R${total_dias:_.2f}'.replace(".", ",").replace("_", "."))
print(f'e rodou {km_total}km x R$0.15 = R${km_valor:_.2f}'.replace(".", ",").replace("_", "."))
print(f'ficando o todal de R${valor_final:_.2f}'.replace(".", ",").replace("_", "."))
print('Obrigado, Volte sempre!')



