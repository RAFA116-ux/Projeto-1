def exibir_matriz(matriz):
    print("\n🔥 ÍDOLOS DO FLAMENGO VS CORINTHIANS ⚽\n")
    print(f"{'FLAMENGO':<15} | {'CORINTHIANS':<15}")
    print("-" * 32)

    for linha in matriz:
        print(f"{linha[0]:<15} | {linha[1]:<15}")

# Matriz de ídolos Flamengo x Corinthians
matriz = [
    ["ZICO", "SÓCRATES"],
    ["GABIGOL", "RIVELLINO"],
    ["ARRASCAETA", "MARCELINHO"],
    ["LEANDRO", "NETO"],
    ["JUNIOR", "CASAGRANDE"]
]

# Chama a função para exibir a matriz
exibir_matriz(matriz)
