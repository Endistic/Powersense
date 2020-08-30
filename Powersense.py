import client
_symbol = 'BTC-PERPETUAL'
market_ticker = client.exchange.fetch_ticker(_symbol)
_bid = market_ticker['bid']
_ask = market_ticker['ask']

print(_bid)
print(_ask)
