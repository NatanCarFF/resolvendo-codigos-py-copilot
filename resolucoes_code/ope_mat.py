# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitando os números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Escolhendo a operação a ser realizada
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada: ")

# Realizando a operação
if opcao == '1':
    resultado = numero1 + numero2
    operacao = "adição"
elif opcao == '2':
    resultado = numero1 - numero2
    operacao = "subtração"
elif opcao == '3':
    resultado = numero1 * numero2
    operacao = "multiplicação"
elif opcao == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        operacao = "divisão"
    else:
        print("Erro: Divisão por zero!")
        resultado = None
else:
    print("Opção inválida!")
    resultado = None

# Imprimindo o resultado, se válido
if resultado is not None:
    print(f"O resultado da {operacao} é: {resultado}")
