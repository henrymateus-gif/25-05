produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

print("📊 RELATÓRIO DE CRESCIMENTO DE VENDAS (2019 vs 2020)")
print("Apenas produtos que tiveram alta no período:")
print("-" * 65)

# O enumerate nos dá o índice (i) e o item (produto) ao mesmo tempo
for i, produto in enumerate(produtos):
    venda_19 = vendas2019[i]
    venda_20 = vendas2020[i]
    
    # Condição: Só avança se as vendas de 2020 forem MAIORES que as de 2019
    if venda_20 > venda_19:
        # Calcula o percentual de crescimento conforme a fórmula dada
        crescimento = (venda_20 / venda_19) - 1
        
        # Exibe os dados formatados
        # :.<18 cria um alinhamento com pontinhos para o nome do produto
        # :,.0f formata os números com separador de milhar
        # :+.1% formata como porcentagem com sinal de + ou - e 1 casa decimal
        print(f"Produto: {produto:.<18} | 2019: {venda_19:,.0f} | 2020: {venda_20:,.0f} | Crescimento: {crescimento:+.1%}")

print("-" * 65)