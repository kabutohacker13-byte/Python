# Programa Conversor de Medidas
# Programador: Antonio Claudio
# Contato: kabutohacker13@gmail.com
# Data: 17/09/2026
print('-' * 30)
print('Conversor de Medidas'.center(30))
print('-' * 30)

# Pede pro usuário digitar um valor (em metros)
# float() = converte o texto para número decimal (com casa decimal)
# Guarda o valor na variável medida
medida = float(input("Digite a medida em metros: "))

# Pega o valor de medida
# Multiplica por 100 (porque 1 metro = 100 centímetros)
# Guarda o resultado em centimetros
centimetros = medida * 100

# Pega o valor de medida
# Multiplica por 1000 (porque 1 metro = 1000 milímetros)
# Guarda o resultado em milimetros
milimetros = medida * 1000

# Imprime o resultado formatado
# {centimetros:.2f} = mostra só 2 casas decimais
# f"..." = permite usar variáveis dentro do texto
print(f"A medida em centímetros é: {centimetros:.2f}")
print(f"A medida em milímetros é: {milimetros:.2f}") 

# Imprime uma mensagem indicando que o programa terminou   
print("Programa finalizado.")

'''RESUMO DA LÓGICA:
Recebe um valor em metros do usuário
Converte para centímetros (multiplica por 100)
Converte para milímetros (multiplica por 1000)
Mostra os resultados com 2 casas decimais
Finaliza o programa'''