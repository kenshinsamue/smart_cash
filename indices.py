import yfinance as yf
import acciones as acc
import csv
import os

# clase que contiene a los indices generales, ejemplo sp500, ibex35, etc.
class Index :
  # Constructor, se le pasa por parametro el nombre del indice y genera un array que contendra las acciones asociadas
  def __init__(self,name):
    self.name = name
    self.ticker = []
    self.index=yf.Ticker(name)

  def getName(self):
    return self.name
    
  # Metodo que elimina un ticket ya registrado
  def deleteTicker(self,name):
    accionObjectivo = None
    for accion in self.ticker:
      if accion.getName() == name:
        accionObjectivo = accion
    self.ticker.remove(accionObjectivo)

  # Metodo que agrega un nuevo ticket
  def addTicker(self,name):
    accion = acc.Accion(name)
    self.ticker.append(accion)

  # Metodo que retorna la informacion general del indice
  def getGeneralInfo(self):
    return self.index.info
    
  # Metodo que retorna el historial de valores relacionados al indice
  def getHistotyInfo(self):
    return self.index.history()

  # Metodo que guarda la informacion especificada dentro del arbol de directorio 
  def exportToCSV(self,name,data):
    filename = name+'.csv'
    dataHeaders= data.keys()
    dataValues = []
    for header in dataHeaders:
      dataValues.append(data[header])
    try:
      if os.path.exists(filename):
        if os.path.getsize(filename) == 0 or None:
          with open(filename,'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(dataHeaders)
            writer.writerow(dataValues)
        elif os.path.getsize(filename) > 0:
          with open(filename,'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(dataValues)
      if not os.path.exists(filename):
        with open(filename,'a',newline='') as f:
          writer = csv.writer(f)
          writer.writerow(dataHeaders)
          writer.writerow(dataValues)
        
    except BaseException as e:
      print('exception',e)
    else:
      print ('Data has been loaded successfully !')