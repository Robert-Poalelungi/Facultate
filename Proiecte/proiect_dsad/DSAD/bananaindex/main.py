import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Încărcarea datelor
df = pd.read_csv('./bananaindex.csv')

######################
# ANALIZA DE CLUSTER #
######################

# Selectarea caracteristicilor pentru clusterizare
features = df[['emissions_kg', 'land_use_kg']]

# Normalizarea datelor
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Aplicarea K-means pentru clusterizare
kmeans = KMeans(n_clusters=3, n_init=10)
clusters = kmeans.fit_predict(scaled_features)

# Adăugarea etichetelor clusterului în DataFrame
df['cluster'] = clusters

# Vizualizarea rezultatelor
plt.figure(figsize=(10, 6))
plt.scatter(df['emissions_kg'], df['land_use_kg'], c=df['cluster'], cmap='viridis')
plt.xlabel('Emissions (kg)')
plt.ylabel('Land Use (kg)')
plt.title('Clusterizarea Alimentelor pe Baza Emissiilor și Utilizării Terenului')

# Adăugarea etichetelor
for i, txt in enumerate(df['entity']):
    plt.annotate(txt, (df['emissions_kg'][i], df['land_use_kg'][i]), fontsize=8, alpha=0.75)

plt.show()
df.to_csv('./dateOUT/cluster_analysis.csv', index=False)

##########################################
# Analiza Componentelor Principale (PCA) #
##########################################

# Selectarea coloanelor pentru PCA
pca_features = df[['Bananas index (kg)', 'Bananas index (1000 kcalories)', 'Bananas index (100g protein)']]

# Normalizarea datelor pentru PCA
pca_scaler = StandardScaler()
scaled_pca_features = pca_scaler.fit_transform(pca_features)

# Aplicarea PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_pca_features)

# Crearea unui nou DataFrame pentru componente
pca_df = pd.DataFrame(data = principal_components, columns = ['Indice eficienta emisii', 'Impact proteic al emisiilor'])
pca_df['entity'] = df['entity']

# Vizualizarea PCA
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Indice eficienta emisii', y='Impact proteic al emisiilor', data=pca_df, hue=df['cluster'], palette='viridis')
plt.title('PCA Analysis of Banana Index')

# Adăugarea etichetelor
for i in range(pca_df.shape[0]):
    plt.text(pca_df['Indice eficienta emisii'][i], pca_df['Impact proteic al emisiilor'][i], pca_df['entity'][i], fontsize=8, alpha=0.75)
plt.show()
pca_df.to_csv('./dateOUT/pca_analysis.csv', index=False)