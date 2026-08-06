import re
class Stock:
    def __init__(self, ticker, price, shares, cost_basis=None):
        if not re.fullmatch(r"[A-Z]{1,5}", ticker):
            raise ValueError("Ticker not found!")
        if price <= 0:
            raise ValueError("Price must be positive")
        if shares < 0:
            raise ValueError("Shares must be non-negative")

        self.ticker = ticker
        self.price = float(price)
        self.shares = int(shares)
        self.cost_basis = cost_basis if cost_basis is not None else price
    
    @property
    def value(self):
        return self.price * self.shares
        
    def __str__(self):
        sign = "+" if self.unrealized_gain >= 0 else ""
        return f"{self.ticker}: ${self.price:.2f} | {self.shares} shares | Value: ${self.value:,.2f} | P&L: {sign}${self.unrealized_gain:,.2f}"
        
    def buy(self, n):
            self.shares += n
        
    def sell(self, n):
        if n > self.shares:
            raise ValueError("Not enough shares")
        self.shares -= n
        
    @property
    def unrealized_gain(self):
        return (self.price - self.cost_basis) * self.shares

class Portfolio:
    def __init__(self):
        self.stocks = {}
    
    def add(self, stock):
        self.stocks[stock.ticker] = stock
    
    def remove(self, ticker):
        del self.stocks[ticker]
    
    def get(self, ticker):
        return self.stocks[ticker]
    
    @property
    def total_value(self):
        return sum(s.value for s in self.stocks.values())
    
    def __len__(self):
        return(len(self.stocks))
    
    def __str__(self):
        lines = "\n".join(str(s) for s in self.stocks.values())
        return f"{lines}\nTotal Value: ${self.total_value:,.2f} | Holdings: {len(self)}"
    
    def __contains__(self, ticker):
        return ticker in self.stocks
    
class ManagedPortfolio(Portfolio):
    def __init__(self, max_position_pct: float):
        super().__init__()
        self.max_position_pct = max_position_pct
    
    def add(self, stock):
        new_total = self.total_value + stock.value
        if new_total > 0 and stock.value / new_total > self.max_position_pct / 100:
            raise ValueError(f"{stock.ticker} would exceed {self.max_position_pct}% position limit")
        super().add(stock)
