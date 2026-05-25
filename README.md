# didactic-train
## Project Overview
The didactic-train project is designed to analyze stock market data using the Alpaca API. It retrieves historical stock data and provides a foundation for further analysis and trading strategies.
## Key Features
* Retrieves historical stock data for a specified symbol and timeframe
* Utilizes the Alpaca API for trading and data services
* Provides a basic structure for building custom trading strategies
## Tech Stack
* Python 3.x
* Alpaca API (alpaca-trading-api and alpaca-data-api libraries)
## Installation
To install the required libraries, run the following command:
```bash
pip install alpaca-trading-api alpaca-data-api
```
## Usage
1. Replace `API_KEY` and `API_SECRET` with your actual Alpaca API credentials in `main.py`
2. Run the script using `python main.py`
## Environment Variables
The following environment variables are required:
* `API_KEY`: Your Alpaca API key
* `API_SECRET`: Your Alpaca API secret
These variables can be set in a `.env` file or as system environment variables.