import yfinance as yf
import indices as index


# ibex = index.Index("^IBEX")
# ibex.exportToCSV('informacion',ibex.getGeneralInfo())

ibex = yf.Ticker("MAP.MC")
print(ibex.history("max"))


