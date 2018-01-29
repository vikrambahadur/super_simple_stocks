import unittest
import pandas as pd
from sss_calculator import TradeBook

class Test_SSS_Calculator_Trade_Book(unittest.TestCase):
    """ Test class to test Trade book functions"""

    def setUp(self):
        """read the stock prices and initialize the trade book data frame"""
        self.tradeBook = TradeBook( pd.read_csv( 'stock_prices.csv', index_col=0, parse_dates=True ).sort_index() )


    def test_calculate_vwap(self):
        """calculate vwap for all the timestamps for symbol AAPL and test most recent value
        In case of 15 mins past windows size, second param value could be set to 15"""
        self.assertTrue(126.35994216, self.tradeBook.calculate_vwap("AAPL",0)['vwap'][-1])

    def test_record_trade(self):
        """test recoding of trade via trade book record_trade function
        assert count of available orders before and after recording of order"""
        self.assertEqual(3, len(self.tradeBook.trade_data), "Size of book before new trade record")
        self.tradeBook.record_trade('BBL', 3578, 'B', 23.21, '2018-01-29 00:30:57')
        self.assertEqual( 4, len( self.tradeBook.trade_data ), "Size of book after new trade record" )

    def test_gbce_index_via_gm(self):
        """test index for basket of stocks via trade book function calculate_gbce"""
        self.assertEqual(50.12021199211952, self.tradeBook.calculate_gbce(), "Index of stocks via geometric mean")


if __name__ == "__main__":
    unittest.main()
