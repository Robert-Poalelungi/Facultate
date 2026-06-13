import numpy as np
import pandas as pd

#1
arr_1=np.full((7,7),44,int)
print(arr_1)
arr_2=arr_1.astype(float)
print(arr_2)
arr_2[:]=4
arr_2[0,:]=88
arr_2[6,:]=88
arr_2[:,0]=88
arr_2[:,6]=88
print(arr_2)
#2
arr_3=np.full((7,7),4,float)
arr_3[0,:]=7
arr_3[6,:]=7
arr_3[:,0]=7
arr_3[:,6]=7
np.fill_diagonal(arr_3,33)
arr_3[3,3]=777
print(arr_3)
#3
df_1=pd.read_csv('./dataINTest/GS.csv')
PMPV=(df_1['Close']*df_1['Volume']).sum()/df_1['Volume'].sum()
df_1['Abatere']=(df_1['Close']-PMPV)/df_1['Close']
df_1.to_csv('./dataINTest/GS_PMPV.csv',index=False);
#4
vect_1=np.random.uniform(0,20,70)
series=pd.Series(data=vect_1,index=['L_'+str(i+1) for i in range(70)])
print(series)
#5
vect_2=np.random.uniform(-10,10,72)
arr_4=np.ndarray((12,6),float,vect_2)
df_2=pd.DataFrame(arr_4,index=['L'+str(i+1) for i in range(12)],columns=['C'+str(i+1) for i in range(6)])
print(df_2)
#6
dict_1={'S_'+str(i+1):[y for y in np.random.randint(1,10,7)] for i in range(8)};
df_3=pd.DataFrame(dict_1)
print(df_3)
#7
dict_2={'Stud'+str(i+1):[y for y in pd.Series(np.random.randint(1,10,5))] for i in range(7)};
df_4=pd.DataFrame(dict_2,index=['Ex'+str(i+1) for i in range(5)])
print(df_4)
#8
data1=pd.read_csv('./dataINTest/Seria_1.csv');
print(data1)
data2=pd.read_csv('./dataINTest/Seria_2.csv');
print(data2)
serie1=data1.set_index('Label')['Val']
serie2=data2.set_index('Label')['Val']
dict_3={'Col1':serie1,'Col2':serie2}
df_5=pd.DataFrame(dict_3).reset_index(drop=True)
print(df_5)
#9
dict_4={'An'+str(i+1): {'Stud'+str(i+1):[y for y in pd.Series(np.random.randint(1,10,5))] for i in range(12)} for i in range(5)}
df_6=pd.DataFrame(dict_4)
print(df_6)
#txt

data_txt=np.loadtxt('./dataINTest/matrice_34.txt',delimiter=';',dtype=int)
print(data_txt,type(data_txt))
with open("./dataINTest/matrice_32.txt","r") as file:
    txt=file.read().replace("\n",",")
txt_array=np.fromstring(txt,dtype=int,sep=",")
matrice = np.ndarray(shape=(7,6),dtype=int,buffer=txt_array)
print(matrice)
