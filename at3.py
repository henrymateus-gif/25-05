import random

# O computador escolhe um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa as variáveis de controle
tentativas = 0
acertou = False

print("🔢 Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")
print("-------------------------------------------------------------------------")

# O loop continua até que 'acertou' seja True
while not acertou:
    # Recebe o palpite do jogador
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1  # Conta mais uma tentativa
    
    # Verifica o palpite
    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
        acertou = True  # Altera a condição para encerrar o loop
    elif palpite < numero_secreto:
        print("MUITO BAIXO! Tente um número maior. ⬆️")
    else:
        print("MUITO ALTO! Tente um número menor. ⬇️")