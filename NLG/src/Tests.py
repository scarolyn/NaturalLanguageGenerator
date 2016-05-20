import unittest

import NLG


class Tests(unittest.TestCase):

    def test_daycompare(self):
        # tests for 2yr 10yr diff
        self.assertEqual(NLG.day_compare('2yr-10yr_UST', '09-Jun-05', '10-Jun-05'),
                         'The difference between 2yr and 10yr yield steepened by 1 bps.')
        print('done');
        # tests for rates
        #self.assertEqual(NLG.day_compare(''), )
        #tests for

if __name__ == '__main__':
    unittest.main()