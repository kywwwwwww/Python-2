def encontrar_maior_e_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None
    maior = menor = lista_palavras[0]
    for palavra in lista_palavras:
        if len(palavra) > len(maior):
            maior = palavra
        elif len(palavra) < len(menor):
            menor = palavra
    return maior, menor

# Exemplo de uso:
lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
maior_palavra, menor_palavra = encontrar_maior_e_menor_palavra(lista_palavras)
print(f"Maior palavra: {maior_palavra}")
print(f"Menor palavra: {menor_palavra}")