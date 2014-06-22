import pandas as pd
import pandas.io.sql as psql
import MySQLdb as mdb
import numpy as np
from user_input_mod import *
import matplotlib.pyplot as plt

mycon = mdb.connect('localhost', 'main_user', 'mainsql', 'securities_master')

class OBV(object):

    def __init__(self):

# note that this query selects the volume as well adjusted close price..
        self.query = """SELECT dp.price_date, dp.adj_close_price, dp.volume, sym.ticker.
        FROM symbol as sym
        INNER JOIN daily_price AS dp
        ON dp.symbol_id = sym.id
        WHERE
        (dp.price_date BETWEEN
        {start_date} - INTERVAL 1 DAY AND {end_date})
        AND
        (sym.ticker = {ticker})
        ORDER BY dp.price_date ASC;""".format(ticker = get_ticker(), start_date = get_start_date(), end_date = get_end_date())

#This will hold our initial dataframe. Is empty when class is first instantiated.
        self.dataframe = pd.DataFrame()
#or the cumulative number of trades exchanging hands,.

#This function pulls our initial DF from the database using psql
    def initial_df(self):
        self.dataframe =  psql.frame_query(self.query, con=mycon, index_col='price_date')
        return

#Creates column in database containing boolean value based on whether or not the
#daily close price is higher than the previous days'.
    def append_bool(self):
        self.dataframe["positive_return?"] = self.dataframe["adj_close_price"] > self.dataframe["adj_close_price"].shift(-1)
        return

#This creates a new pd Series (column) within dataframe and
#fills it with the neg or pos volume for each day based on.
# the positve_return Series
    def calc_obv_daily(self):
        self.dataframe['daily_obv'] = ""
        for idx,series in self.dataframe.iterrows():
            if series['positive_return?'] == True:
                self.dataframe.daily_obv.set_value(idx, series['volume'])
            elif series['positive_return?'] == False:
                self.dataframe.daily_obv.set_value(idx, (series['volume'] * -1))

     def calc_cum_daily_obv(self):
         self.dataframe['daily_cum_obv'] = self.dataframe.daily_obv.cumsum()
         return
 
 def graph_all(dfinstance):
 
     dfinstance[['volume']] = dfinstance[['volume']].astype(int)
 
     cum_obv_series = pd.Series(dfinstance.daily_cum_obv)
     volume_series = pd.Series(dfinstance.volume)
     price_series = pd.Series(dfinstance.adj_close_price)
     index_series = pd.Series(dfinstance.index)
 
     #GRAPH CUM_OBV
     plt.subplot(3,1,1)
     plt.bar(index_series,cum_obv_series)
     plt.title('Cumulative OBV')
 
     #graph volume
     plt.subplot(3,1,2)
     volume_series.plot()
     plt.title('volume')
     #graph price
     plt.subplot(3,1,3)
     price_series.plot()
     plt.title('price')
 
     plt.show()
 
 if __name__ == "__main__":
 
 
     test = OBV()
     init = test.initial_df()
     append = test.append_bool()
     calc = test.calc_obv_daily()
     calccum = test.calc_cum_daily_obv()
     dframe = test.dataframe
     print dframe
     dframe[['adj_close_price','daily_cum_obv','volume']] = dframe[['adj_close_price','daily_cum_obv','volume']].astype(float)
     graph_all(dframe)

