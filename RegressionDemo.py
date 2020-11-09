import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('D:/headbrain.csv')
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

#calculating x_bar and y _bar
x_bar = np.mean(X)
y_bar = np.mean(Y)

n = len(X)

numer=0
denom=0
for i in range(n):
    numer +=(X[i]-x_bar)*(Y[i]-y_bar)
    denom +=(X[i]-x_bar)**2

beta1 = numer/denom
beta0 = y_bar-(beta1*x_bar)

print('Coefficeint: ',beta1)
print('Coefficeint: ',beta0)

max_x = np.max(X)+100
min_x = np.min(X)+100


x_line = np.linspace(min_x,max_x,1000)
y_line = (beta0+beta1*x_line)

#Lets predict Some value now

newX = float(input('Enter Size of the Head: ' ))
newY = beta0+(beta1*newX)
print('Predcited Brain Size = ',newY)


#Lets plot the result
plt.plot(x_line,y_line)
plt.scatter(X,Y)
plt.show()


















