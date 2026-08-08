from portfolio import Stock, Portfolio
from data import load_holdings, save_holdings, update_holdings, remove_holding
from prices import get_price, get_prices

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

    while True:
        print("1. View Portfolio")
        print("2. Add holding")
        print("3. Remove holding")
        print("4. Refresh prices")
        print("5. Exit")
        choice = input("Choose an option: ")
        match choice:
            case "1":
                view_portfolio(p)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
            case _:
                print("Invalid option. Try again.")

def view_portfolio(p: Portfolio):
    if len(p) == 0:
        print("No holding yet.")
    else: print(p)

if __name__ == "__main__":
    main()