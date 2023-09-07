import pandas as pd
from pyod.models.knn import KNN
import numpy as np
# Loading
credit_data = pd.read_csv('credit_data.csv')
credit_data.dropna(inplace=True)

# Detector
detector = KNN()
detector.fit(credit_data.iloc[:, 1:4])
predict = detector.labels_
outliers_amount = np.unique(predict, return_counts=True)
predict_confidence = detector.decision_scores_

outliers = []
for i in range(len(predict)):
    if predict[i] == 1:
        outliers.append(i)
list_outliers = credit_data.iloc[outliers, :]

print(f'Outliers amount: {outliers_amount}')
print(f'Predict confidence: {predict_confidence}')
print(f'Outliers Id: {outliers}')
print(f'\nlist of possible Outliers:\n{list_outliers}')
