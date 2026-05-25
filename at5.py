# Pede a palavra ao usuário e a converte para minúsculas
palavra = input("Digite uma palavra: ").lower()

# Define quais são as vogais que estamos procurando
vogais = "aeiouáéíóúâêîôûãõàèìòù"

# Inicializa o contador de vogais e o índice do loop
quantidade_vogais = 0
indice = 0

# O loop vai rodar enquanto o índice for menor que o tamanho da palavra
while indice < len(palavra):
    # Verifica se a letra atual está dentro da string de vogais
    if palavra[indice] in vogais:
        quantidade_vogais += 1
    
    # Avança para a próxima letra
    indice += 1

print(f"A palavra digitada contém {quantidade_vogais} vogal(is).")
