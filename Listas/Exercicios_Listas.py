# EXERCÍCIO 1 - INVERTER NÚMEROS

# numeros = list(str(input("qual é os numeros? ")))
# numeros.reverse()
# print("".join(map(str, numeros)))



# EXERCÍCIO 2 - MÉDIA DAS NOTAS

# notas = list(map(int, input("quais são as notas?: ").split()))
# soma = 0

# for media in notas:
#     soma += media

# print(f"a média é: {soma / len(notas)}")



# EXERCÍCIO 3 - CONTAR CONSOANTES

# vetor = list(input("qual sao as letras? "))
# consoantes = 0
# listaconso = []

# for i in range(len(vetor)):
#     if vetor[i] in ('a', 'e', 'i', 'o', 'u'):
#         continue
#     else:
#         consoantes += 1
#         listaconso.append(vetor[i])

# print(f"{consoantes} é a quantidade de consoantes e essas são as consoantes: {listaconso}")



# EXERCÍCIO 4 - SEPARAR NÚMEROS PARES E ÍMPARES

# numeros = list(map(int, input("quais são os numeros?: ")))
# par = []
# impar = []

# for num in numeros:
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)

# print(f"{numeros} \n{par} \n{impar}")



# EXERCÍCIO 5 - MÉDIA DOS ALUNOS APROVADOS

# notas = []
# i = 0

# while i < 4:
#     nota = list(map(float, (input("quais sao as notas?: ").split())))
#     notas.append(nota)
#     i += 1

# aprovado = []
# soma = 0

# for k in range(len(notas)):
#     media = 0
#     j = 0
#     soma = 0

#     while j < 4:
#         soma += notas[k][j]
#         j += 1

#     media = soma / 4

#     if media >= 7:
#         aprovado.append(media)

# print(aprovado)



# EXERCÍCIO 6 - SOMA E MULTIPLICAÇÃO DE NÚMEROS

# numeros = []
# i = 0

# while i < 5:
#     num = int(input("quais sao os numeros?: "))
#     numeros.append(num)
#     i += 1

# soma = sum(numeros)
# multiplicacao = 1

# for mult in numeros:
#     multiplicacao *= mult

# print(soma)
# print(multiplicacao)



# EXERCÍCIO 7 - INVERTER ORDEM DE IDADE E ALTURA

# ordem = []
# i = 0

# while i < 5:
#     idade = float(input("qual é a sua idade?: "))
#     altura = float(input("qual é a sua altura?: "))
#     ordem.append([idade, altura])
#     i += 1

# ordem.reverse()
# print(ordem)



# EXERCÍCIO 8 - INTERCALAR SEQUÊNCIAS

# ordem = []
# i = 0

# while i < 3:
#     seq = list(input("qual é a sequencia?: ").split())
#     ordem.append(seq)
#     i += 1

# intercalado = []
# j = 0

# while j < 10:
#     intercalado.append(ordem[0][j])
#     intercalado.append(ordem[1][j])
#     intercalado.append(ordem[2][j])
#     j += 1

# print(intercalado)



# EXERCÍCIO 9 - ALUNOS ABAIXO DA MÉDIA DE ALTURA

# alunos = []
# i = 0

# while i < 3:
#     idade = float(input("qual é a sua idade?: "))
#     altura = float(input("qual é a sua altura?: "))
#     alunos.append([idade, altura])
#     i += 1

# media_altura = 0

# for j in range(len(alunos)):
#     media_altura += alunos[j][1]

# media_altura /= 3
# soma = 0

# for j in range(len(alunos)):
#     if alunos[j][0] > 13 and alunos[j][1] < media_altura:
#         soma += 1

# print(soma)

# ==========================================
# O QUE EU APRENDI
# ==========================================

# list()transforma um valor em lista.
# reverse() inverte um numero
# join() junta elementos em um texto.
# len() mostra a quantidade de elementos.
# sum()  soma os valores de uma lista.
# continue - pula a repetição atual do loop.
# range() - cria uma sequência de números.