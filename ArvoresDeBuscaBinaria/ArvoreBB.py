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
  def remove(self, v):
    return self.removeCasos(None, self.getRaiz(), v)
  
  def removeCasos(self, pai, atual, v):
    if atual == None: # Valor não encontrado
      return None
    elif v < atual.getChave():
      return self.removeCasos(atual, atual.getFe(), v)
    elif v > atual.getChave():
      return self.removeCasos(atual, atual.getFd(), v)
    else:
      # Se o nó a remover é folha
      if not atual.temDoisFilhos():
        return self.fazRemocao(pai, atual)
      else:
        return self.removeNaoTrivial(atual, atual, atual.getFe())
      
  def fazRemocao(self, pai, atual):
    if atual.eFolha():
      if atual == self.getRaiz():
        self.setRaiz(None)
      elif atual.eFeDe(pai):
        pai.setFe(None)
      else:
        pai.setFd(None)
    elif atual.soTemFe():
      if atual == self.getRaiz():
        self.setRaiz(atual.getFe())
      elif atual.eFeDe(pai):
        pai.setFe(atual.getFe())
      else:
        pai.setFd(atual.getFe())
      atual.setFe(None)
    else:
      if atual == self.getRaiz():
        self.setRaiz(atual.getFd())
      elif atual.eFeDe(pai):
        pai.setFe(atual.getFd())
      else:
        pai.setFd(atual.getFd())
      atual.setFd(None)
    return atual
    
  def removeNaoTrivial(self, fixo, pai, atual):
    if atual.getFd() != None:
      return self.removeNaoTrivial(fixo, atual, atual.getFd())
    else:
      x = fixo.getDado()
      fixo.setDado(atual.getDado())
      atual.setDado(x)
      return self.fazRemocao(pai, atual)

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

# Correção dos Exercicios Abaixo
  # Letra a 
  def invertido(self, no):
    if no != None:
      self.invertido(no.getFd())
      print(no.getValores())
      self.invertido(no.getFe())
  
  # Letra b
  def buscaNo(self, no, v):
    if no == None:
      return False
    elif v < no.getChave():
      return self.buscaNo(no.getFe(), v)
    elif v > no.getChave():
      return self.buscaNo(no.getFd(), v)
    else:
      return True
  
  # Letra C
  def quantidade(self, no):
    if no == None:
      return 0
    else:
      return 1 + self.quantidade(no.getFe()) + self.quantidade(no.getFd())

  # Letra C
  def soma(self, no):
    if no == None:
      return 0
    else:
      return no.getChave() + self.soma(no.getFe()) + self.soma(no.getFd())
  
  # Letra E
  def menor(self, no):
    if no.getFe() != None:
      return self.menor(no.getFe())
    return no.getChave()

  # Letra F
  def maior(self, no):
    if no.getFd() != None:
      return self.maior(no.getFd())
    return no.getChave()

  # Letra g
  def mostraPorNivel(self):
    fila = []
    nvl = []
    fila.append(self.getRaiz())
    nvl.append(0)
    while len(fila) > 0:
      x = fila.pop(0)
      y = nvl.pop(0)
      print(x.getValores(), ' Nivel ', y)
      if x.getFe() != None:
        fila.append(x.getFe())
        nvl.append(y+1)
      if x.getFd() != None:
        fila.append(x.getFd())
        nvl.append(y+1)
