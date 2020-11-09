import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('D:/headbrain.csv')
#print(data.head())
#print(data.tail())

X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values

mean_X=np.mean(X)
mean_Y=np.mean(Y)

n=len(X)
numer=0
denom=0
for i in range(n):
    numer+=(X[i]-mean_X)*(Y[i]-mean_Y)
    denom+=(X[i]-mean_X)**2
b1=numer/denom
print('intercept=',b1)
b0=mean_Y-(b1*mean_X)
print('Slop =',b0)
max_x=np.max(X)+100
min_x=np.min(X)+100

x=np.linspace(min_x,max_x,1000)
y= b0+(b1*x)

plt.plot(x,y)
plt.scatter(X,Y)
plt.xlabel('Head Size')
plt.xlabel('Brain Weight')
           
plt.show()







