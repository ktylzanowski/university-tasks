import pandas as pd

VARIETY = "variety"

#1
df = pd.read_csv("iris_with_errors.csv")
print(df.head())
print(f"Missing {df.isnull().sum().sum()}")
print(df.describe(include="all"))

#2
for column in df.columns:
    if column != VARIETY:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df.loc[(df[column] < 0) | (df[column] > 15), column] = df[column].mean()
print(df)
#3

print(df[VARIETY].unique())
variety_map = {'setosa': "Setosa", "Versicolour": "Versicolor", 'virginica': 'Virginica'}
df[VARIETY] = df[VARIETY].replace(variety_map)

print(df[VARIETY].unique())
