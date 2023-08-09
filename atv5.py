def filtrar_numeros_pares(lista):
    return [num for num in lista if num % 2 == 0]

# Exemplo de uso:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filtrar_numeros_pares(numeros)
print("Números pares:", numeros_pares)