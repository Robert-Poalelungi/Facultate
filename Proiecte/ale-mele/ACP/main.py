import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

# read csv
df = pd.read_csv("Freelancer.csv")

# replace na
for column in df.columns:
    if any(df[column].isna()):
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column].fillna(df[column].mean(), inplace=True)

        else:
            df[column].fillna(df[column].mode()[0], inplace=True)

# standardizare
coloane_standardizabile = df.columns[3:].values
standardizare = (
        (df[coloane_standardizabile] - np.mean(df[coloane_standardizabile], axis=0)) /
        np.std(df[coloane_standardizabile], axis=0))

# acp
acp_model = PCA()
acp_model.fit(standardizare)

# componentele principale (vectorii proprii) ale setului de date
componente = acp_model.components_

# varianta explicativa (valori proprii)
# = cata varianta a setului de date este explicata
# de fiecare componenta principala
varianta_explicativa = acp_model.explained_variance_

# varianta explicativa %
varianta_explicativa_ratio = acp_model.explained_variance_ratio_

# datele transformate pe componentele deja realizate
scor_componente = acp_model.transform(standardizare)

# Criteriul procentului de variație explicată
varianta_cumulativa_ratio = np.cumsum(varianta_explicativa_ratio)

# Criteriul Kaiser - pastrarea componentelor care au varianta mai mare decat 1
kaiser = [componente[i] for i in range(0, len(varianta_explicativa)) if varianta_explicativa[i] > 1]

kaiser2 = componente[:, varianta_explicativa > 1]  # cleaner

# Criteriul Cattell - cate componente sunt relevante
plt.plot(np.arange(1, len(varianta_explicativa) + 1), varianta_explicativa, marker='o')
plt.xlabel('Numărul de componente principale')
plt.ylabel('Autovaloare')
plt.title('Scree Plot')
plt.show()
