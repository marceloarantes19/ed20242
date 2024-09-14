class Elemento:
  def __init__(self, chave = 0):
    self.__chave = chave
    self.__nome  = ""
  def setChave(self, c):
    self.__chave = c
  def getChave(self):
    return self.__chave
  def setNome(self, n):
    self.__nome = n 
  def getNome(self):
    return self.__nome
  def getValores(self):
    return self.getChave(), self.getNome()