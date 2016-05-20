import FrameFunctions as ff
import Ticker as t

name = '2yr_tsy'
date1 = '18-May-05'
date2 = '19-May-05'
delta = ff.get_delta(name, date1, date2)

t = t.Ticker(name)
print(t._up_value)
tickers = {}
for x in ff.get_headers():
    tickers[x] = t.Ticker(x)


def day_compare(name, date1, date2):
    t = tickers[name]
    delta = ff.get_delta(name, date1, date2)
    if delta < 0:
        return "The " + t._fullname + t._down_value + " by " + delta + "bps."
    elif delta > 0:
        return "The " + t._fullname + t._up_value + " by " + delta + "bps."
    return "There was no change in the " + t._fullname + "."

print()
#2 year treasury interest rates rallied 7bps.

