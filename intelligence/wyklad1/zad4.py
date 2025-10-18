from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

pca_full = PCA().fit(x)

variances = pca_full.explained_variance_
total_variance = np.sum(variances)

cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_)
print(cumulative_variance)

num_components_95 = np.argmax(cumulative_variance >= 0.95) + 1
print(num_components_95)

removed_variance = np.sum(variances[num_components_95:])
info_loss = removed_variance / total_variance
print(info_loss)

num_columns_to_remove = len(variances) - num_components_95
print(num_columns_to_remove)

pca = PCA(n_components=num_components_95)
x_pca = pca.fit_transform(x)

if num_components_95 == 2:
    plt.figure(figsize=(8, 6))
    for i, target_name in enumerate(iris.target_names):
        plt.scatter(x_pca[y == i, 0], x_pca[y == i, 1], label=target_name)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA Iris - 2D")
    plt.legend()
    plt.show()

elif num_components_95 == 3:
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    for i, target_name in enumerate(iris.target_names):
        ax.scatter(x_pca[y == i, 0], x_pca[y == i, 1], x_pca[y == i, 2], label=target_name)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_zlabel("PC3")
    ax.set_title("PCA Iris - 3D")
    ax.legend()
    plt.show()
