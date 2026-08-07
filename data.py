import csv
def load_holdings() -> list[dict]:
    """Reads holdings.csv and will return a list with some keys, however if there is none then will return an empty list"""
    try:
        with open("holdings.csv", "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_holdings(holdings: list[dict]):
    with open("holdings.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["ticker", "shares", "cost_basis"])
        writer.writeheader()
        writer.writerows(holdings)

def update_holdings(ticker, shares, cost_basis):
    holdings = load_holdings()
    for holding in holdings:
        if holding["ticker"] == ticker:
            holding["shares"] = shares
            holding["cost_basis"] = cost_basis
            break
    else:
        holdings.append({"ticker": ticker, "shares": shares, "cost_basis": cost_basis})
    save_holdings(holdings)