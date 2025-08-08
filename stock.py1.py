import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 140
}

portfolio = {}  # User-entered stocks and quantities

# User input
print("Enter stock symbols and quantities (type 'done' to finish):")
while True:
    stock = input("Stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

# Calculate total investment
total_investment = 0
summary_data = [["Stock", "Quantity", "Price", "Value"]]

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    summary_data.append([stock, qty, price, value])

summary_data.append(["", "", "Total", total_investment])

# Display summary in terminal
print("\n=== Portfolio Summary ===")
for row in summary_data:
    print("{:<8} {:<8} {:<8} {:<10}".format(*row))

# Save to CSV
save = input("Save to CSV file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(summary_data)
    print("Saved to portfolio_summary.csv")
