import yfinance as yf

# clase que contiene a los indices generales, ejemplo sp500, ibex35, etc.
class Index :
  # Constructor, se le pasa por parametro el nombre del indice y genera un array que contendra las acciones asociadas
  def __init__(self,name):
    self.name = name
    self.ticker = []
    self.index=yf.Ticker(name)

  # Metodo que elimina un ticket ya registrado
  def deleteTicker(self,name):
    self.ticker.remove(name)

  # Metodo que agrega un nuevo ticket
  def addTicker(self,name):
    self.ticker.append(name)

  # Metodo que retorna la informacion general del indice
  def getGeneralInfo(self):
    return self.index.info
