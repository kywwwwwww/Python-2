def converter_para_maiusculas(lista_strings):
    return [string.upper() for string in lista_strings]

# Exemplo de uso:
lista_strings = ["olá", "mundo", "python", "é", "incrível"]
lista_maiusculas = converter_para_maiusculas(lista_strings)
print("Lista em letras maiúsculas:", lista_maiusculas)