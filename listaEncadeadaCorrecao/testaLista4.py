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
  pos = int(input("Posição: "))
  l.insereNaPosicao(n, pos)
  l.mostraRecursivo(l.getPrimeiroElemento())
  print("Elementos na lista: ", l.quantidadeDeElementos())
  chave = int(input("Digite uma chave [-1 para sair]: "))

pos = int(input("Digite uma posicao para retirar [-1 para sair]: "))
while pos != -1 and not l.listaVazia():
  n = l.retiraNaPosicao(pos)
  if n != None:
    print(n.getElemento().getValores())
  else:
    print("Nó não encontrado!")
  l.mostraRecursivo(l.getPrimeiroElemento())
  pos = int(input("Digite uma posicao para retirar [-1 para sair]: "))


