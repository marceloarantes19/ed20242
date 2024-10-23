from Elemento import Elemento
class NoABB:
  def __init__(self, elemento = None):
    self.__fe = None
    self.__fd = None
    self.__dado = elemento
  def getFe(self):
    return self.__fe
  def setFe(self, no):
    self.__fe = no
  def getFd(self):
    return self.__fd
  def setFd(self, no):
    self.__fd = no
  def getDado(self):
    return self.__dado
  def getChave(self):
    return self.getDado().getChave()
  def getValores(self):
    return self.getDado().getValores()
  def eFolha(self):
    return self.getFe() == None and self.getFd() == None
  def temDoisFilhos(self):
    return self.getFe() != None and self.getFd() != None
  def soTemFe(self):
    return self.getFe() != None and self.getFd() == None
  def soTemFd(self):
    return self.getFe() == None and self.getFd() != None
  def eFeDe(self, pai):
    return pai.getFe() == self
  def eFdDe(self, pai):
    return pai.getFd() == self
  


