import FrameFunctions as ff
from Ticker import Ticker

#name = '10yr_tsy'
#date1 = '19-May-05'
# date2 = '20-May-05'
# delta = ff.get_delta(name, date1, date2)

tickers = {}
for x in ff.get_headers():
    tickers[x] = Ticker(x)


def day_compare(name, date1, date2):
    t = tickers[name]
    delta = ff.get_delta(name, date1, date2)
    if delta < 0:
        return 'The ' + str(t._fullname) + ' ' + str(t._down_value) + ' by ' + str(abs(delta)) + 'bps.'
    elif delta > 0:
        return 'The ' + str(t._fullname) + ' ' + str(t._up_value) + ' by ' + str(abs(delta)) + 'bps.'
    return 'There was no change in the ' + t._fullname + '.'

#print(day_compare(name, date1, date2))
#2 year treasury interest rates rallied 7bps.

