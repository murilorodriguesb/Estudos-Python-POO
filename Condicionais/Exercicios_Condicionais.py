# EXERCÍCIO 01 - ENCONTRAR O MAIOR NÚMERO


# numeros = map(int, input("Quais são os numeros?: ").split())
# maior = max(numeros)
# print(maior)



# EXERCÍCIO 02 - ORDENAR NÚMEROS COM SORTED

# numeros = map(int, input("Quais são os numeros para ordem?: ").split())
# ordem = sorted(numeros, reverse=False)
# print(ordem)



# EXERCÍCIO 03 - ORDENAR LISTA COM SORT

# numeros = list(map(int, input("Quais são os numeros para ordem?: ").split()))
# numeros.sort()
# print(numeros)



# EXERCÍCIO 04 - MÉDIA E CONCEITO

# notas = list(map(float, input("Quais são as notas?: ").split()))
# media = (notas[0] + notas[1]) / 2
# if media >= 9.0:
#     print("Aprovado por conceito A")
# elif media >= 7.5:
#     print("Aprovado por conceito B")
# elif media >= 6.0:
#     print("Aprovado por conceito C")
# elif media >= 4.0:
#     print("Reprovado por conceito D")
# else:
#     print("Reprovado por conceito E")



# EXERCÍCIO 05 - EQUAÇÃO DE SEGUNDO GRAU

# import math

# valores = list(map(float, input("Quais são os valores?: ").split()))
# if valores[0] == 0:
#     print("Se trata de uma equação de 1 grau!")
# else:
#     delta = (valores[1] ** 2) - 4 * valores[0] * valores[2]
#     if delta < 0:
#         print("O delta é negativo, portanto nao existe raizes!")
#     elif delta == 0:
#         print("So existe uma raiz")
#         raiz1 = -valores[1] / (2 * valores[0])
#         print(raiz1)
#     else:
#         raizdelta = math.sqrt(delta)
#         raiz1 = (-valores[1] + raizdelta) / (2 * valores[0])
#         raiz2 = (-valores[1] - raizdelta) / (2 * valores[0])
#         print(f"Possui duas raizes: {raiz1} {raiz2}")



# EXERCÍCIO 06 - VERIFICAR ANO BISSEXTO

# ano = int(input("Qual é o ano?: "))
# if ano % 100 == 0:
#     if ano % 4 == 0 and ano % 400 == 0:
#         print("bissexto")
#     else:
#         print("não bissexto")
# elif ano % 4 == 0:
#     print("bissexto")
# else:
#     print("não bissexto")



# EXERCÍCIO 07 - VALIDAR UMA DATA

# data = input("Qual é a data?: ").replace("/", " ")
# dia, mes, ano = map(int, data.split())

# if (mes > 12 or mes <= 0) or (ano < 0) or (dia > 31 or dia <= 0):
#     print("Não existe")

# else:
#     bissexto = 0
#     if ano % 100 == 0:
#         if ano % 4 == 0 and ano % 400 == 0:
#             bissexto = 1
#     elif ano % 4 == 0:
#         bissexto = 1

#     if mes in (1, 3, 5, 7, 8, 10, 12):
#         if dia <= 31:
#             print("Existe")
#         elif dia <= 0 or dia > 31:
#             print("Não existe")
#     elif mes == 2:
#         if dia <= 29 and bissexto == 1:
#             print("Existe")
#         elif dia <= 28:
#             print("Existe")
#         elif dia <= 0 or dia >= 29:
#             print("Não existe")
#     else:
#         if dia <= 30:
#             print("Existe")
#         elif dia <= 0 or dia >= 31:
#             print("Não existe")



# EXERCÍCIO 08 - CENTENA, DEZENA E UNIDADE

# numero = list(input("Quais os numeros? ").strip(" "))
# numero = list(map(int, numero))
# centena, dezena, unidade = numero

# c = "centena" if centena == 1 else "centenas"
# d = "dezena" if dezena == 1 else "dezenas"
# u = "unidade" if unidade == 1 else "unidades"

# print(f"{centena} {c}, {dezena} {d}, {unidade} {u}")



# EXERCÍCIO 09 - CAIXA ELETRÔNICO

# dinheiro = int(input("Qual é a quantidade do saque?: "))

# cem = dinheiro // 100
# dinheiro %= 100

# cinquenta = dinheiro // 50
# dinheiro %= 50

# vinte = dinheiro // 20
# dinheiro %= 20

# dez = dinheiro // 10
# dinheiro %= 10

# cinco = dinheiro // 5
# dinheiro %= 5

# um = dinheiro

# c = "nota de 100" if cem == 1 else "notas de 100"
# cin = "nota de 50" if cinquenta == 1 else "notas de 50"
# v = "nota de 20" if vinte == 1 else "notas de 20"
# d = "nota de 10" if dez == 1 else "notas de 10"
# c5 = "nota de 5" if cinco == 1 else "notas de 5"
# u = "moeda de 1" if um == 1 else "moedas de 1"

# if cem > 0:
#     print(f"{cem} {c}")
# if cinquenta > 0:
#     print(f"{cinquenta} {cin}")
# if vinte > 0:
#     print(f"{vinte} {v}")
# if dez > 0:
#     print(f"{dez} {d}")
# if cinco > 0:
#     print(f"{cinco} {c5}")
# if um > 0:
#     print(f"{um} {u}")



# EXERCÍCIO 10 - PAR OU ÍMPAR

# numero = int(input("Qual é o numero?: "))
# if numero % 2 == 0:
#     print("par")
# else:
#     print("impar")



# EXERCÍCIO 11 - INTEIRO OU DECIMAL

# numero = float(input())
# if numero == round(numero):
#     print("inteiro")
# else:
#     print("decimal")

# round serve para arredondar
# numero = 3.91867
# print(round(numero, 3))



# EXERCÍCIO 12 - CALCULADORA E CLASSIFICAÇÃO

# numeros = list(map(float, input("Quais sao os numeros?: ").split()))
# operacao = str(input("Qual é a operação?: "))

# if operacao == '+':
#     resultado = numeros[0] + numeros[1]
# elif operacao == '-':
#     resultado = numeros[0] - numeros[1]
# elif operacao == '*':
#     resultado = numeros[0] * numeros[1]
# elif operacao == '/':
#     resultado = numeros[0] / numeros[1]

# par = "par" if resultado % 2 == 0 else "impar"
# pos = "positivo" if resultado >= 0 else "negativo"
# dec = "inteiro" if resultado == round(resultado) else "decimal"

# print(f"o resultado é {resultado} e esse numero é: {par}, {pos}, {dec}")


# ==========================================
# O QUE EU APRENDI
# ==========================================

# .strip() serve para tirar algum caractere da entrada.
# .split() separa strings por espaços.
# map() transforma os valores em inteiros ou outros tipos.
# list() transforma os valores em uma lista.
# sorted() organiza os valores em ordem crescente por padrão.
# reverse=False do menor para o maior.
# reverse=True do maior para o menor.
# round() arredonda.