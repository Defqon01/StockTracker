import requests
import pandas as pd

def fetch_stock_symbols(exchange, api_key):
    url = f"https://finnhub.io/api/v1/stock/symbol?exchange={exchange}&token={api_key}"
    try:
        response = requests.get(url)
        symbols = [item['symbol'] for item in response.json() if 'symbol' in item]
        return symbols
    except Exception as e:
        print(f"Failed to fetch symbols from {exchange}: {e}")
        return []

def get_stock_data(symbol, api_key):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'c' in data and 'pc' in data and data['c'] != 0:
            change_percent = ((data['c'] - data['pc']) / data['pc']) * 100
            return (symbol, data['c'], change_percent)
        else:
            return (symbol, None, None)
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return (symbol, None, None)

def main():
    api_key = 'YOUR_API_KEY_HERE'  # Replace this with your actual API key
    exchange = 'US'  # Example: 'US' for US stocks
    symbols = fetch_stock_symbols(exchange, api_key)
    results = []

    if symbols:
        for symbol in symbols:
            symbol_data = get_stock_data(symbol, api_key)
            if symbol_data[1] is not None and symbol_data[2] is not None:
                results.append(symbol_data)
            else:
                print(f"No data or incomplete data for {symbol}")

    if results:
        # Convert results to DataFrame
        df = pd.DataFrame(results, columns=['Symbol', 'Current Price', 'Change Percent'])
        df_sorted = df.sort_values(by='Change Percent', ascending=False)
        
        # Display top 10 performers and bottom 10 performers
        print("Top 10 Performers:")
        print(df_sorted.head(10))
        print("\nBottom 10 Performers:")
        print(df_sorted.tail(10))
    else:
        print("No valid data received from API for any symbols.")

if __name__ == "__main__":
    main()
