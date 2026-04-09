import csv

# Predefined stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

print("📊 Stock Portfolio Tracker")

n = int(input("How many stocks you want to enter: "))

# Create CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Stock Name", "Quantity", "Price", "Total Value"])
    
    for i in range(n):
        name = input("Enter stock name: ").upper()
        qty = int(input("Enter quantity: "))
        
        if name in stocks:
            price = stocks[name]
            value = price * qty
            total += value
            
            print("Added:", name, "| Value:", value)
            
            # Save each entry in CSV
            writer.writerow([name, qty, price, value])
        else:
            print("❌ Stock not found")

    # Save total at end
    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total])

print("\n💰 Total Investment Value:", total)
print("✅ Data saved in portfolio.csv file")