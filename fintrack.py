import re
from portfolio import Stock, Portfolio
from data import load_holdings, save_holdings, update_holdings, remove_holding
from prices import get_price, get_prices

def view_portfolio(p: Portfolio):
    if len(p) == 0:
        print("No holding yet.\n")
    else: print(p)

def add_holding(p: Portfolio):
    while True:
        ticker = input("Ticker: ").upper()
        if re.fullmatch(r'[A-Z]{1,5}', ticker):
            break
        print("Invalid ticker. Try Again.")

    while True:
        try:
            shares = int(input("Shares: "))
        except ValueError:
            print("Invalid shares. Try again.")
        else:
            if shares <= 0:
                print("Shares must be positive. Try again.")
            else: break

    price = get_price(ticker)
    if price is None:
        print(f"Could not fetch price for {ticker}.")
        return

    stock = Stock(ticker, price, shares, price)
    p.add(stock)
    update_holdings(ticker, shares, price)
    print(f"Added {ticker}: {shares} shares at ${price:.2f}")
    
def remove_holding_menu(p: Portfolio):
    ticker = input("Ticker: ").upper()
    if ticker not in p:
        print(f"{ticker} not found in the portfolio.")
        return
    p.remove(ticker)
    remove_holding(ticker)
    print(f"{ticker} removed from the portfolio.")
    
def refresh_prices(p: Portfolio):
    prices = get_prices(list(p.stocks.keys()))
    if not prices:
        print("Could not fetch prices.")
        return
    for ticker, price in prices.items():
        p.stocks[ticker].price = price
    print("Prices updated.")

def main():
    p = Portfolio()
    loaded_holdings = load_holdings()
    for holding in loaded_holdings:
        ticker = holding["ticker"]
        shares = int(holding["shares"])
        cost_basis = float(holding["cost_basis"])
        price = get_price(ticker)
        if price is None:
            price = cost_basis
        stock = Stock(ticker, price, shares, cost_basis)
        p.add(stock)

def show_chart(p: Portfolio):
    ...

    while True:
        print("-----------------------------")
        print("1. View Portfolio")
        print("2. Add holding")
        print("3. Remove holding")
        print("4. Refresh prices")
        print("5. Exit")
        choice = input("Choose an option: ")
        print("-----------------------------")

        match choice:
            case "1":
                view_portfolio(p)
            case "2":
                add_holding(p)
            case "3":
                remove_holding_menu(p)
            case "4":
                refresh_prices(p)
            case "5":
                break
            case _:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()