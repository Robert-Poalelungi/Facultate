import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from pca import PCA
from graphics import plot_scree, plot_correlation_circle, plot_countries_in_pc_space, plot_clusters
from cluster.cluster import hclust

# Incarcare set de date
file_path = './dateIN/date.xlsx'
data = pd.read_excel(file_path)

# Selectarea coloanelor numerice pentru PCA
numerical_data = data.drop(columns=['Country'])

# Standardizarea datelor
scaler = StandardScaler()
standardized_data = scaler.fit_transform(numerical_data)

# Aplicarea PCA folosind clasa furnizata
pca = PCA.PCA(standardized_data)

# Extragerea rezultatelor din clasa PCA
principal_components = pca.getPrincipalComponents()
factor_loadings = pca.getFactorLoadings()
explained_variance = pca.getEigenvalues()
communalities = pca.getCommunalities()

# Scree plot
explained_variance_ratio = explained_variance / np.sum(explained_variance)
cumulative_variance = np.cumsum(explained_variance_ratio)
plot_scree(explained_variance_ratio, cumulative_variance)

# Cerc de corelatie
plot_correlation_circle(factor_loadings, numerical_data.columns)

# Reprezentarea tarilor in planul PC1-PC2
plot_countries_in_pc_space(principal_components, data['Country'])

# Clusterizare ierarhica folosind clasa hclust
cluster_model = hclust(t=data.set_index('Country'), variabile=numerical_data.columns.tolist(), metoda="ward")
cluster_model.plot_ierarhie()

# Adaugarea clusterelor la date
data['Cluster'] = cluster_model.p

# Reprezentarea grafica a clusterelor
plot_clusters(principal_components, data['Cluster'], data['Country'])

# Salvarea datelor in fisier
output_file = './dateOUT/clustered_data.xlsx'
data.to_excel(output_file, index=False)
print(f"Clustered data saved to {output_file}")
