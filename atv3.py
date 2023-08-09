def imprimir_numeros_ate_n(n):
    if n < 0:
        return
    for i in range(n+1):
        print(i)

# Exemplo de uso:
numero = int(input("Digite um número inteiro positivo: "))
imprimir_numeros_ate_n(numero)
