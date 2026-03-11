nome = input("escreva o seu nome: ")
nota1 = float(input("escreva a nota da primeira prova: "))
nota2 = float(input("escreva a nota da segunda prova "))

aluno = {
    "nome": nome,
    "nota1": nota1,
    "nota2": nota2
}

media = (nota1 + nota2) / 2
aluno["media"] = media

if media >= 7:
    aluno["situacao"] = "Aprovado"
elif 5 <= media < 7:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"

print("\n Boletim do Aluno ")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")