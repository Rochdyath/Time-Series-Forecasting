import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

end_date = today.strftime("%Y-%m-%d")
d2 = today - timedelta(days=365)
start_date = d2.strftime("%Y-%m-%d")


data = yf.download('GOOG', start=start_date, end=end_date, progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())
print(data.tail())