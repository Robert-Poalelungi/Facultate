import numpy as np
import pandas as pd

#1
data=np.fromfile('./dataIN/matrice_2.txt',dtype=int,sep=',')
print(data)
arr1=np.ndarray(shape=(6,5),dtype=int,buffer=data)
print(arr1)

#2
vect_1=np.random.uniform(-10,10,50)
series=pd.Series(data=vect_1,index=['R_'+str(i+1) for i in range(50)])
print(series)

#6
vect_2=np.random.uniform(-10,10,70)
arr2=np.ndarray((10,7),float,vect_2);
df_1=pd.DataFrame(arr2,index=['R'+str(i+1) for i in range(10)],columns=['C'+str(i+1) for i in range(7)])
print(df_1)

#4
arr3=np.full((7,7),9,float)
print(arr3)
arr3[:]=0
arr3[0,:]=5
arr3[6,:]=5
arr3[:,0]=5
arr3[:,6]=5
print(arr3)

#5
dict_1={'Stud_'+str(i+1):[y for y in np.random.randint(1,10,5)] for i in range(7)}
df_2=pd.DataFrame(dict_1)
print(df_2)

#6
data1=pd.read_csv('./dataIN/pokemon_data.csv')
data2=pd.read_csv('./dataIN/pokemon_data.csv')
series1=data1.iloc[:,1]
series2=data2.iloc[:,2]
dict_3={'Col1':series1,'Col2':series2}
df_4=pd.DataFrame(dict_3)
print(df_4)

#7
data3=pd.read_csv('./dataIN/pokemon_data.csv');
data3['RV']=(data3['Sp. Atk']-data3['Sp. Def'])/data3['Speed']
data3.to_csv('./dataIn/RV',index=False);


#8
dict_2={'An_'+str(i+1):{'Stud'+str(i+1):[y for y in np.random.randint(1,10,3)] for i in range(8)} for i in range(3)}
df_3=pd.DataFrame(dict_2)
print(df_3)

#9
arr4=np.full((7,7),0,float)
arr4[0,:]=4
arr4[6,:]=4
arr4[:,0]=4
arr4[:,6]=4
np.fill_diagonal(arr4,11)
arr4[3,3]=99
print(arr4)