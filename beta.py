import pandas.io.sql as psql
import MySQLdb as mdb
import numpy as np
from user_input_mod import *
import pandas as pd
mycon= mdb.connect('localhost', 'main_user', 'mainsql', 'securities_master')

print "BETA TEST"


#STOCK:
sql_stock = """SELECT dp.price_date, dp.adj_close_price, sym.ticker
         FROM symbol AS sym
         INNER JOIN daily_price AS dp
         ON dp.symbol_id = sym.id
         WHERE
         (dp.price_date BETWEEN.
         {start_date} - INTERVAL 1 DAY AND {end_date})
         AND
         (sym.ticker = {ticker})
         ORDER BY dp.price_date ASC;""".format(ticker = get_ticker(), start_date = get_start_date(), end_date = get_end_date())

#create initial pandas data frame from query
stock_frame = psql.frame_query(sql_stock, con=mycon, index_col='price_date')

#append daily returns to dataframe
daily_stock_ret= pd.Series(stock_frame.adj_close_price - stock_frame.adj_close_price.shift(1))



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
         ORDER BY idp.price_date ASC;""".format(ticker = get_index(), start_date = get_start_date(), end_date = get_end_date())

#create initial data frame from query
index_frame = psql.frame_query(sql_index,  con=mycon, index_col='price_date')


#daily_index_returns
daily_ind_ret= pd.Series(index_frame.adj_close_price - index_frame.adj_close_price.shift(1))


 #BETA:
 
 var_tick = daily_stock_ret.var()
 
 var_ind = daily_ind_ret.var()
 
 covar = daily_stock_ret.cov(daily_ind_ret)
 
 beta = var_ind/covar
 
 
 print "BETA: ", beta
 
 
 #compute R-squared
 R2 = 0.0
 R2 = (covar*covar)/(var_ind*var_tick)
 print "R-squared=",R2
