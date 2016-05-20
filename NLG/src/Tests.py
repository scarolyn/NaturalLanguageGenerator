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
                    'There was no change in the 10 year Treasury rates.')
        print('done with Treasury rates tests')
        # tests for swap rates
        self.assertEqual(NLG.day_compare('5yr_swap', '03-Jul-07', '05-Jul-07'),
                    'The 5 year swap rates sold off by 10bps.')
        self.assertEqual(NLG.day_compare('5yr_swap', '02-Jul-10', '06-Jul-10'),
                    'The 5 year swap rates rallied by 5bps.')
        print('done with swap rates tests')
        # tests for mortgages
        # both null compare
        self.assertEqual(NLG.day_compare('30_YR_Survey_Rate', '18-May-05', '19-May-05'),
                    'There was no change in the 30 year mortgage rate.')
        # one null compare
        self.assertEqual(NLG.day_compare('30_YR_Survey_Rate', '07-Jan-09', '08-Jan-09'),
                    'The 30 year mortgage rate sold off by 3bps.')
        # both available compare
        self.assertEqual(NLG.day_compare('30_YR_Survey_Rate', '23-Feb-09', '24-Feb-09'),
                    'The 30 year mortgage rate rallied by 2bps.')
        self.assertEqual(NLG.day_compare('30_YR_Survey_Rate', '23-May-11', '24-May-11'),
                    'The 30 year mortgage rate sold off by 7bps.')
        print('done with mortgage tests')
        # tests for spreads TODO should be a 2 difference thing!!
        print('done with spreads tests')

if __name__ == '__main__':
    unittest.main()