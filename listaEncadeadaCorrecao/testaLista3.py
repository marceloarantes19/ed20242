from Elemento import Elemento
from No import No 
from Lista import Lista
l = Lista()
chave = int(input("Digite uma chave [-1 para sair]: "))
while chave != -1:
  nome = input("Digite um nome: ")
  e = Elemento(chave)
  e.setNome(nome)
  n = No(e)
  l.insereNaOrdem(n)
  l.mostraInvertido(l.getPrimeiroElemento())
  print("Elementos na lista: ", l.quantidadeDeElementos())
  chave = int(input("Digite uma chave [-1 para sair]: "))

chave = int(input("Digite uma chave para retirar [-1 para sair]: "))
while chave != -1 and not l.listaVazia():
  n = l.retiraChave(chave)
  if n != None:
    print(n.getElemento().getValores())
  else:
    print("Chave não encontrada!")
  chave = int(input("Digite uma chave para retirar [-1 para sair]: "))


