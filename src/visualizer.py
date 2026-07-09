import matplotlib.pyplot as plot
import pandas as pd


# def plot_close_price(data: pd.DataFrame, ticker: str):
#     plot.figure(figsize=(12, 5))
#     plot.plot(data['Date'], data['Close'], color='blue', linewidth= 1.5)
#     plot.title(f"{ticker} - Closing price")
#     plot.xlabel('Date')
#     plot.ylabel('Price (USD)')
#     plot.grid(True)
#     plot.tight_layout()
#     plot.show()

def plot_close_price(data: pd.DataFrame, ticker: str):
    fig, ax1 = plot.subplots(figsize=(12, 6))

    # Volume (háttérben)
    ax2 = ax1.twinx()
    ax2.bar(data["Date"], data["Volume"], color="grey", alpha=0.3, width=0.8)
    ax2.set_ylabel("Volume (million pcs)", color="grey")

    # Closing price (előtérben)
    ax1.plot(data["Date"], data["Close"], color="blue", linewidth=1.5)
    ax1.set_title(f"{ticker} - Closing Price & Volume")
    ax1.set_ylabel("Price (USD)", color="blue")
    ax1.set_xlabel("Date")
    ax1.grid(True)

    plot.tight_layout()
    plot.show()