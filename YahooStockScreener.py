from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta

# delta = ticker['Close'].diff()
# up = delta.clip(lower=0)
# down = -1*delta.clip(upper=0)
# ema_up = up.ewm(com=13, adjust=False).mean()
# ema_down = down.ewm(com=13, adjust=False).mean()
# rs = ema_up/ema_down

# print(ticker)


today = datetime.today().strftime('%Y/%m/%d')

now = datetime.now()

unformatted_last_week = now - timedelta(days=14)

last_week = unformatted_last_week.strftime('%Y/%m/%d')

tickers = ['AAPL', 'AMZN', 'BA']

historical_datas = {}

for ticker in tickers:
    historical_datas[ticker] = get_data(ticker=ticker, start_date=last_week,
                                        end_date=today, index_as_date=True, interval="1d")
    delta = historical_datas[ticker]['adjclose'].diff()
    up = delta.clip(lower=0)
    down = -1*delta.clip(upper=0)
    ema_up = up.ewm(com=7, adjust=False).mean()
    ema_down = down.ewm(com=7, adjust=False).mean()
    rs = ema_up/ema_down
    rsi = 100 - (100/(1+rs))
    print(rsi, ticker)


# print(historical_datas)
