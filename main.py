from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
trading_client = TradingClient(API_KEY, API_SECRET)
data_client = StockHistoricalDataClient(API_KEY, API_SECRET)

dia_request = StockBarsRequest(symbol_or_symbols=["DIA"], timeframe=TimeFrame.Day, start="2023-01-01", end="2024-01-01")
dia_data = data_client.get_stock_bars(dia_request)
