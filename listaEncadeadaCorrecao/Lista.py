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
  def getPrimeiroElemento(self):
    return self.getCabeca().getProximo()
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
  # Exercício 9
  def insereNaOrdem(self, v):
    anterior = self.getCabeca()
    atual = anterior.getProximo()
    while atual != None and atual.getElemento().getChave() < v.getElemento().getChave():
      anterior = atual
      atual = anterior.getProximo()
    v.setProximo(atual)
    anterior.setProximo(v)
  # Exercício 10
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

# Correção dos Exercícios
  # Exercício 3 - Quantidade de elementos na lista
  def quantidadeDeElementos(self):
    ret = 0
    aux = self.getCabeca().getProximo()
    while aux != None:
      ret = ret + 1
      aux = aux.getProximo()
    return ret
  
  # Exercício 4 - Recursivo para mostrar todos os elementos da lista
  def mostraRecursivo(self, n):
    if n != None:
      print(n.getElemento().getValores())
      self.mostraRecursivo(n.getProximo())
  
  # Exercício 5 - Recursivo para mostrar a lista invertida
  def mostraInvertido(self, n):
    if n != None:
      self.mostraInvertido(n.getProximo())
      print(n.getElemento().getValores())
  
  # Exercício 6 - Inserir na posição
  def insereNaPosicao(self, n, p):
    if p > 0 and p <= self.quantidadeDeElementos()+1:
      ant = self.getCabeca()
      atu = self.getPrimeiroElemento()
      i = 1
      while i < p and atu != None:
        i = i + 1
        ant = atu
        atu = ant.getProximo()
      n.setProximo(atu)
      ant.setProximo(n)

  # Exercício 7 - Retira na posição
  def retiraNaPosicao(self, p):
    ret = None
    if p > 0 and p <= self.quantidadeDeElementos():
      ant = self.getCabeca()
      ret = self.getPrimeiroElemento()
      i = 1
      while i < p:
        i = i + 1
        ant = ret
        ret = ant.getProximo()
      ant.setProximo(ret.getProximo())
      ret.setProximo(None)
    return ret

  def limpaLista1(self):
    ret = None
    while not self.listaVazia():
      ret = self.retiraNaPosicao(1)
  
  def limpaRec(self, n):
    if n != None:
      self.limpaRec(n.getProximo())
      n.setProximo(None)