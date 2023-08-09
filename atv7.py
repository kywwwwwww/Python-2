def calcular_fatorial(numero):
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Exemplo de uso:
numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")