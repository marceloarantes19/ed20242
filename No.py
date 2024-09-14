class No:
  def __init__(self, ele = None):
    self.__elemento = ele
    self.__proximo  = None
  def setElemento(self, e):
    self.__elemento = e
  def getElemento(self):
    return self.__elemento
  def setProximo(self, p):
    self.__proximo = p
  def getProximo(self):
    return self.__proximo
