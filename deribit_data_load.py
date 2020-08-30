
from deribit_ws import client
import json
import websockets
import time
import sys
import os
import pandas as pd
import datetime


def real_time():
    pass


def order_book():
    index = client.get_order_book('BTC-PERPETUAL')
    instrument_name = index['result']
    name = instrument_name['instrument_name']
    price = index['result']
    price_ask = price['asks']
    # _times = price['timestamp']
    df_p_a = pd.DataFrame(price_ask)
    df_p_a.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
    price_bids = price['bids']
    df_p_b = pd.DataFrame(price_bids)
    df_p_b.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
    print('\t\t', name)
    print('\t\t'"Order Book")
    print('\t\t'"Bids Price")
    print(df_p_b.head(10))
    print('\t\t'"Asks Price")
    print(df_p_a.head(10))
    # print(_times)


def show_order_price():
    index = client.get_order_book('BTC-PERPETUAL')
    _instrument_name = index['result']
    _price = index['result']
    _times = _price['timestamp']
    while _times != 0:
        print(order_book())

# column = df_trac.iloc[[0, 5]]
# print(column)
# print(df_trac)
