import yfinance as yf

class Accion:
    def __init__(self,name):
        self.name = name
        self.accion = yf.ticker(name)

    def getName(self):
        return self.name
    #  Metodo que retorna todos los valores registrados de una accion o conjunto de acciones (open/High/Low/Close/Volume/Dividends/Stock/Splits)
    def getTotalData(self):
        return self.accion.history(period="max")

    # Metodo que retorna todos los valores registrados dedividendos y splits 
    def getDividendSplitData(self):
        return self.accion.actions

    # Metodo que retorna la informacion de todos los dividendos de una accion
    def getDividend(self):
        return self.accion.dividends

    # Metodo que retona la informacion de todos los splits registrados de una accion 
    def getSplits(self):
        return self.accion.splits

    # Metodo que retorna la informacion de todos los resultados financieros de una accion
    def finacialsResults(self):
        return self.accion.financials

    # Metodo que retorna informacion sobre los propietarios de acciones por segmentos 
    def majorHoldersSet(self):
        return self.accion.major_holders

    # Metodo que retorna informacion sobre los propietarios institucionales de la acciuon 
    def institutionalHolders(self):
        return self.accion.institutional_holders

    # Metodo que retorna el balance de las acciones    
    def balanceResults(self):
        return self.accion.balance_sheet

    # Metodo que retorna el flujo de caja de las acciones
    def cashFlow(self):
        return self.accion.cashFlow

    # Metodo que retorna las ganancias de la accion
    def earnings(self):
        return self.accion.earnings

    # Metodo que retorna la sostenibilidad de una accion 
    def sustainability(self):
        return self.accion.sustainability

    # Metodo que retorna las recomendaciones de principales asesores 
    def organizationsRecommendations(self):
        return self.accion.recommendations

    # Metodo que retorna el calendario de eventos programados de una accion
    def eventsCalendar(self):
        return self.accion.calendar