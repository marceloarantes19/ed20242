from Elemento import Elemento
from No import No
from pilhaEncadeada import pilhaEncadeada

p = pilhaEncadeada()
nome = input("Digite um nome: ")
for i in nome:
  e = Elemento()
  e.setNome(i)
  n = No(e)
  p.push(n)

while not p.pilhaVazia():
  print(p.pop().getElemento().getNome())

