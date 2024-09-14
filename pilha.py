class Pilha:
  def __init__(self):
    self.__pilha = []
  def pilhaVazia(self):
    return len(self.__pilha) == 0
  def push(self, valor):
    self.__pilha.append(valor)
  def pop(self):
    if not self.pilhaVazia():
      return self.__pilha.pop()
    return None
  