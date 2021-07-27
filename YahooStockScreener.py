from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta

today = datetime.today().strftime('%Y/%m/%d')

now = datetime.now()

unformatted_last_week = now - timedelta(days=7)

last_week = unformatted_last_week.strftime('%Y/%m/%d')

tickers = ['AAPL', 'AMZN', 'BA']

historical_datas = {}

for ticker in tickers:
    historical_datas[ticker] = get_data(ticker=ticker, start_date=last_week,
                                        end_date=today, index_as_date=True, interval="1d")

print(historical_datas)
