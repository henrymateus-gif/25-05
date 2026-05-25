numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Inicializa o acumulador da soma total
soma_total = 0

print("🔢 Mostrando cada número individualmente:")
print("----------------------------------------")

# 1. O primeiro loop percorre as linhas (as sublistas)
for linha in numeros:
    
    # 2. O segundo loop percorre os elementos dentro de cada linha
    for numero in linha:
        print(f"Número encontrado: {numero}")
        
        # 3. Soma o número atual ao totalizador
        soma_total += numero

print("----------------------------------------")
# 4. Exibe a soma de todos os números ao final
print(f"🏆 A soma total de todos os números é: {soma_total}")