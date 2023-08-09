def encontrar_maior_e_menor_numero(sequencia):
    if not sequencia:
        return None, None
    maior = menor = sequencia[0]
    for numero in sequencia:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    return maior, menor

# Exemplo de uso:
sequencia = [int(num) for num in input("Digite uma sequência de números separados por espaço: ").split()]
maior_numero, menor_numero = encontrar_maior_e_menor_numero(sequencia)
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")