from DataSet import DataSet
from pandas import read_csv

class CSVDataSetBuilder(DataSet):
    _path_to_csv = ""
    
    def __init__(self, path_to_csv):
        super().__init__()
        self._path_to_csv = path_to_csv
    
    def __build(self):
        self._df = read_csv(self._path_to_csv)
