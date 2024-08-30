num_Binario = input("agrega un numero: ")
num_inverso = num_Binario[::-1]
contador = 0
caja = 0
for i in num_inverso:
    resultado = int(i) * 2**contador
    caja = caja + resultado
    contador += 1

print(f"el numero binario a decimal es: {caja}")
