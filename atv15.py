def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Escolha a conversão (1 - Celsius para Fahrenheit, 2 - Fahrenheit para Celsius): ")

if opcao == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius:.2f} graus Celsius equivale a {fahrenheit:.2f} graus Fahrenheit.")
elif opcao == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit:.2f} graus Fahrenheit equivale a {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida. Escolha 1 ou 2 para realizar a conversão.")