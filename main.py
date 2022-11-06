import yfinance as yf

# clase que contiene a los indices generales, ejemplo sp500, ibex35,
class Index :
    def __init__(self,name):
        self.name = name
        pass







#  Metodo que retorna todos los valores registrados de una accion o conjunto de acciones (open/High/Low/Close/Volume/Dividends/Stock/Splits)
def getTotalData(acciones):
    historic = acciones.history(period="max")
    return historic

# Metodo que retorna todos los valores registrados dedividendos y splits 
def getDividendSplitData(acciones):
    dividendsSplit = acciones.actions
    return dividendsSplit
# Metodo que retorna la informacion de todos los dividendos de una accion
def getDividend(acciones):
    dividends = acciones.dividends
    return dividends

# Metodo que retona la informacion de todos los splits registrados de una accion 
def getSplits(acciones):
    splits = acciones.splits
    return splits

# Metodo que retorna la informacion de todos los resultados financieros de una accion
def finacialsResults(acciones):
    finalcialsResutls = acciones.financials
    return finalcialsResutls

# Metodo que retorna informacion sobre los propietarios de acciones por segmentos 
def majorHoldersSet(acciones):
    holders = acciones.major_holders
    return holders
# Metodo que retorna informacion sobre los propietarios institucionales de la acciuon 
def institutionalHolders(acciones):
    institutions = acciones.institutional_holders
    return institutions

# Metodo que retorna el balance de las acciones    
def balanceResults(acciones):
    balances = acciones.balance_sheet
    return balances

# Metodo que retorna el flujo de caja de las acciones
def cashFlow(acciones):
    cashFlow = acciones.cashFlow
    return cashFlow

# Metodo que retorna las ganancias de la accion
def earnings(acciones):
    earnings = acciones.earnings
    return earnings

# Metodo que retorna la sostenibilidad de una accion 
def sustainability(acciones):
    sustainability = acciones.sustainability
    return sustainability

# Metodo que retorna las recomendaciones de principales asesores 
def organizationsRecommendations(acciones):
    recomendation = acciones.recommendations
    return recomendation

# Metodo que retorna el calendario de eventos programados de una accion
def eventsCalendar(acciones):
    events = acciones.calendar
    return events

msft = yf.Ticker("^IBEX")
print (msft.info)


