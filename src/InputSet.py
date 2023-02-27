import numpy as np
import pandas as pd


class InputSet:

    def __init__(self, age, salary):
        array = np.array([[age, salary]])
        self.df = pd.DataFrame(data=array, columns=['Age', 'EstimatedSalary'])

    def preprocess(self, scaler):
        self.df = pd.DataFrame(data=scaler.transform(self.df), columns=['Age', 'EstimatedSalary'])
