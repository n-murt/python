import pandas as pd

df = pd.read_csv('california_housing_train.csv')

data = df[(df['population'] <= 500) & (df['population'] >= 0)]['median_house_value'].mean()
print('Средняя стоимость дома: ', data)
