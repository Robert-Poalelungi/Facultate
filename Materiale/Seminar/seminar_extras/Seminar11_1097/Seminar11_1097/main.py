import pandas as pd
from sklearn.model_selection import train_test_split

t = pd.read_csv("data_in/Hernia/hernia.csv",index_col=0)
variabile = list(t)
predictori = variabile[:-1]
tinta = variabile[-1]

x_train,x_test,y_train,y_test = train_test_split(
    t[predictori],t[tinta],test_size=0.2
)
