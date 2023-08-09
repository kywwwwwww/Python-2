def calcular_media(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)

# Exemplo de uso:
lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print("A média dos valores é:", media)