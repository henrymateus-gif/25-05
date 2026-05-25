# Inicializa a lista do quarto vazia
quarto = []

# 1. Pergunta a quantidade de pessoas que ficarão no quarto
quantidade_pessoas = int(input("Quantas pessoas ficarão no quarto (1 a 4)? "))

# 2. Loop FOR que roda exatamente a quantidade de vezes necessária
for i in range(quantidade_pessoas):
    print(f"\n--- Cadastro da {i + 1}ª pessoa ---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    
    # Cria uma lista menor para essa pessoa específica
    hospede = [nome, f"cpf:{cpf}"]
    
    # 3. Adiciona a lista da pessoa dentro da lista principal 'quarto'
    quarto.append(hospede)

# Exibe o resultado final estruturado
print("\n=========================================")
print("Quarto registrado com sucesso!")
print(quarto)
print("=========================================")