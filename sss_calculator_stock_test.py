import unittest
import pandas as pd
from sss_calculator import Stock

class Test_SSS_Calculator(unittest.TestCase):
    """Test class to calculate following features
    1. stock dividend yield
    2. stock p/e ratio """

    def setUp(self):
        """ set the sample data via pandas data frame"""
        stock_details_data = {
            'symbol':['TEA', 'POP', 'ALE', 'GIN', 'JOE'],
            'symbol_type':['Common', 'Common', 'Common', 'Preferred', 'Common'],
            'last_dividend':[0, 8, 23, 8, 13],
            'fixed_dividend':[0, 0, 0, 2, 0],
            'par_value':[100, 100, 60, 100, 250]
        }
        self.stock_details_df = pd.DataFrame( stock_details_data, columns=['symbol', 'symbol_type', 'last_dividend', 'fixed_dividend', 'par_value'] )


    def test_dividend_yield_common(self):
        """test dividend yield for the common stock
            from the sample values create object of Stock """
        stock_data = self.stock_details_df[self.stock_details_df['symbol']=='POP']
        stock = Stock(stock_data.symbol, stock_data.symbol_type, stock_data.par_value, stock_data.last_dividend, stock_data.fixed_dividend)
        self.assertTrue((8/218==stock.dividend_yield(218)).bool())
        self.assertTrue( ("POP"==stock.symbol).bool() )

    def test_dividend_yield_preferred(self):
        """test dividend yield for preferred stock"""
        stock_data = self.stock_details_df[self.stock_details_df['symbol']=='GIN']
        stock = Stock(stock_data.symbol, stock_data.symbol_type, stock_data.par_value, stock_data.last_dividend, stock_data.fixed_dividend)
        self.assertTrue((.02*100/218==stock.dividend_yield(218)).bool())
        self.assertTrue( ("GIN"==stock.symbol).bool() )

    def test_p_e_ratio(self):
        """test P/E ratio"""
        stock_data = self.stock_details_df[self.stock_details_df['symbol']=='POP']
        stock = Stock(stock_data.symbol, stock_data.symbol_type, stock_data.par_value, stock_data.last_dividend, stock_data.fixed_dividend)
        self.assertTrue((27.25==stock.pe_ratio(218)).bool())
        self.assertTrue( ("POP"==stock.symbol).bool() )

if __name__ == "__main__":
    unittest.main()
