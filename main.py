import statistics

vendas = [1500, 2300, 1800, 2000, 2500]

print("Análise de Vendas")
print(f"Total: {sum(vendas)}")
print(f"Média: {statistics.mean(vendas)}")
print(f"Maior venda: {max(vendas)}")
print(f"Menor venda: {min(vendas)}")
