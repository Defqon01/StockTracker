# Stock Tracker

## Project Overview
This Stock Tracker is a Python application that fetches and analyzes stock price data using the Finnhub API. The script retrieves stock symbols from a specified exchange, gathers their current and previous closing prices, and calculates the percentage change to identify the top and bottom performers. This tool is useful for investors or analysts looking to quickly scan the market for potential investment opportunities.

## Features
- **Fetch Stock Symbols**: Retrieves a list of all stock symbols from a specified stock exchange.
- **Get Stock Data**: Gathers real-time stock price data (current and previous close) for each symbol.
- **Calculate Changes**: Computes the percentage change in stock prices to highlight top and bottom performers.
- **Results Display**: Displays the top 10 and bottom 10 performers based on the price change percentage.

## Dependencies
This project relies on the following Python libraries:
- `requests`: To handle HTTP requests to the Finnhub API.
- `pandas`: For data manipulation and analysis.

## Setup Instructions

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/stock-tracker.git
   cd stock-tracker
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

### API Key Configuration
You will need to obtain a free API key from [Finnhub](https://finnhub.io/). Once you have the key, replace `'YOUR_API_KEY_HERE'` in the `stock_tracker.py` script with your actual API key.

## Usage
Run the script from the command line:
```bash
python stock_tracker.py
```

The script will execute and print the top 10 and bottom 10 stock performers based on the price change percentage.

## Contributing
Contributions to the Stock Tracker are welcome. Please ensure that your pull requests are well-documented and include any necessary test updates.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

### Notes:
- **Adjust the Repository URL**: Replace `https://github.com/yourusername/stock-tracker.git` with your actual repository URL.
- **API Key Security**: Remind users not to expose their API keys publicly, suggesting the use of environment variables or other methods to keep keys secure.
- **LICENSE File**: If you decide to use the MIT License, make sure to include a `LICENSE` file in your repository with the MIT License text.

This README provides all necessary details to get a user started with using and contributing to your stock tracker project. If there are specific features or configurations unique to your project, be sure to include them in the relevant sections of the README.
