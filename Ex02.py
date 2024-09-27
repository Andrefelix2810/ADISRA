def contar_pares_impares(matriz, linhas, colunas):
    pares = 0
    impares = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] % 2 == 0:
                pares += 1
            else:
                impares += 1
    
    return max(pares, impares)

# Exemplo de uso
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

linhas = 3
colunas = 3

resultado = contar_pares_impares(matriz_exemplo, linhas, colunas)
print(f"A maior quantidade de ocorrências é: {resultado}")