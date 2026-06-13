import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import dendrogram

# Scree plot
def plot_scree(explained_variance_ratio, cumulative_variance):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(explained_variance_ratio) + 1), cumulative_variance, marker='o', label='Cumulative Variance')
    plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7, label='Individual Variance')
    plt.title('Explained Variance by Principal Components')
    plt.xlabel('Principal Components')
    plt.ylabel('Variance Explained')
    plt.axhline(y=0.85, color='r', linestyle='--', label='85% Variance Threshold')
    plt.legend()
    plt.grid()
    plt.show()

# Correlation circle
def plot_correlation_circle(factor_loadings, variable_names):
    plt.figure(figsize=(8, 8))
    for i, var in enumerate(variable_names):
        plt.arrow(0, 0, factor_loadings[i, 0], factor_loadings[i, 1], color='b', alpha=0.5)
        plt.text(factor_loadings[i, 0] * 1.15, factor_loadings[i, 1] * 1.15, var, color='g', ha='center', va='center')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Correlation Circle (PC1 vs PC2)')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.grid()
    plt.show()

# Countries in PC1-PC2 space
def plot_countries_in_pc_space(principal_components, country_names):
    plt.figure(figsize=(10, 7))
    plt.scatter(principal_components[:, 0], principal_components[:, 1], c='skyblue', edgecolor='k')
    for i, country in enumerate(country_names):
        plt.text(principal_components[i, 0], principal_components[i, 1], country, fontsize=9)
    plt.title('Countries in PC1-PC2 Space')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.grid()
    plt.show()

# Dendrogram
def plot_dendrogram(linkage_matrix, country_names):
    plt.figure(figsize=(12, 8))
    dendrogram(linkage_matrix, labels=country_names, leaf_rotation=90)
    plt.xticks(rotation=90)
    plt.title('Dendrogram (Hierarchical Agglomerative Clustering)')
    plt.xlabel('Countries')
    plt.ylabel('Distance')
    plt.grid()
    plt.show()

# Scatter plot with clusters
def plot_clusters(principal_components, clusters, country_names):
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x=principal_components[:, 0], y=principal_components[:, 1], hue=clusters, palette='viridis', s=100)
    for i, country in enumerate(country_names):
        plt.text(principal_components[i, 0], principal_components[i, 1], country, fontsize=9)
    plt.title('Clustered Countries in PC1-PC2 Space')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend(title='Cluster')
    plt.grid()
    plt.show()