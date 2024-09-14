from Elemento import Elemento
from No import No
class Lista:
  def __init__(self):
    elemento = Elemento()
    no = No(elemento)
    self.__cabeca = no
  def getCabeca(self):
    return self.__cabeca
  def setCabeca(self, c):
    self.__cabeca = c
  def listaVazia(self):
    return self.getCabeca().getProximo() == None
  def insereNoInicio(self, v):
    v.setProximo(self.getCabeca().getProximo())
    self.getCabeca().setProximo(v)
  def retiraNoInicio(self):
    ret = None
    if not self.listaVazia():
      ret = self.getCabeca().getProximo()
      self.getCabeca().setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret
  def insereNoFim(self, v):
    aux = self.getCabeca()
    while aux.getProximo() != None:
      aux = aux.getProximo()
    aux.setProximo(v)
  def retiraNoFim(self):
    ret = None
    if not self.listaVazia():
      aux = self.getCabeca()
      ret = aux.getProximo()
      while ret.getProximo() != None:
        aux = ret
        ret = aux.getProximo()
      aux.setProximo(None)
    return ret
  def insereNaOrdem(self, v):
    anterior = self.getCabeca()
    atual = anterior.getProximo()
    while atual != None and atual.getElemento().getChave() < v.getElemento().getChave():
      anterior = atual
      atual = anterior.getProximo()
    v.setProximo(atual)
    anterior.setProximo(v)
  def retiraChave(self, c):
    ret = None
    if not self.listaVazia():
      anterior = self.getCabeca()
      ret = anterior.getProximo()
      while ret != None and ret.getElemento().getChave() != c:
        anterior = ret
        ret = anterior.getProximo()
      if ret != None:
        anterior.setProximo(ret.getProximo())
        ret.setProximo(None)
    return ret
  def mostraLista(self):
    atual = self.getCabeca().getProximo()
    while atual != None:
      print(atual.getElemento().getValores())
      atual = atual.getProximo()
  