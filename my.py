'''import pandas as pd
s=pd.Series([1,2.5,'Ahosan'])
print(s)
data = [['Alex', 10], ['Ronald', 18], ['Jane', 33]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print('list')
print(df.to_dict(orient='list'))
print('************************************')
print('series')
print(df.to_dict(orient='series'))
print('************************************')
print('dict')
print(df.to_dict(orient='dict'))
print('************************************')
print('split')
print(df.to_dict(orient='split'))
print('************************************')
print('records')
print(df.to_dict(orient='records'))
print('************************************')
print('index')
print(df.to_dict(orient='index'))


import pandas as pd
data = {'Items': ['coins', 'pens', 'books'], 'Quantity': [22, 28, 3]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print(df.loc['A'])
print('-------------------------------')
print(df.loc[['A', 'B'], ['Items']])'''
import numpy as np
a =np.arange(10).reshape((2,5))
print(a)

A =np.ones((3,3))
print(A)




