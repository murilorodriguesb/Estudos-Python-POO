# EXERCÍCIO 1 - VALIDAR SENHA

# senha = int(input("Qual é a senha?"))

# while senha < 0 or senha > 10:
#     senha = int(input("Qual é a senha?: "))


# EXERCÍCIO 2 - VALIDAR NOME E SENHA

# while True:
#     nome = str(input("Qual é o nome?"))
#     senha = str(input("Qual é a senha?"))

#     if nome != senha:
#         print("Pode continuar!")
#         break
#     else:
#         print("sua senha nao pode ser igual ao seu nome")
#         continue


# EXERCÍCIO 3 - VALIDAR DADOS PESSOAIS

# nome = str(input("Qual é o seu nome?: "))
# idade = int(input("Sua idade?: "))
# salario = int(input("Seu salario?: "))
# estado = str(input("Qual é seu estado civil?: "))

# quant = len(nome) - nome.count(" ")

# n = "Nome confere" if quant > 3 else "Nome não confere"
# i = "Idade confere" if idade in range(0, 150) else "Idade não confere"
# s = "Salario confere" if salario > 0 else "Salario não confere"
# e = "Estado civil confere" if estado in ('s', 'c', 'v', 'd') else "Estado civil não confere"

# print(f"{n} \n{i} \n{s} \n{e}")


# EXERCÍCIO 4 - CRESCIMENTO DE POPULAÇÃO

# cidadeA = 80000
# cidadeB = 200000
# anos = 0

# while cidadeA < cidadeB:
#     cidadeA *= 1.03
#     cidadeB *= 1.015
#     anos += 1

# print(f"{anos} anos")


# EXERCÍCIO 5 - LISTAR NÚMEROS DE 1 A 20

# i = 1
# lista = []

# while i <= 20:
#     lista.append(i)
#     i += 1

# print(" ".join(map(str, lista)))


# EXERCÍCIO 6 - VALIDAR QUANTIDADE DE NÚMEROS

# while True:
#     numeros = list(map(int, input("Qual é o numero? ").split()))

#     if(len(numeros) != 5):
#         print("digite 5 numeros!")
#         print(f"voce digitou {len(numeros)} e não 5")
#     else:
#         maior = max(numeros)
#         print(maior)
#         break


# EXERCÍCIO 7 - NÚMEROS ÍMPARES DE 1 A 50

# numeros = list((range(1, 50, 2)))
# print(" ".join(map(str, (numeros))))


# EXERCÍCIO 8 - NÚMEROS PARES DE 0 A 49

# numeros = []
# i = 0

# while i < 50:
#     if i % 2 == 0:
#         numeros.append(i)
#     i += 1

# print(" ".join(map(str, (numeros))))


# EXERCÍCIO 9 - INTERVALO ENTRE DOIS NÚMEROS

# num = input()
# partes = num.split()

# num = []

# for parte in partes:
#     num.append(int(parte))

# print(num)

# intervalo = list(range(min(num), max(num) + 1))

# print(" ".join(map(str, (intervalo)))


# EXERCÍCIO 10 - SOMAR NÚMEROS

# num = list(map(int, input("Quais são os numeros?: ").split()))
# soma = 0

# for i in num:
#     soma += i

# print(soma)


# EXERCÍCIO 11 - TABUADA

# numero = int(input("Qual é o numero?: "))
# i = 1

# while i <= 10:
#     print(f"{numero} X {i} = {numero * i}")
#     i += 1


# EXERCÍCIO 12 - CONTAR PARES E ÍMPARES

# numeros = list(map(int, input("Quais sao os numeros? ").split()))

# i = 0
# par = 0
# impar = 0

# while i < 10:
#     if numeros[i] % 2 == 0:
#         par += 1
#     else:
#         impar += 1

#     i += 1

# print(f"{par} {impar}")


# EXERCÍCIO 13 - SEQUÊNCIA DE FIBONACCI

# termo = int(input("Qual é o termo?: "))

# atual = 1
# anterior = 0
# aux = 0
# i = 0

# while i < termo:
#     if i != 1:
#         aux = atual
#         atual = atual + anterior
#         anterior = aux
#     i += 1

# print(atual)


# EXERCÍCIO 14 - FATORIAL

# numero = int(input("Qual é o numero?: "))
# lista = list(range(1, numero + 1))
# ordem = list(sorted(lista, reverse=True))
# i = 1
# resultado = 1

# while i <= numero:
#     resultado = resultado * i
#     i += 1

# print(f"{numero}! = {".".join(map(str, (ordem)))} = {resultado}")

# sorted serve para organizar a lista de maior para menor


# EXERCÍCIO 15 - ESTATÍSTICAS DE UMA LISTA

# conjunto = list(map(int, input("Qual é os numeros?: ").split()))
# quant = len(conjunto)
# minimo = min(conjunto)
# maximo = max(conjunto)
# i = 0
# soma = 0

# while i < quant:
#     soma += conjunto[i]
#     i += 1

# print(f"{quant} {minimo} {maximo} {soma}")


# EXERCÍCIO 16 - VERIFICAR NÚMERO PRIMO

# numero = int(input("Qual é o numero?: "))
# primo = 0
# divisores = []

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         primo += 1
#         divisores.append(i)

