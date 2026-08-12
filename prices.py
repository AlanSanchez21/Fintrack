import yfinance as yf

def get_price(ticker: str) -> float | None:
    try:
        data = yf.Ticker(ticker)
        price = data.fast_info["lastPrice"]
        if price and price > 0:
            return float(price)
        return None
    except Exception:
        return None

def get_history(ticker, period="1mo"):
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period=period)
        if hist.empty:
            return None
        else:
            prices = hist["Close"]
            dates = hist.index
            return dates, prices
    except Exception:
        return None

def get_prices(tickers: list[str]) -> dict[str, float]:
    return {t: p for t in tickers if (p := get_price(t)) is not None}
