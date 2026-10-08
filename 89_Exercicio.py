ficha = []

while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? (s/n): ')).lower()
    if resp == 'n':
        break
print('-=' * 30)
print(f'{'No.':<4}{'Nome':<10}{'Media':>8}')
print('_' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')                                                                                        
while True:
    print('_' * 35)
    opc = int(input('Mostar notas de qual aluno? (999) finalizar: '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<<   VOLTE SEMPRE   >>>')