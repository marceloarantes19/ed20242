from Elemento import Elemento
from NoABB import NoABB
from ArvoreBB import ArvoreBB 
x = [8,3,14,1,5,12,16,0,2,4,7,10,13,15,20]
arv = ArvoreBB()
for i in x:
  ele = Elemento(i, str(i))
  no = NoABB(ele)
  arv.insere(no)
print("Arvore em ordem \n")
arv.posOrdem(arv.getRaiz())
print("fim")