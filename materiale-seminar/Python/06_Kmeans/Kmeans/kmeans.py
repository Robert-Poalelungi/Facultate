import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

data = pd.read_csv('Mall_Customers.csv')
print(data.info())
print(data.head())
summary_statistics = data.describe()
print(summary_statistics)




df = data.copy()
# -------------------------------
# EXERCIȚIU 1: Medii pe gen
# -------------------------------
gender_group = df.groupby("Genre").agg({
    "Annual_Income_(k$)": "mean",
    "Spending_Score": "mean"
}).rename(columns={
    "Annual_Income_(k$)": "Mean_Income",
    "Spending_Score": "Mean_Spending_Score"
})
print("1. Venit și scor mediu pe gen:")
print(gender_group, '\n')


# -------------------------------
# EXERCIȚIU 2: Grupare pe decade de vârstă
# -------------------------------
df["Age_Group"] = pd.cut(df["Age"], bins=range(10, 71, 10), right=False)
age_group_stats = df.groupby("Age_Group").agg({
    "Annual_Income_(k$)": "mean",
    "Spending_Score": "mean",
    "CustomerID": "count"
}).rename(columns={"CustomerID": "Nr_Clients"})
print("2. Statistici pe decade de vârstă:")
print(age_group_stats, '\n')


# -------------------------------
# EXERCIȚIU 3: Gen x Categorie de venit
# -------------------------------
df["Income_Category"] = pd.cut(df["Annual_Income_(k$)"], bins=[0, 40, 70, 150],
                               labels=["Mic", "Mediu", "Mare"])
gender_income_group = df.groupby(["Genre", "Income_Category"]).agg({
    "Spending_Score": ["mean", "count"]
})
print("3. Intersecție Gen x Categorie Venit:")
print(gender_income_group, '\n')



# -------------------------------
# EXERCIȚIU 5: Top 5 grupuri demografice
# -------------------------------
top_groups = df.groupby(["Genre", "Income_Category"]).agg({
    "Spending_Score": "mean"
}).sort_values(by="Spending_Score", ascending=False).head(5)
print("5. Top 5 grupuri demografice cu Spending Score mare:")
print(top_groups)

'''
Visualizing Distributions of Numerical Variables

'''
fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # creates a figure and a 2x2 grid of subplots (axes) with the specified size.
fig.suptitle('Distribution of Numerical Variables')  # title


sns.histplot(data['Age'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Age Distribution')

sns.histplot(data['Annual_Income_(k$)'], bins=20, kde=True, ax=axes[0, 1])
axes[0, 1].set_title('Annual Income Distribution')

sns.histplot(data['Spending_Score'], bins=20, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Spending Score Distribution')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


'''
Pasul 1: Verificarea Valorilor Lipsă
Este esențial să verificăm dacă există valori lipsă în setul de date, deoarece acestea pot afecta performanța modelului. Dacă găsim astfel de valori, va trebui să decidem dacă le imputăm (înlocuim) sau le eliminăm.

Pasul 2: Codificarea Variabilelor Categorice
Modelele de învățare automată funcționează cu date numerice. Așadar, variabilele categorice, cum ar fi 'Genul', trebuie convertite într-un format numeric folosind tehnici precum codificarea One-Hot sau Label Encoding.

Pasul 3: Scalarea Caracteristicilor
Scalarea datelor este necesară, în special când folosim algoritmi care sunt sensibili la scala datelor, cum ar fi SVM sau KNN. Procesul implică standardizarea (aducerea la o distribuție cu media 0 și deviația standard 1) sau normalizarea (aducerea valorilor între 0 și 1) datelor.

Pasul 4: Detectarea Outlierilor
Outlierii sunt valori atipice care se abat semnificativ de la celelalte observații și pot influența negativ modelul. Trebuie identificați și gestionati, fie prin eliminare, fie prin alte metode de tratare a outlierilor.

Pasul 5: Analiza Corelației
Analizăm corelațiile dintre diferite variabile pentru a identifica relații posibile. Corelațiile puternice între variabile pot influența modelul, uneori indicând coliniaritate, ceea ce poate fi problematic pentru unele modele de învățare automată.


'''


# 1. Check for Missing Values
missing_values = data.isnull().sum()

print(missing_values)



# 2. Encode Categorical Variables ('Genre' is the only categorical variable)
print(data['Genre'])
data['Genre'] = data['Genre'].map({'Male': 0, 'Female': 1})  # Encoding 'Male' as 0 and 'Female' as 1
print(data['Genre'])

# 3. Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data.drop(['CustomerID'], axis=1)), columns=data.columns[1:])

# 4. Outlier Detection
sns.boxplot(data=data_scaled)
plt.title('Boxplot for Outlier Detection')
plt.show()

# 5. Correlation Analysis
correlation_matrix = data_scaled.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Heatmap for Correlation Analysis')
plt.show()



# using only Spending_Score and income variable for easy visualisation
X = data.iloc[:, [2, 3]].values
print (X)


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(x = range(1, 11), y = wcss,marker='o',color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)



# Visualising the clusters
plt.figure(figsize=(15,7))
sns.scatterplot(x = X[y_kmeans == 0, 0], y =X[y_kmeans == 0, 1], color = 'yellow', label = 'Cluster 1',s=50)
sns.scatterplot(x = X[y_kmeans == 1, 0], y = X[y_kmeans == 1, 1], color = 'blue', label = 'Cluster 2',s=50)
sns.scatterplot(x =X[y_kmeans == 2, 0], y = X[y_kmeans == 2, 1], color = 'green', label = 'Cluster 3',s=50)

sns.scatterplot(x= kmeans.cluster_centers_[:, 0], y = kmeans.cluster_centers_[:, 1], color = 'red',
                label = 'Centroids',s=300,marker=',')
plt.grid(False)
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# -----------------------------------------------------------
# Evaluarea modelului K-Means
# -----------------------------------------------------------

from sklearn.metrics import silhouette_score

# Silhouette Score
"""
Măsoară cât de apropiat este un punct de clusterul său comparativ cu celelalte clustere.
Scorul este între -1 și 1:

~1 → punctul este bine încadrat

~0 → este la graniță între clustere

< 0 → probabil este pus greșit în cluster"""
sil_score = silhouette_score(X, y_kmeans)
print(f"Silhouette Score: {sil_score:.4f}")

# Interpretare:
# +1 = clustere bine definite, 0 = la limită, <0 = atribuire greșită


for k in range(2, 11):
    km = KMeans(n_clusters=k, init='k-means++', random_state=42)
    preds = km.fit_predict(X)
    score = silhouette_score(X, preds)
    print(f'k = {k} --> silhouette score = {score:.4f}')