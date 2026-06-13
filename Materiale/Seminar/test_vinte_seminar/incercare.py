import numpy as np
import pandas as pd

# 1 ndarray
arr1=np.full((7,7),0,dtype=float)
arr1[0,:]=7
arr1[6,:]=7
arr1[:,0]=7
arr1[:,6]=7
np.fill_diagonal(arr1,33)
arr1[3,3]=77
print(arr1,type(arr1))

# 2

arr2=np.full((7,7),np.nan,float)
print(arr2)
arr2[:]=0
arr2[0,:]=5
arr2[6,:]=5
arr2[:,0]=5
arr2[:,6]=5
print(arr2)

# 3
vectSub=arr2[arr2==0];
arr3=np.ndarray((5,5),float,vectSub)
print(arr3, type(arr3))

# 4
vect_1=np.random.uniform(0,10,100)
print(vect_1)
pdSeries=pd.Series(vect_1,index=[f'L_{i+1}' for i in range(100)])
print(pdSeries)

#5
arr4=np.ndarray((11,5), float, buffer=np.random.uniform(0,10,55))
pdArray=pd.DataFrame(data=arr4,index=['L'+str(i+1) for i in range(11)],columns=['C'+str(i+1) for i in range(5)])
print(pdArray)

#6
dict_1={'S_'+str(i+1):[y for y in np.random.randint(1,10,7)] for i in range(8)}
print(dict_1)
df_1=pd.DataFrame(data=dict_1)
print(df_1)

#7
dict_2={'Stud'+str(i+1):[y for y in pd.Series(np.random.randint(1,10,5))] for i in range(7)}
print(dict_2)
df_2=pd.DataFrame(data=dict_2,index=['Ex'+str(i+1) for i in range(len(dict_2['Stud1']))])
print(df_2)

#8

series1=pd.read_csv('./dataIN/pokemon_data.csv');
series1=series1.iloc[:,1]
series2=pd.read_csv('./dataIN/pokemon_data.csv');
series2=series2.iloc[:,2]
dict_3={'Col1':series1,'Col2':series2}
df_3=pd.DataFrame(dict_3);
print(df_3)
print(series1,type(series1))

#9
dict_5={'Stud'+str(x+1):[t for t in np.random.randint(1,10,5) ] for x in range(8)}
dict_4={'An'+str(i+1): {'Stud'+str(x+1):[t for t in np.random.randint(1,10,5) ] for x in range(8)} for i in range(5)}
df_4=pd.DataFrame(dict_4)
print(df_4)
print(dict_5)

