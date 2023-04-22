import pandas as pd

df = pd.read_csv('california_housing_train.csv')
min_population = df['population'].min()
data = df[df['population'] == min_population]['households'].max()
print('Максимальная households в зоне минимального значения population: ', data)
