import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("iris_big.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=12)

results = {}

dt = DecisionTreeClassifier(random_state=12)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
results["Decision Tree"] = {
    "accuracy": accuracy_score(y_test, y_pred_dt),
    "confusion_matrix": confusion_matrix(y_test, y_pred_dt)
}

knn3 = KNeighborsClassifier(n_neighbors=3)
knn3.fit(X_train, y_train)
y_pred_knn3 = knn3.predict(X_test)
results["3-NN"] = {
    "accuracy": accuracy_score(y_test, y_pred_knn3),
    "confusion_matrix": confusion_matrix(y_test, y_pred_knn3)
}

knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, y_train)
y_pred_knn5 = knn5.predict(X_test)
results["5-NN"] = {
    "accuracy": accuracy_score(y_test, y_pred_knn5),
    "confusion_matrix": confusion_matrix(y_test, y_pred_knn5)
}

knn11 = KNeighborsClassifier(n_neighbors=11)
knn11.fit(X_train, y_train)
y_pred_knn11 = knn11.predict(X_test)
results["11-NN"] = {
    "accuracy": accuracy_score(y_test, y_pred_knn11),
    "confusion_matrix": confusion_matrix(y_test, y_pred_knn11)
}

nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
results["Naive Bayes"] = {
    "accuracy": accuracy_score(y_test, y_pred_nb),
    "confusion_matrix": confusion_matrix(y_test, y_pred_nb)
}

for clf_name, metrics in results.items():
    print(f"\n{clf_name}:")
    print(f"Dokładność: {metrics['accuracy']*100:.2f}%")
    print("Macierz błędów:")
    print(metrics["confusion_matrix"])

accuracies = {clf: metrics['accuracy'] for clf, metrics in results.items()}
best_clf = max(accuracies, key=accuracies.get)
print(f"\nNajlepszy klasyfikator: {best_clf} z dokładnością {accuracies[best_clf]*100:.2f}%")
