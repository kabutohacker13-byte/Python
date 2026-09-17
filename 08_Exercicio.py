# Programa Conversor de Medidas
# Programador: Antonio Claudio
# Contato: kabutohacker13@gmail.com
# Data: 17/09/2026
print('-' * 30)
print('Conversor de Medidas'.center(30))
print('-' * 30)

medida = float(input("Digite a medida em metros: "))
centimetros = medida * 100
milimetros = medida * 1000
print(f"A medida em centímetros é: {centimetros:.2f}")
print(f"A medida em milímetros é: {milimetros:.2f}")    
print("Programa finalizado.")