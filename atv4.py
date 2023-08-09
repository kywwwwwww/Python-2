def verificar_palindromo(palavra):
    return palavra == palavra[::-1]

# Exemplo de uso:
palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
