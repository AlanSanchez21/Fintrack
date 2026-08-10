# Fintrack
A CLI-based personal finance tracker built in Python. Track stock holdings, fetch live prices via yfinance, calculate unrealized gains/losses, and generate portfolio summaries, with persistent CSV storage. **This is a SIMULATION**

# Install it !
The only things you need to download is : yfinance. To download, write in the terminal "pip3 install yfinance".

# How to run it
The most efficient way to run the program is through writting in the terminal "python3 fintrack.py".

# Features of the program
There will appear a menu with 5 interactive options.
| Interactive Options | Description |
|---------------------|-------------|
|   1. `View Portfolio` | Will print the content inside the portfolio, the symbol of the stock, the amount of money hold, number of shares, the value of a single stock, and the profit or loss along the time. |
|   2. `Add to Portfolio` | Write the stock synbol and the amount of shares you want, and it will store it in the portfolio. |
|   3. `Remove from Portfolio` | Write the stock synbol and the amount of shares you want to be removed, and it will remove them from the portfolio. |
|   4. `Refresh Portfolio` | Will refresh the value of the stock to the most recent registered price. |
|   5. `Exit`| Will kick you out of the program |

# File Structures
| File | Description |
|------|-------------|
| `fintrack.py` | Main entry point and dislay interactive menu |
| `portfolio.py` | Stock and Portfolio classes |
| `data.py` | CSV read/write for persistent storage |
| `prices.py` | Live price fetching via yfinance |

# Extra Notes !!!
This program's holdings are saved to `holdings.csv` and persistent between sessions.