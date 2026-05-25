
numero = int(input("Digite um número para ver a sua tabuada: "))

contador = 1

print(f"\n--- Tabuada do {numero} ---")

while contador <= 10:
    resultado = numero * contador
    
    print(f"{numero} x {contador:2d} = {resultado}")
    

    contador += 1
