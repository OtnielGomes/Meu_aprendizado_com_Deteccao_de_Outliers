import pandas as pd
import plotly.express as px

# Loading
credit_data = pd.read_csv('credit_data.csv')
print(credit_data)
print(credit_data.isnull().sum())
credit_data.dropna(inplace=True)
print(credit_data.isnull().sum())

# Outliers Box Plot
graphic = px.box(credit_data, y='age')
graphic.show()
outliers_age = credit_data[credit_data['age'] < 0]
print(f'\nOutliers age: \n{outliers_age}')

graphic = px.box(credit_data, y='loan')
graphic.show()
outliers_loan = credit_data[credit_data['loan'] > 13300]
print(f'\nOutliers loan: \n{outliers_loan}')

graphic = px.box(credit_data, y='income')
graphic.show()
print('\nOutliers income is False')

# Outliers scatter graphic
# income x age
graphic = px.scatter(x=credit_data['income'], y=credit_data['age'])
graphic.show()

# income x loan
graphic = px.scatter(x=credit_data['income'], y=credit_data['loan'])
graphic.show()

# age x loan
graphic = px.scatter(x=credit_data['age'], y=credit_data['loan'])
graphic.show()

