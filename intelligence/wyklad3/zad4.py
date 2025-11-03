import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("diabetes.csv")

for column in df.columns:
    if column in ['glucose-concentr', 'blood-pressure', 'skin-thickness', 'insulin']:
        nonzero = df.loc[df[column] != 0, column]
        if len(nonzero) > 0:
            mean_value = nonzero.mean()
            df.loc[df[column] == 0, column] = mean_value

if df['class'].dtype == object:
    df['class'] = df['class'].astype(str).str.strip().str.lower()
    df.loc[df['class'] == 'tested_positive', 'class'] = '1'
    df.loc[df['class'] == 'tested_negative', 'class'] = '0'

df['class'] = pd.to_numeric(df['class'], errors='coerce')
df = df.dropna(subset=['class']).copy()
df['class'] = df['class'].astype(int)

columns_to_normalize = [
    'pregnant-times', 'glucose-concentr', 'blood-pressure',
    'skin-thickness', 'insulin', 'mass-index', 'pedigree-func', 'age'
]

scaler = MinMaxScaler()
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

df = df.dropna(subset=columns_to_normalize).copy()

X = df[columns_to_normalize]
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "kNN (k=5)": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB(),
    "MLP (relu)": MLPClassifier(hidden_layer_sizes=(32,), activation='relu', max_iter=1500, random_state=42),
    "MLP (tanh)": MLPClassifier(hidden_layer_sizes=(64, 32), activation='tanh', max_iter=1500, random_state=42),
    "MLP (logistic)": MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', max_iter=1500, random_state=42),
}

accuracies = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    accuracies[name] = acc

    print("=" * 60)
    print(f"Model: {name}")
    print(f"Dokładność: {acc * 100:.2f}%")

    cm = confusion_matrix(y_test, y_pred)
    print("Macierz błędów:")
    print(cm)

    plt.figure(figsize=(4.5, 3.8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Pred 0', 'Pred 1'], yticklabels=['True 0', 'True 1'])
    plt.title(f"Macierz błędów - {name}")
    plt.xlabel("Predykcja")
    plt.ylabel("Rzeczywista")
    plt.tight_layout()
    plt.show()

labels = list(accuracies.keys())
values = [v * 100 for v in accuracies.values()]

plt.figure(figsize=(9, 5))
plt.bar(labels, values)
plt.ylabel("Dokładność [%]")
plt.xlabel("Klasyfikator")
plt.title("Porównanie dokładności klasyfikatorów (diabetes.csv)")
plt.xticks(rotation=20, ha='right')
plt.ylim(0, 100)
for i, v in enumerate(values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.show()

print("=" * 60)
print("Podsumowanie dokładności (%):")
for name, acc in accuracies.items():
    print(f"{name:20s}: {acc * 100:.2f}%")
