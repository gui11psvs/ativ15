# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
num1 = float(input("digete o primeiro número: "))
num2 = float(input("digete o segundo número: "))

operacao = input("digite a operação (soma, subtração, multiplicação, divisão): ")

if operacao == "soma":
    resultado = num1 + num2
    print(f"o resultado da soma é: {resultado}")
elif operacao == "subtração" or operacao == "subtracao":
    resultado = num1 - num2
    print(f"o resultado da subtração é: {resultado}")
elif operacao == "multiplicação" or operacao == "multiplicação":
    resultado = num1 * num2
    print(f"o resultado da multiplicação é: {resultado}")
elif operacao == "divisão" or operacao =="divisão":
    if num2 != 0:
        resultado = num1 / num2
        print(f"o resultado da divisão é: {resultado}")
    else:
        print("erro: divisão por zero não é permitida.")
else:
    print("operação inválida! tente novamente.")
    