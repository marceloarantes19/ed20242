class ArvoreBB:
  def __init__(self):
    self.__raiz = None
  def getRaiz(self):
    return self.__raiz
  def setRaiz(self, no):
    self.__raiz = no
  def arvoreVazia(self):
    return self.getRaiz() == None 
  def insere(self, no):
    if self.arvoreVazia():
      self.setRaiz(no)
    else:
      self.insereNo(None, self.getRaiz(), no)
  def insereNo(self, pai, atual, no):
    if atual == None:
      if no.getChave() < pai.getChave():
        pai.setFe(no)
      else:
        pai.setFd(no)
    elif no.getChave() < atual.getChave():
      self.insereNo(atual, atual.getFe(), no)
    else:
      self.insereNo(atual, atual.getFd(), no)  

#
# Reservado ara a remocao de nos
#

  def emOrdem(self, no):
    if no != None:
      self.emOrdem(no.getFe())
      print(no.getValores())
      self.emOrdem(no.getFd())
  def preOrdem(self, no):
    if no != None:
      print(no.getValores())
      self.preOrdem(no.getFe())
      self.preOrdem(no.getFd())
  def posOrdem(self, no):
    if no != None:
      self.posOrdem(no.getFe())
      self.posOrdem(no.getFd())
      print(no.getValores())

# Insiram os Exercicios Abaixo
