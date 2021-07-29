from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import json

from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    today = datetime.today().strftime('%Y/%m/%d')

    now = datetime.now()

    unformatted_last_week = now - timedelta(days=7)

    last_week = unformatted_last_week.strftime('%Y/%m/%d')

    tickers = ['AAPL', 'AMZN', 'BA']

    historical_datas = {}

    for ticker in tickers:
        historical_datas[ticker] = get_data(ticker=ticker, start_date=last_week,
                                            end_date=today, index_as_date=True, interval="1d")
    historical_datas[]
    return HttpResponse("Success!")
