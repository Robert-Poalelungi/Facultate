import pandas as pd

pd.set_option("display.max_columns",None)

industria_alimentara = pd.read_csv("data_in/IndustriaAlimentara.csv",index_col=0)

industrii = list(industria_alimentara)[1:]

numar_angajati = industria_alimentara[industrii].apply(func=lambda x:x.sum(),axis=1)
# print(numar_angajati)
cerinta1 = industria_alimentara[numar_angajati>0]
cerinta1.to_csv("data_out/Cerinta1.csv")

procent_angajati = industria_alimentara[industrii].apply(func=lambda x:x/x.sum(),axis=1)
assert isinstance(procent_angajati,pd.DataFrame)
procent_angajati.insert(0,"Localitate",industria_alimentara["Localitate"])
procent_angajati.fillna(0,inplace=True)
procent_angajati.to_csv("data_out/Cerinta2.csv")

populatia = pd.read_csv("data_in/PopulatieLocalitati.csv",index_col=0)
industria_alimentara_loc = industria_alimentara.merge(populatia,left_index=True,right_index=True)

pondere_angajati =pd.DataFrame(industria_alimentara_loc[industrii+["Populatie"]].\
                    apply(func=lambda x:x[industrii].sum()/x["Populatie"],axis=1),columns=["PondereAngajati"])
pondere_angajati.insert(0,"Localitate",industria_alimentara_loc["Localitate_x"])
pondere_angajati.to_csv("data_out/pondere_angajati_loc.csv")
