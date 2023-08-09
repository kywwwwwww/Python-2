import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

dado1, dado2 = lancar_dados()
soma = dado1 + dado2
print(f"Lançamento: Dado 1: {dado1}, Dado 2: {dado2}, Soma: {soma}")