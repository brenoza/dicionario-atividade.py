#

matricula1 = 2026001
nome1 = "Ana Silva"
telefone = "9999-8888"

aluno = {
    "matricula": 2026001
    "nome": "Ana Silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruno": "Bruna",
    "@joão": "joão",
}

print(contato)
print(type(contato))

print(contato["@camila"])

print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

print("Original: ", contato)

contato["@giovana"] = "Giovana"
print("Após add: ", contato)

contato["@paola"] = "Paola Oliveira"
print("Após add: ", contato)

contato.update(
    {
        "@bruna": "Bruna Marquezine",
        "@camila": "Camila Q."
    }
)

print("Após atualização:", contato)

removido = contato.pop("@sheron")
print(f"Removido: {removido}")
print("Após o pop: ", contato)


del contato["@paola"]
print("Após o del: ", contato)


copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia: ", copia)

print("Número de contato: ", len(contato))

contato.pop("@camila")
print("Apos remover um: ", len(contato))

if "@joao" in contato:
    print(f"Encontrado: {contato['@joao']}")

if "@inexistente" in contato:
    print("Existe")

else:
    print("Não existe. ")

vazio = {}


dados = {
    "nome": "João",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
}

print

("Vazio: ", vazio)
print("Vazio: ", dados)


