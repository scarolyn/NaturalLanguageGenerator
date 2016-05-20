import unittest

import NLG


class Tests(unittest.TestCase):

    def test_daycompare(self):
        # tests for 2yr 10yr diff
        self.assertEqual(NLG.day_compare('2yr-10yr_UST', '09-Jun-05', '10-Jun-05'),
                         'The difference between 2yr and 10yr yield steepened by 1bps.')
        self.assertEqual(NLG.day_compare('2yr-10yr_UST', '14-Nov-05', '15-Nov-05'),
                         'The difference between 2yr and 10yr yield flattened by 3bps.')
        print('done with 2yr 10yr diff tests')
        # tests for Treasury rates
        self.assertEqual(NLG.day_compare('10yr_tsy', '19-May-05', '20-May-05'),
                         'The 10 year Treasury rates sold off by 2bps.')
        self.assertEqual(NLG.day_compare('10yr_tsy', '25-Jan-10', '26-Jan-10'),
                         'The 10 year Treasury rates rallied by 0bps.')
        print('done with Treasury rates tests')
        # tests for swap rates
        print('done with swap rates tests')
        # tests for mortgages
        print('done with mortgage tests')
        # tests for spreads
        print('done with spreads tests')

if __name__ == '__main__':
    unittest.main()