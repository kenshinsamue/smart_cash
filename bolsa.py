import indices as indeces

class Bolsa :

  def __init__(self):
    self.indices = []
    pass

  def loadIndexes(self):
    with open ('./bolsa/indices.txt','r') as fichero :
      index = fichero.read()
      self.indices.append(indeces.Index('^'+index))
    
    for bolsa in self.indices :
      with open ('./bolsa/'+bolsa.getName()+".txt") as fichero:
        bolsa.addTicker(fichero.read())

  def saveHistoricData(self):
    for indice in self.indices :
      history = indice.getHistotyInfo()
      indice.exportToCSV('./dato/bolsas/'+indice.getName()+"/history",history)
    
