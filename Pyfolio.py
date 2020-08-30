import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime
#get PTTGC data
pttgc = pdr.get_data_yahoo('PTTGC.BK', start = datetime.datetime(2019, 1, 1), end = datetime.datetime ( 2020, 8, 20))
#get TOP data
top = pdr.get_data_yahoo('TOP.BK', start = datetime.datetime(2017, 10, 1), end = datetime.datetime ( 2018, 1, 1))

plt.plot(pttgc)
plt.show()


# print(pttgc)
# print(top)