# if primo == 2:
#     print("primo")
# else:
#     print("não primo")
#     print(" ".join(map(str , divisores)))


# EXERCÍCIO 17 - ENCONTRAR NÚMEROS PRIMOS

# numero = int(input("Qual é o numero? "))

# divisoes = 0
# cont = 0

# for i in range(1, numero + 1):
#     cont = 0

#     for j in range (1, i + 1):
#         divisoes += 1

#         if i % j == 0:
#             cont += 1

#     if cont == 2:
#         print(i)

# print(divisoes)


# EXERCÍCIO 18 - MÉDIA DAS NOTAS

# notas = list(map(int, input("qual é as notas? ").split()))
# quant = len(notas)

# media = 0 

# for i in range(0, quant):
#     media += notas[i]

# media = media / quant
# print(media)


# EXERCÍCIO 19 - CLASSIFICAR MÉDIA DE IDADES

# idades = list(map(int , input("Qual é as idades? ").split()))

# soma = 0

# for idade in idades:
#     soma += idade

# media = soma // len(idades)

# if media < 26:
#     print ("novo")
# elif media < 61:
#     print("meia idade")
# else:
#     print("véi")


# EXERCÍCIO 20 - CONTAR VOTOS

# eleitores = int(input("Qual é o numero total de eleitores?: "))
# um = 0
# dois = 0
# tres = 0   

# for i in range(0, eleitores):
#     voto = int(input("Qual candidato?: "))

#     if voto == 1:
#         um += 1
#     elif voto == 2:
#         dois += 1
#     elif voto == 3:
#         tres += 1

# vencedor = max(um, dois, tres)
# print(f"candidato {vencedor}")


# EXERCÍCIO 21 - MÉDIA DE ALUNOS POR TURMA

# turmas = int(input("Quantidade de turmas? "))

# media = 0

# for i in range(0, turmas):
#     alunos = int(input("quantidade alunos: "))

#     if alunos > 40:
#         while alunos > 40:
#             print("uma turma nao pode ter mais de 40 alunos")
#             alunos = int(input("quantidade alunos: "))

#     media += alunos

# media = media // turmas
# print(f"a media é {media}")


# EXERCÍCIO 22 - FATORIAL

# numero = int(input("qual é o numero?: "))
# lista = list(range(1, numero + 1))
# ordem = sorted(lista, reverse=True)

# valor = 1

# for i in lista:
#     valor *= i
    
# print(f"{numero}! = {".".join(map(str, ordem))} = {valor}")


# EXERCÍCIO 23 - DADOS DE PESSOAS

# codigo = []
# altura = []
# peso = []
# encerrar = 1

# while encerrar != 0:
#     codigo.append(int(input("qual é o seu codigo?")))
#     altura.append(float(input("qual é a sua altura?")))
#     peso.append(float(input("qual é o seu peso?")))
#     encerrar = int(input("deseja encerrar 0 = sim! "))

# mediaaltura = 0
# mediapeso = 0
# tam = len(codigo)

# for i in range(tam):
#     mediaaltura += altura[i] 
#     mediapeso += peso[i]

# mediaaltura = mediaaltura / tam
# mediapeso = mediapeso / tam

# maiorp = 0
# menorp = peso[0]
# maiora = 0
# menora = altura[0]
# v1 = 0
# v2 = 0
# v3 = 0
# v4 = 0

# for j in range(tam):
#     if peso[j] > maiorp:
#         maiorp = peso[j]
#         v1 = j

#     if peso[j] < menorp:
#         menorp = peso[j]
#         v2 = j

#     if altura[j] > maiora:
#         maiora = altura[j]
#         v3 = j

#     if altura[j] < menora:
#         menora = altura[j]
#         v4 = j

# print(f"maior peso: {maiorp} pessoa codigo: {codigo[v1]}")
# print(f"menor peso: {menorp} pessoa codigo: {codigo[v2]}")
# print(f"maior altura: {maiora} pessoa codigo: {codigo[v3]}")
# print(f"menor peso: {menora} pessoa codigo: {codigo[v4]}")
# print(f"media peso: {mediapeso}")
# print(f"media altura: {mediaaltura}")


# EXERCÍCIO 24 - MAIOR E MENOR ALTURA

# alunos = []

# for i in range(10):
#     numero = int(input("qual é o seu numero? "))
#     altura = int(input("qual é a sua altura? "))
    
#     alunos.append([numero, altura])

# menor = maior = alunos[0][1]
# imenor = imaior = 0

# for j in range(10):
#     if alunos[j][1] > maior:
#         maior = alunos[j][1]
#         imaior = j

#     if alunos[j][1] < menor:
#         menor = alunos[j][1]
#         imenor = j

# print(f"o aluno maior é o de numero {alunos[imaior][0]} com {maior} cm de altura")
# print(f"o aluno de menor altura é o de numero {alunos[imenor][0]} com {menor} cm de {menor}")


# O QUE EU APRENDI

# while True cria um loop que continua até receber um break.
# break encerra o loop
# count()conta quantas vezes um valor aparece.
# max() - retorna o maior valor.
# min() retorna o menor valor.
# sorted() organiza os valores de uma lista.
# range(início, fim, passo) cria uma sequência com intervalo definido.