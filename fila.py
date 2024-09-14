class Fila:
  def __init__(self):
    self.__fila = []
  def filaVazia(self):
    return len(self.__fila) == 0
  def enQueue(self, valor):
    self.__fila.append(valor)
  def deQueue(self):
    if not self.filaVazia():
      return self.__fila.pop(0)
    return None
  
