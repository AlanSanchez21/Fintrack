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

def get_prices(tickers: list[str]) -> dict[str, float]:
    return {t: p for t in tickers if (p := get_price(t)) is not None}