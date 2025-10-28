# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

# List of stock tickers
tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']

# Create 'charts' directory if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

# Download and plot data for each ticker
for ticker in tickers:
    data = yf.download(ticker, period="1mo")  # last 1 month of data
    if data.empty:
        print(f"No data found for {ticker}, skipping.")
        continue

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label=f"{ticker} Closing Price")
    plt.title(f"{ticker} - Last Month Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.legend()
    plt.grid(True)
    
    # Save plot to charts folder
    filename = f"charts/{ticker}.png"
    plt.savefig(filename)
    plt.close()  # close to free memory for next plot

    print(f"Saved {filename}")

print("All charts created successfully!")
