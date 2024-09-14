from pilha import Pilha
p = Pilha()
nome = input("Digite um nome: ")
for i in nome:
  p.push(i)

nome = ""
while not p.pilhaVazia():
  nome = nome + p.pop()

print(nome)

