from pandas import DataFrame

class DataSet:
    _df = DataFrame()
    
    def __init__(self):
        pass
    
    def getDf(self):
        return self._df
