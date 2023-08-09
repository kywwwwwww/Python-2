def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        meio1 = lista_ordenada[n // 2 - 1]
        meio2 = lista_ordenada[n // 2]
        return (meio1 + meio2) / 2

# Exemplo de uso:
lista_numeros = [10, 15, 20, 30, 40, 50]
mediana = calcular_mediana(lista_numeros)
print("Mediana dos valores:", mediana)