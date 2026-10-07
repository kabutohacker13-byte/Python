valor = []
par = []
impar = []

for i in range(0, 7):
    numero = int(input('Digite um numero: '))
    valor.append(numero)
    
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
       
print(f"Todos os valores: {sorted(valor)}")
print(f"Valores pares: {sorted(par)}")
print(f"Valores ímpares: {sorted(impar)}")
