from DataSet import DataSet
from sklearn.preprocessing import StandardScaler

class NormalizeDataSet(DataSet):
    def __init__(self):
        super().__init__()
    
    def normalize(self):
        std_scaler = StandardScaler()
        scaler = std_scaler.fit(self._df)
        self._df = scaler.transform(self._df)
