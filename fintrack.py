import yfinance as yf
ticker = yf.Ticker("AAPL")
price = ticker.fast_info["lastPrice"]
name = ticker.info["longName"]