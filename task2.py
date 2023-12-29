class StockPortfolio:
    def __init__(self):
        self.portfolio = []

    def add_stock(self, symbol):
        stock = {'id': len(self.portfolio) + 1, 'symbol': symbol}
        self.portfolio.append(stock)
        print(f"Stock '{symbol}' added to the portfolio.")

    def remove_stock(self, stock_id):
        stock = next((s for s in self.portfolio if s['id'] == stock_id), None)
        if stock:
            self.portfolio.remove(stock)
            print(f"Stock '{stock['symbol']}' removed from the portfolio.")
        else:
            print("Stock not found in the portfolio.")

    def display_portfolio(self):
        print("\nYour Portfolio:")
        for stock in self.portfolio:
            print(f"{stock['id']}. {stock['symbol']}")
        print()

def main():
    portfolio = StockPortfolio()

    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ")
            portfolio.add_stock(symbol)
        elif choice == '2':
            stock_id = int(input("Enter stock ID to remove: "))
            portfolio.remove_stock(stock_id)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            print("Exiting the Stock Portfolio Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
