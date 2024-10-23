from Elemento import Elemento
from NoABB import NoABB
from ArvoreBB import ArvoreBB 

arv = ArvoreBB()
c = int(input("Chave [-1 para terminar]: "))
while c != -1:
  n = input("Nome: ")
  ele = Elemento(c, n)
  no = NoABB(ele)
  arv.insere(no)
  print("Arvore em ordem \n")
  arv.emOrdem(arv.getRaiz())
  c = int(input("Chave [-1 para terminar]: "))
print("fim")