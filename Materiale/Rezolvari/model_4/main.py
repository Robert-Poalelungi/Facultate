import pandas as pd

industrie = pd.read_csv("Industrie.csv", index_col = 1)
populatie = pd.read_csv("PopulatieLocalitati.csv", index_col = 1)

industrie = industrie.merge(populatie[["Judet","Populatie"]], left_index=True, right_index=True)

lista = ["Alimentara", "Textila", "Lemnului", "ChimicaFarmaceutica",
              "Metalurgica", "ConstructiiMasini", "CalculatoareElectronica",
              "Mobila", "Energetica"]

# cerinta 1
# - ca totala la nivel de localitate

industrie["Total"] = industrie[lista].sum(axis=1)

industrie.reset_index(inplace= True)

cerinta1 = industrie[["Siruta", "Localitate", "Total"]]

cerinta1 = cerinta1.sort_values(by="Total", ascending=False)

cerinta1.to_csv("Cerinta1.csv", index=False)


# cerinta 2
# - activitatea cu cea mai mare cifra de afaceri pe localitate

industrie.reset_index(inplace= True)

industrie["ActivitateDominanta"] = industrie[lista].idxmax(axis=1)

cerinta2 = industrie[["Siruta", "Localitate", "ActivitateDominanta"]]

cerinta2.to_csv("Cerinta2.csv", index=False)


# cerinta 3
# - cifra de afaceri pe locuitor la nivel de județ

industrie_1 = industrie.groupby("Judet").agg({"Total": "sum", "Populatie": "sum"})

# Împărțim cifra de afaceri totală a județului la populația totală a județului
industrie_1["CifraAfaceriPeLocuitor"] = industrie_1["Total"] / industrie_1["Populatie"]

cerinta3 = industrie_1[["CifraAfaceriPeLocuitor"]].reset_index()

cerinta3.to_csv("Cerinta3.csv", index=False)


# cerinta 4
# - pentru fiecare judet, localitatea cu ca max pe locuitor

industrie["CifraAfaceriPeLocuitor"] = industrie["Total"] / industrie["Populatie"]

cerinta4 = industrie.loc[industrie.groupby("Judet")["CifraAfaceriPeLocuitor"].idxmax(), ["Judet", "Siruta"]]

cerinta4.to_csv("Cerinta4.csv", index=False)


# cerinta 5
# - grafic

import matplotlib.pyplot as plt

# Folosim cerinta1 deja calculată și sortată descrescător
primele50 = cerinta1.head(50)

# Creăm graficul
plt.figure(figsize=(15,6))
plt.bar(primele50["Localitate"], primele50["Total"], color='skyblue')

plt.xticks(rotation=90)  # rotim numele localităților pentru lizibilitate
plt.xlabel("Localitate")
plt.ylabel("Cifra de afaceri totală")
plt.title("Cifra de afaceri totală pentru primele 50 de localități")
plt.tight_layout()  # pentru a nu tăia etichetele

plt.show()



















