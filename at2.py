# Inicializa as variáveis
soma = 0
numero_atual = 1

# O loop continua enquanto a soma for menor ou igual a 20
while soma <= 20:
    soma += numero_atual
    
    # Exibe o passo a passo da soma (opcional, mas bom para entender)
    print(f"Somando {numero_atual}... Soma atual = {soma}")
    
    # Passa para o próximo número inteiro
    numero_atual += 1

print("---")
print(f"Resultado final: A soma ultrapassou 20 e chegou a {soma}.")