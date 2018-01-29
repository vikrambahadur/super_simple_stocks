# SSS - Super Simple Stocks application https://github.com/vikrambahadur/super_simple_stocks

## Code Description
Required python version is 3.6.3,

Class Stock location https://github.com/vikrambahadur/super_simple_stocks/blob/master/sss_calculator.py serves stock functionality
on available stock details data these are
a) Calculate dividend_yield and
b) Calculate pe_ratio on market price.

Class TradeBook location https://github.com/vikrambahadur/super_simple_stocks/blob/master/sss_calculator.py serves trade book functionality
on trade data these are
a) record_trade - To record/capture new trade into trading system
b) calculate_vwap - To calculate stock VWAP
    1. filter the data rows available for given symbol for past 15 mins, if window_in_mins=0, ignore time window
    2. find vwap as cumulative sum of quantity*price divide by cumulative sum of quantity
c) calculate_gbce
    Calculation of index works in below steps
    step1: find the set of distinct available stock symbols in trade book
    step2: declare empty dictionary of key as symbol and value as price (most recent VWAP)
    step3: iterate over step1 found symbols, call calculate_vwap for each symbol
    step4: put into step2 dictionary most recent VWAP price against symbol
    step5: call private geomath to find geometric mean of all the prices



## Unit Testing
Class Test_SSS_Calculator location https://github.com/vikrambahadur/super_simple_stocks/blob/master/sss_calculator_stock_test.py
provides unit testing of stock functionalities, available test cases are
a) test_dividend_yield_common
b) test_dividend_yield_preferred and
c) test_p_e_ratio

Class Test_SSS_Calculator_Trade_Book location https://github.com/vikrambahadur/super_simple_stocks/blob/master/sss_calculator_trade_book_test.py
provides unit testing of trade book functionalities, its initialize trade book dataframe with the help of CSV file stock_prices.csv

timestamp,indicator,price,quantity,symbol
2018-01-28 19:12:49.000000,B,127.21,36761000,AAPL
2018-01-28 19:12:45.000000,S,125.9,67941100,AAPL
2018-01-29 00:30:57.495412,B,19.88,20,BBL

available test cases are
a) test_calculate_vwap
b) test_record_trade and
c) test_gbce_index_via_gm