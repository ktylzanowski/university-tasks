from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

features = ['sepal length (cm)', 'sepal width (cm)']
x_selected = x[features]

scaler_minmax = MinMaxScaler()
x_minmax = scaler_minmax.fit_transform(x_selected)

scaler_z = StandardScaler()
x_zscore = scaler_z.fit_transform(x_selected)


def plot_scatter(data, title):
    plt.figure(figsize=(8, 6))
    for i, target_name in enumerate(iris.target_names):
        plt.scatter(data[y == i, 0], data[y == i, 1], label=target_name)
    plt.xlabel(features[0])
    plt.ylabel(features[1])
    plt.title(title)
    plt.legend()
    plt.show()


plot_scatter(x_selected.values, "Oryginalne dane")
plot_scatter(x_minmax, "Dane znormalizowane Min-Max")
plot_scatter(x_zscore, "Dane zeskalowane Z-score")

print("Statystyki dla oryginalnych danych (sepal length i width):")
print(x_selected.describe())


# By ai
# prompt: Treść zadania

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Wczytanie danych Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Wybieramy dwie zmienne
x_col = 'sepal length (cm)'
y_col = 'sepal width (cm)'

# Normalizacja Min-Max
scaler_minmax = MinMaxScaler()
df_minmax = df.copy()
df_minmax[[x_col, y_col]] = scaler_minmax.fit_transform(df[[x_col, y_col]])

# Skalowanie z-score
scaler_std = StandardScaler()
df_zscore = df.copy()
df_zscore[[x_col, y_col]] = scaler_std.fit_transform(df[[x_col, y_col]])

# Funkcja do rysowania wykresu
def plot_iris(df_plot, title):
    plt.figure(figsize=(6, 4))
    for species in df_plot['species'].unique():
        subset = df_plot[df_plot['species'] == species]
        plt.scatter(subset[x_col], subset[y_col], label=species)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.legend()
    plt.show()

# Wykresy
plot_iris(df, "Irysy - oryginalne dane")
plot_iris(df_minmax, "Irysy - normalizacja Min-Max")
plot_iris(df_zscore, "Irysy - skalowanie z-score")
