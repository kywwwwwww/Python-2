def contar_ocorrencias_palavras(texto):
    palavras = texto.split()
    ocorrencias = {}
    for palavra in palavras:
        ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1
    return ocorrencias

# Exemplo de uso:
texto = input("Digite um texto: ")
ocorrencias_palavras = contar_ocorrencias_palavras(texto)
for palavra, quantidade in ocorrencias_palavras.items():
    print(f"{palavra}: {quantidade} ocorrências")