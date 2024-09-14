from Elemento import Elemento
from No import No 
from Lista import Lista
l = Lista()
nome = input("Digite um nome: ")
k = 0
for i in nome:
  e = Elemento(k)
  e.setNome(i)
  n = No(e)
  l.insereNoInicio(n)
  k = k + 1

while not l.listaVazia():
  print(l.retiraNoInicio().getElemento().getValores())
