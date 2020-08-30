import ccxt
import credentials
import time
# import pandas as pd
import numpy as np
import sys

exchange = ccxt.deribit({
    'apiKey': credentials.client_id,
    'secret': credentials.client_secret
})
# _perpetual = 'BTC-PERPETUAL'
# _sep = 'BTC-25SEP20'
# _dec = 'BTC-25DEC20'
# _mar = 'BTC-26MAR21'
# delay = 1
#
#
# def order_book(_symbol):
#     count_loop = 1
#     while True:
#         orderBook = exchange.fetch_order_book(_symbol, 5)
#         orderBook_bid = orderBook['bids']
#         orderBook_ask = orderBook['asks']
#         list_bid = pd.DataFrame(orderBook_bid)
#         list_ask = pd.DataFrame(orderBook_ask)
#         list_bid.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
#         list_ask.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
#         # print("Ask")
#         # print(list_ask)
#         time.sleep(delay)
#         print("Bid")
#         print(list_bid)
#         count_loop += 1
#
#
#
# def order_one_bid(_symbol):
#     count_loop = 1
#     while (count_loop > 0) is True:
#         orderBook = exchange.fetch_order_book(_symbol, 5)
#         orderBook_bid = orderBook['bids']
#         list_bid = pd.DataFrame(orderBook_bid)
#         price_bid_1 = list_bid[0][0]
#         bid_size_1 = list_bid[1][0]
#         time.sleep(delay)
#         print(price_bid_1, bid_size_1)
#         # print(bid_size_1)
#         count_loop += 1
#         #price_bid_1 = list_bid[0][0]
#         # price_bid_2 = list_bid[0][1]
#         # price_bid_3 = list_bid[0][2]
#         # price_bid_4 = list_bid[0][3]
#         # price_bid_5 = list_bid[0][4]
#         #
#         # bid_size_1 = list_bid[1][0]
#         # bid_size_2 = list_bid[1][1]
#         # bid_size_3 = list_bid[1][2]
#         # bid_size_4 = list_bid[1][3]
#         # bid_size_5 = list_bid[1][4]
#
#
#
#
#     # list_bid.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
#     # list_ask.rename(columns={0: 'Price', 1: 'Size'}, inplace=
#     # Bidprice
#
#     # print(price_bid_1)
#     # print(price_bid_2)
#     # print(price_bid_3)
#     # print(price_bid_4)
#     # print(price_bid_5)
#     # print('\n')
#
#     # Bidsize
#     # bid_size_1 = list_bid[1][0]
#     # bid_size_2 = list_bid[1][1]
#     # bid_size_3 = list_bid[1][2]
#     # bid_size_4 = list_bid[1][3]
#     # bid_size_5 = list_bid[1][4]
#     # print(bid_size_1)
#     # print(bid_size_2)
#     # print(bid_size_3)
#     # print(bid_size_4)
#     # print(bid_size_5)
#     # print('\n')
#
#     # Askprice
#     # ask_price_1 = list_ask[0][0]
#     # ask_price_2 = list_ask[0][1]
#     # ask_price_3 = list_ask[0][2]
#     # ask_price_4 = list_ask[0][3]
#     # ask_price_5 = list_ask[0][4]
#     # print(ask_price_1)
#     # print(ask_price_2)
#     # print(ask_price_3)
#     # print(ask_price_4)
#     # print(ask_price_5)
#     # print('\n')
#
#     # Asksize
#     # ask_size_1 = list_ask[1][0]
#     # ask_size_2 = list_ask[1][1]
#     # ask_size_3 = list_ask[1][2]
#     # ask_size_4 = list_ask[1][3]
#     # ask_size_5 = list_ask[1][4]
#
#     # print(ask_size_1)
#     # print(ask_size_2)
#     # print(ask_size_3)
#     # print(ask_size_4)
#     # print(ask_size_5)
#
#
# def order_one_ask(_symbol):
#     orderBook = exchange.fetch_order_book(_symbol, 5)
#     orderBook_ask = orderBook['asks']
#     list_ask = pd.DataFrame(orderBook_ask)
#     ask_price_1 = list_ask[0][0]
#     ask_price_2 = list_ask[0][1]
#     ask_price_3 = list_ask[0][2]
#     ask_price_4 = list_ask[0][3]
#     ask_price_5 = list_ask[0][4]
#
#     ask_size_1 = list_ask[1][0]
#     ask_size_2 = list_ask[1][1]
#     ask_size_3 = list_ask[1][2]
#     ask_size_4 = list_ask[1][3]
#     ask_size_5 = list_ask[1][4]
#     return (list_ask, ask_price_1, ask_price_2, ask_price_3, ask_price_4, ask_price_5, ask_size_1, ask_size_2,
#             ask_size_3, ask_size_4, ask_size_5)
#
#
# def market_price(_symbol):
#     market_ticker = exchange.fetch_ticker(_symbol)
#     _information = market_ticker['info']
#     _market_price = _information['mark_price']
#
#