from Elemento import Elemento
from NoABB import NoABB
from ArvoreBB import ArvoreBB 
x = [10, 5, 15, 3, 9, 12, 17, 4, 7, 11]
arv = ArvoreBB()
for i in x:
  ele = Elemento(i, str(i))
  no = NoABB(ele)
  arv.insere(no)
print("Arvore em ordem \n")
arv.emOrdem(arv.getRaiz())
rm = int(input('Digite a chave a remover [-1 para sair]: '))
while rm != -1:
  no = arv.remove(rm)
  if no != None:
    print(no.getValores(), " Removido! ")
  else:
    print("Nao encontrado!")
  arv.emOrdem(arv.getRaiz())
  rm = int(input('Digite a chave a remover [-1 para sair]: '))
print('Fim')
