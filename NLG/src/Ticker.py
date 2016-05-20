class Ticker(object):

    def __init__(self, name):
        self._name = name
        if 'tsy' in name:
            self._type = 'interest'
            self._fullname = self.get_yr(name) + ' Treasury Yield'
            self._up_value = 'sold-off'
            self._down_value = 'rallied'
        elif 'swap' in name:
            self._type = 'interest'
            self._fullname = self.get_yr(name) + ' Swap Rate'
            self._up_value = 'sold-off'
            self._down_value = 'rallied'
        elif 'OAS' in name:
            self._type = 'spreads'
            self._fullname = 'Fannie ' + name[3:7] + ' Coupon spread'
            self._up_value = 'widened'
            self._down_value = 'narrowed'
        elif 'Survey_Rate' in name:
            self._type = 'mortgage'
            self._fullname = 'Mortgage Rate'
            self._up_value = 'sold-off'
            self._down_value = 'rallied'
        elif 'UST' in name:
            self._type = 'yield'
            self._fullname = '2-10 Treasury curve'
            self._up_value = 'steepened'
            self._down_value = 'flattened'



    def get_yr(self, name):
        return str(name[0: int(name.index('yr'))]) + ' year'


