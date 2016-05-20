import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import sys
import csv

Location = r'C:\Users\Carolyn\hack\NaturalLanguageGenerator\locus_data_12years.csv'
df = pd.read_csv(Location)

df_index = df.set_index('Date')
df_index.fillna(method='bfill')

#print(df_index.irow(912))
df_index.fillna(method='bfill', inplace=True)
#print('     AFTER')
#print(df_index.irow(912))

def get_delta(ticker, first_date, second_date):
    try:
        return bp_format(df_index.at[second_date, ticker] - df_index.at[first_date, ticker])
    except KeyError:
        print('No data available for these dates.')
        sys.exit()


def get_value(ticker, date):
    try:
        return bp_format(df_index.at[date, ticker])
    except KeyError:
        print('No data available for this date.')
        sys.exit()

def get_percent_value(ticker, date):
    return df_index.at[date, ticker]

def bp_format(number):
    return int(round(number*100))


def get_headers():
    return list(df_index.columns.values)


def get_linregress(name, date1, date2):
    series = df_index.loc[:, name : name].values[get_row_index(date1):get_row_index(date2)]
    series = [float(x) for x in series]
    dates = df.index.values[get_row_index(date1):get_row_index(date2)]
    slope, intercept, r_val, p_val, std_err = stats.linregress(dates,series)
    return p_val, slope


def get_row_index(date):
    count = -1
    for x in df['Date'].tolist():
        count += 1
        if x == date:
            return count
    return -1


def get_col_index(ticker):
    count = -1
    for x in get_headers():
        count += 1
        if x == ticker:
            return count


def get_lowest(name, date):
    # series = df_index.loc[0:get_row_index(curDate), name:name].values()
    # print (series)
    series = df_index.loc[:, name: name].values[0:get_row_index(date)]
    # print(series)
    min = series[0]
    count = 0
    counter = -1
    for x in series:
        counter += 1
        if min > x:
            min = x
            count = counter

    text = ''
    with open(Location, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        text = mycsv[count+1][0]
    return float(min), text


def get_highest(name, date):
    # series = df_index.loc[0:get_row_index(curDate), name:name].values()
    # print (series)
    series = df_index.loc[:, name: name].values[0:get_row_index(date)]
    # print(series)
    maximum = series[0]
    count = 0
    counter = -1
    for x in series:
        counter += 1
        if maximum < x:
            maximum = x
            count = counter

    text = ''
    with open(Location, 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        text = mycsv[count+1][0]
    return float(maximum), text


def graph_yield_curve(date):
    rates = [2, 3, 5, 10, 30]
    yields = []
    yields.append(get_percent_value('2yr_tsy', date))
    yields.append(get_percent_value('3yr_tsy', date))
    yields.append(get_percent_value('5yr_tsy', date))
    yields.append(get_percent_value('10yr_tsy', date))
    yields.append(get_percent_value('30yr_tsy', date))
    plt.plot(rates, yields, 'bs')
    plt.xlim(0, 35)
    plt.xlabel('Time frame (in years) of Treasury Bill')
    plt.ylabel('Yield (in %)')
    fig1 = plt.gcf()
    fig1.savefig(r'C:\CreditSuisse\REAL\NaturalLanguageGenerator\NLG\src\static\yield.png')




