import FrameFunctions as ff
from Ticker import Ticker
# from datetime import datetime
# from datetime import timedelta
from datetime import datetime, date, time, timedelta


important_tickers = ['2yr-10yr_UST', '2yr_tsy', '10yr_swap', 'FN_4.0%_OAS']

name = '2yr_tsy'
date1 = '23-May-05'
date2 = '03-Jun-05'


def format_date(date):
    array = date.split('-')
    if len(array[0]) is 1:
        return '0' + date
    return date

delta = ff.get_delta(name, date1, date2)
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

def regress_compare(name, date1, date2):
    t = tickers[name]
    p_val, slope = ff.get_linregress(name, date1, date2)
    output = ''
    if p_val < .05:
        if slope > 0:
            output += 'The ' + str(t._fullname) + ' ' + 'has ' + str(t._up_value) + ' overall.'
            if 'UST' in name:
                output += ' Concerning the spreads of 2yr rates versus 10yr rates, they have been ' + \
                          str(t._up_value) + '.'
        elif slope < 0:
            output += 'The ' + str(t._fullname) + ' ' + 'has ' + str(t._down_value) + ' overall.'
            output += ' Concerning the spreads of 2yr rates versus 10yr rates, they have been ' + \
                      str(t._down_value) + '.'
        elif slope is 0:
            output += 'The ' + str(t._fullname) + ' ' + 'has had mixed trends.'

        return output
    else:
        return 'The ' + str(t._fullname) + ' ' + 'has had mixed trends.'


def week_compare(name, date1, date2):
    t = tickers[name]
    output = ''
    min = abs(ff.get_delta(name, date1, date2))
    max = abs(ff.get_delta(name, date1, date2))
    cur_date = convert_date(date1)
    date2 = convert_date(date2)
    prev_delta = -1
    while not cur_date == date2:
        temp1 = revert_date(cur_date)
        cur_date += timedelta(days=1)
        temp2 = revert_date(cur_date)
        delta = ff.get_delta(name, temp1, temp2)
        if int(min) > int(abs(delta)):
            min = abs(delta)
        if int(max)< int(abs(delta)):
            max = abs(delta)

        if delta > 0:
            delta = 1
        else:
            delta = 0
        if prev_delta is -1:
            prev_delta = delta
            continue
        # print (prev_delta, delta)
        if not prev_delta is delta:
            delta = -2
            break
        prev_delta = delta
        min = str(min)
        max = str(max)
    if delta is 1:
        output += 'In this time interval, all of the ' + str(t._fullname) + ' consistently ' + str(t._up_value) + '.'
    elif delta is 0:
        output += 'In this time interval, all of the ' + str(t._fullname) + ' consistently ' + str(t._down_value) + '.'
    output += 'Fluctuation in between these dates ranges from ' + str(min) + ' to ' + str(max) + 'bps. '
    return output

def convert_date(date):
    # '18-May-2005'
    date = format_date(date)
    year = int(date[7:])
    if 59 <= year <= 99:
        date = date[0:7] + '19' + str(year)
    else:
        date = date[0:7] + '20' + str(year).zfill(2)
    return datetime.strptime(date, '%d-%b-%Y')


def revert_date(date):
    temp = date.strftime('%d-%b-%Y')
    return str(temp[0:7]) + str(temp[9:])


def paragraph(date1, date2):
    output = ''
    dateobj1 = convert_date(date1)
    dateobj2 = convert_date(date2)
    dateobj1 += timedelta(days=1)
    ff.graph_yield_curve(date2)

    # if greater than 1 day difference

    if dateobj1 < dateobj2:
        for x in important_tickers:
            output += week_compare(x, date1, date2) + ' ' + regress_compare(x, date1, date2) + ' '
        return output
    else:
        for x in important_tickers:
            output += day_compare(x, date1, date2) + ' '
        return output




# print(day_compare(name, date1, date2))
# print(regress_compare(name, date1, date2))
# print(week_compare(name, date1, date2))
#print(paragraph(date1, date2))
#print (ff.get_lowest('2yr_tsy', '23-May-05'))
#print(day_compare(name, date1, date2))
#2 year treasury interest rates rallied 7bps.

