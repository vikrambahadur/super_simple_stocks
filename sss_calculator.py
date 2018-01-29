import pandas as pd
import datetime
from datetime import datetime, timedelta
import math

class Stock(object):
    """ Stock represent entity against row of sample_data.csv.
    Stocks have the following attributes:
    Attributes:
        symbol: string represent stock name.
        stock_type: could be literal 'common' or 'preferred'.
        dividend: number of type double, in case of preferred stock its in % otherwise in absolute.
        par_value: number of type double.
        """
    def __init__(self, symbol, stock_type, par_value, last_dividend=0, fixed_dividend=0):
        """ return stock object initialized with name, type, dividend and par value"""
        self.symbol = symbol
        self.stock_type = stock_type
        if (self.stock_type=='Common').bool():
            self.dividend = last_dividend
        if (self.stock_type == 'Preferred').bool():
            self.dividend = fixed_dividend*par_value/100
        self.par_value = par_value

    def dividend_yield(self, market_price):
        """ return dividend yield on market price depend on type of stock"""
        return self.dividend / market_price

    def pe_ratio(self, market_price):
        """return price earning ration on current market price"""
        return market_price / self.dividend


class TradeBook(object):
    """trade book represent trades available in system at any point of time.
        having following attributes.
    Attributes:
        trade_data: type of pandas data frame"""
    def __init__(self, trade_data_df):
        #self.file_name = 'stock_prices.csv'
        self.trade_data = trade_data_df #pd.read_csv( 'stock_prices.csv', index_col=0, parse_dates=True ).sort_index()
        self.trade_data.index.name = 'timestamp'

    def record_trade(self, symbol, quantity, indicator, trade_price, timestamp = datetime.today()):
        #self.trade_data.append()
        new_vals = pd.DataFrame( {'symbol': symbol, 'quantity': quantity, 'indicator': indicator, 'price': trade_price},
                                 index=pd.to_datetime( [timestamp]))
        self.trade_data = self.trade_data.append( new_vals )

    def calculate_vwap(self, symbol, window_in_mins = 15):
        """1. filter the data rows available for given symbol for past 15 mins, if window_in_mins=0, ignore time window
           2. find vwap as cumulative sum of quantity*price divide by cumulative sum of quantity"""
        if window_in_mins == 0:
            symbol_df = self.trade_data.loc[self.trade_data["symbol"] == symbol].sort_index()
        else:
            symbol_df = self.trade_data.loc[self.trade_data["symbol"]==symbol].sort_index()\
            .between_time( *pd.to_datetime( [datetime.now() - timedelta( minutes=window_in_mins ), datetime.now()] ).time )

        symbol_df['vwap'] = (symbol_df['quantity'] * symbol_df['price']).cumsum() / symbol_df['quantity'].cumsum()

        return symbol_df

    def calculate_gbce(self):
        """calculation of index works in below steps
        step1: find the set of distinct available stock symbols in trade book
        step2: declare empty dictionary of key as symbol and value as price (most recent VWAP)
        step3: iterate over step1 found symbols, call calculate_vwap for each symbol
        step4: put into step2 dictionary most recent VWAP price against symbol
        step5: call private geomath to find geometric mean of all the prices
        """
        set_of_symbols = set( self.trade_data['symbol'].tolist() )
        symbol_price_dic = dict()
        for symbol in set_of_symbols:
            self.calculate_vwap( symbol, 0 )
            symbol_latest_vwap = self.calculate_vwap( symbol, 0 )['vwap'][-1]
            symbol_price_dic[symbol] = symbol_latest_vwap
        return self.__geomath(symbol_price_dic.values())

    def __geomath(self, iterable):
        """math module used to calculate the geometric mean."""
        return math.exp( sum( math.log( i ) for i in iterable ) / len( iterable ) )