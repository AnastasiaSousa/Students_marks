# --------------------------------------------------------------------------------
# O programa lê as 10 notas e de seguida executa as 10 operacoes diferentes
# 14-02-2023, Anastasiya Sousa
# --------------------------------------------------------------------------------

print('---------------------------------------------------------------------------------------')
print('Programa para pedir as 10 notas.')
print('De seguida mostra executa as 10 operacoes.')
print('---------------------------------------------------------------------------------------')


notas = [] # cria uma lista vazia para armazenar as notas

# lê as 10 notas
for i in range(10):
    while True:
        try:
            nota = float(input("Digite a nota nº {} (entre 0 e 20): ".format(i+1)))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print('A nota deve estar entre 0 e 20')
        except ValueError:
            print('Digita os numeros corretos')

print(notas)

# imprime as notas
print('---------------------------------------------------------------------------------------')
print("1. Lista introduzida: ", notas)
print('---------------------------------------------------------------------------------------')
print("2. Elementos da Lista: ", end="")
for i in range(len(notas)):
    print(notas[i], end=" ")
print()
print('---------------------------------------------------------------------------------------')
print("3. Ordem Inversa:")
for i in range(len(notas) - 1, -1, -1):
    print(notas[i])
print('---------------------------------------------------------------------------------------')
# ordena as notas em ordem crescente
notas.sort()
# imprime as notas em ordem crescente
print("4. Ordem crescente: ", end="")
for i in range(len(notas)):
    print(notas[i], end=" ")
print()
print('---------------------------------------------------------------------------------------')
# calcula a soma das notas
soma = sum(notas)
# imprime a soma das notas
print("5. Soma dos elementos:", soma)
print('---------------------------------------------------------------------------------------')
# calcula o maior elemento
maior = max(notas)
# imprime o maior elemento
print("6. O maior elemento:", maior)
print('---------------------------------------------------------------------------------------')
# calcula o menor elemento
menor = min(notas)
# imprime o menor elemento
print("7. O menor elemento:", menor)
print('---------------------------------------------------------------------------------------')
# calcula a média das notas
media = soma / len(notas)
# imprime a média das notas
print("8. Média dos elementos:", media)
print('---------------------------------------------------------------------------------------')
# conta quantas notas estão acima da média
contador = 0
for i in range(len(notas)):
    if notas[i] > media:
        contador += 1

# imprime o número de notas acima da média
print("Número de notas acima da média:", contador)
print()
# imprime as notas acima da média
if contador > 0:
    print("9. Notas acima da média:")
    for i in range(len(notas)):
        if notas[i] > media:
            print(notas[i])
print('---------------------------------------------------------------------------------------')
# conta quantas notas estão abaixo de 9.5
contador_abaixo = 0
notas_abaixo = []
for nota in notas:
    if nota < 9.5:
        contador_abaixo += 1
        if contador_abaixo > 0:
            notas_abaixo.append(nota)
# imprime o resultado
print("Quantidade de notas abaixo de 9.5:", contador_abaixo)
print()
print("10. Elementos negativos:", notas_abaixo)