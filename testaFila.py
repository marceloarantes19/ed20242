from fila import Fila
f = Fila()
nome = input("Digite um nome: ")
for i in nome:
  f.enQueue(i)

while not f.filaVazia():
  print(f.deQueue())
 