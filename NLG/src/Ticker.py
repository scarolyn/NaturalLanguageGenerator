class Ticker(object):

    def __init__(self, name):
        self._name = name
        if 'tsy' in name:
            self._type = 'interest'
            self._fullname = self.get_yr(name) + ' treasury rates'
            self._up_value = 'sold off'
            self._down_value = 'rallied'
        elif 'swap' in name:
            self._type = 'interest'
            self._fullname = self.get_yr(name) + ' swap rates'
            self._up_value = 'sold off'
            self._down_value = 'rallied'
        elif 'OAS' in name:
            self._type = 'spreads'
            self._fullname = name[3:7] + ' spread'
            self._up_value = 'widened'
            self._down_value = 'narrowed'
        elif 'Survey_Rate' in name:
            self._type = 'mortgage'
            self._fullname = '30 year mortgage rate'
            self._up_value = 'sold off'
            self._down_value = 'rallied'
        elif 'UST' in name:
            self._type = 'yield'
            self._fullname = 'difference between 2yr and 10yr yield'
            self._up_value = 'steepened'
            self._down_value = 'flattened'



    def get_yr(self, name):
        return str(name[0: int(name.index('yr'))]) + 'year'


