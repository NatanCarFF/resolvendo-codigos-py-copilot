# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicitando a string e o número inteiro do usuário
texto = input("Digite uma string: ")
numero_repeticoes = int(input("Digite um número inteiro para a quantidade de repetições: "))

# Repetindo a string o número de vezes informado
resultado = texto * numero_repeticoes

# Imprimindo o resultado
print("O texto repetido é:", resultado)
