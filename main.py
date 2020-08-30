from deribit_ws import client
def order_book():
    index = client.get_order_book('BTC-PERPETUAL')
    instrument_name = index['result']
    print(index)

    # name = instrument_name['instrument_name']
    # price = index['result']
    # price_ask = price['asks']
    # # df = pd.DataFrame(index)
    # # df_trac = df[['result']]
    # df_p_a = pd.DataFrame(price_ask)
    # df_p_a.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
    # price_bids = price['bids']
    # df_p_b = pd.DataFrame(price_bids)
    # df_p_b.rename(columns={0: 'Price', 1: 'Size'}, inplace=True)
    # print('\t\t', name)
    # print('\t\t'"Order Book")
    # print('\t\t'"Bids Price")
    # print(df_p_b.head(10))
    # print('\t\t'"Asks Price")
    # print(df_p_a.head(10))

# column = df_trac.iloc[[0, 5]]
# print(column)
# print(df_trac)
