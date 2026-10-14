turma = {}

turma['nome'] = str(input('Digite o nome: '))
turma['media'] = float(input('Digite  a media: '))

if turma['media'] >= 7:
    turma['situacao'] = 'Aprovado'
else:
    turma['situacao'] = 'reprovado'
for k, v in turma.items():
    print(f'{k} = {v}')
print(turma)