import numpy as np
import  pandas as pd

arr1=np.full((7,7),0,float)

arr1[0,:]=7
arr1[6,:]=7
arr1[:,0]=7
arr1[:,6]=7
np.fill_diagonal(arr1,33)
arr1[3,3]=77
print(arr1)

arr2=np.full((7,7),np.nan,float)
print(arr2)
arr2[:]=0
arr2[0,:]=5
arr2[6,:]=5
arr2[:,0]=5
arr2[:,6]=5
print(arr2)

arr3=np.ndarray((5,5),float,arr2[arr2==0])
print(arr3)

vect_1=np.random.uniform(0,10,100)
series=pd.Series(data=vect_1,index=['L_'+str(i+1) for i in range(100)])
print(series)

vect_2=np.random.uniform(0,10,55)
arr4=np.ndarray((11,5),float,vect_2)
df_1=pd.DataFrame(data=arr4,index=['L'+str(i+1) for i in range(11)], columns=['C'+str(i+1) for i in range(5)])
print(df_1)

dict_1={'S_'+str(i+1):[y for y in np.random.randint(1,10,7)] for i in range(8)}
df_2=pd.DataFrame(data=dict_1)
print(df_2)

dict_2={'Stud'+str(i+1):[y for y in pd.Series(np.random.randint(1,10,5))] for i in range(7)}
df_3=pd.DataFrame(dict_2,index=['Ex'+str(i+1) for i in range(5)])
print(df_3)

data1=pd.read_csv('./dataIN/pokemon_data.csv')
data2=pd.read_csv('./dataIN/pokemon_data.csv')
series1=data1.iloc[:,1]
series2=data2.iloc[:,2]
dict_3={'Col1':series1,'Col2':series2}
df_4=pd.DataFrame(dict_3)
print(df_4)


