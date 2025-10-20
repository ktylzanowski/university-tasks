import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv("iris_big.csv")

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=12)

print("Zbiór treningowy (X_train):")
print(X_train[:5])
print("Zbiór treningowy (y_train):")
print(y_train[:5])

print("\nZbiór testowy (X_test):")
print(X_test[:5])
print("Zbiór testowy (y_test):")
print(y_test[:5])

clf = DecisionTreeClassifier(random_state=12)

clf.fit(X_train, y_train)

print("\nDrzewo decyzyjne (tekstowo):")
print(export_text(clf, feature_names=df.columns[:-1].tolist()))

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nDokładność klasyfikatora: {accuracy*100:.2f}%")

cm = confusion_matrix(y_test, y_pred)
print("\nMacierz błędów:")
print(cm)

plt.figure(figsize=(20,10))
plot_tree(clf, feature_names=df.columns[:-1], class_names=clf.classes_, filled=True)
plt.show()
