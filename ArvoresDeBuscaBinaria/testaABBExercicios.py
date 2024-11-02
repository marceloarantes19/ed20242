from Elemento import Elemento
from NoABB import NoABB
from ArvoreBB import ArvoreBB 
x = [10, 5, 15, 3, 9, 12, 17, 4, 7, 11]
arv = ArvoreBB()
for i in x:
  ele = Elemento(i, str(i))
  no = NoABB(ele)
  arv.insere(no)

print("Arvore em Ordem")
arv.emOrdem(arv.getRaiz())

#print("\nArvore em Inverida")
#arv.invertido(arv.getRaiz())

x = int(input('Digite um valor a procurar na árvore: '))
if arv.buscaNo(arv.getRaiz(), x):
  print('Valor encontrado')
else:
  print('Valor não encontrado')

print("Quantidade de Nós na árvore: ", arv.quantidade(arv.getRaiz()))
print("Soma de chaves na árvore: ", arv.soma(arv.getRaiz()))
print("A menor Chave é: ", arv.menor(arv.getRaiz()))
print("A maior Chave é: ", arv.maior(arv.getRaiz()))
print("Árvore Nível a Nível: ")
arv.mostraPorNivel()
