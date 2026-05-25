meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print("🚀 Vendedores que bateram a meta:")
print("---------------------------------")

# O loop percorre a lista principal e separa o nome e o valor de cada linha
for vendedor, valor in vendas:
    # Verifica se o valor vendido é maior ou igual à meta
    if valor >= meta:
        print(f"Vendedor: {vendedor} - Vendeu: R$ {valor:,.2f}")

print("---------------------------------")