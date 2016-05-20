import pandas as pd #this is how I usually import pandas

Location = r'C:\CreditSuisse\NaturalLanguageGenerator\locus_data_12years.csv'
df = pd.read_csv(Location)

df_index = df.set_index('Date')


def get_delta(ticker, first_date, second_date):
    return bp_format(df_index.at[second_date, ticker] - df_index.at[first_date, ticker])


def get_value(ticker, date):
    return bp_format(df_index.at[date, ticker])


def bp_format(number):
    return int(round(number*100))


def get_headers():
    return list(df_index.columns.values)
