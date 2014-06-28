import pandas as pd
import pandas.io.sql as psql
import MySQLdb as mdb
from user_input_mod import *


# Connect to the MySQL instance
db_host = 'localhost'
db_user = 'main_user'
db_pass = 'mainsql'
db_name = 'securities_master'
mycon= mdb.connect(db_host, db_user, db_pass, db_name)

start = get_start_date()
end = get_end_date()


#STOCK:

sql_stock = """SELECT dp.price_date, dp.adj_close_price, sym.ticker
         FROM symbol AS sym
         INNER JOIN daily_price AS dp
         ON dp.symbol_id = sym.id
         WHERE
         (dp.price_date BETWEEN
         {start_date} - INTERVAL 1 DAY AND {end_date})
         AND
         (sym.ticker = {ticker})
         ORDER BY dp.price_date ASC;""".format(ticker = get_ticker(), start_date = start, end_date = end)

#create initial data frame from query
stock_frame = psql.frame_query(sql_stock, con=mycon, index_col='price_date')

#append daily returns to dataframe
stock_frame['stck_returns'] = stock_frame.adj_close_price - stock_frame.adj_close_price.shift(1)

#append daily return percentage to the stock dataframe
stock_frame['stck_returnperc'] = ((stock_frame.stck_returns / stock_frame.adj_close_price.shift(1) ) * 100)

#INDEX:
sql_index = """SELECT idp.price_date, idp.adj_close_price, isym.ticker
         FROM index_symbol AS isym
         INNER JOIN index_daily_price AS idp
         ON idp.symbol_id = isym.id
         WHERE
         (idp.price_date BETWEEN
         {start_date} - INTERVAL 1 DAY AND {end_date})
         AND
         (isym.ticker = {ticker})
         ORDER BY idp.price_date ASC;""".format(ticker = get_index(), start_date = start, end_date = end)

#create initial data frame from query
index_frame = psql.frame_query(sql_index,  con=mycon, index_col='price_date')....

#append daily returns to dataframe
index_frame['index_returns'] = index_frame.adj_close_price - index_frame.adj_close_price.shift(1)

#append daily return percentage to the index dataframe
index_frame['index_returnperc'] = ((index_frame.index_returns / index_frame.adj_close_price.shift(1) ) * 100)

#ALPHA:

stock_series = stock_frame.stck_returnperc
index_series = index_frame.index_returnperc

daily_active_returns = pd.Series((stock_series - index_series), name='ActiveReturns')


alpha_average = (daily_active_returns.sum(skipna=True))/(daily_active_returns.count())
alpha_cumulative = daily_active_returns.sum(skipna=True)

print daily_active_returns
print "alpha average:", alpha_average
print "alpha cumulative", alpha_cumulative
