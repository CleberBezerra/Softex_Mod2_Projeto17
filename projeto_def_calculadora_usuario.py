from cgitb import reset

def calculadora_usuario(num1, num2, operacao):
    if (operacao == 1):
        resultado = num1 + num2
    elif (operacao == 2):
        resultado = num1 - num2
    elif (operacao == 3):
        resultado = num1 * num2
    elif (operacao == 4):
        resultado = num1 / num2
    #elif (operacao == 0):
    else:
        print("Essa opção não existe!!!")

    return resultado

operacao = int(input("Digite o valor correspondente a operação: \n 1: Soma\n 2: Subtração\n 3: Multiplicação\n 4: Divisão\n 0: Sair\n"))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

res = calculadora_usuario(num1, num2, operacao)
print("O resultado é: ",res)