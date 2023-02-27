# importing libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, f1_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# class for the model
class Model:

    def __init__(self, x, y, test_rat):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(x, y, test_size=test_rat)
        self.random_forest_model = RandomForestClassifier()

    def train(self):
        self.random_forest_model.fit(self.X_train, self.y_train)

    def test(self):
        return self.random_forest_model.predict(self.X_test)

    def predict(self, x_input):
        return self.random_forest_model.predict(x_input)
