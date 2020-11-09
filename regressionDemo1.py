import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('D:/headbrain.csv')
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
#this is using sci-kit learn library

x=X.reshape(-1,1)
y=Y.reshape(-1,1)

model = LinearRegression(fit_intercept=True)

print(model.fit(x, y))
min_x = np.min(X)+100
max_x = np.max(X)+100
xfit = np.linspace(min_x, max_x, 1000)
yfit = model.predict(xfit.reshape(-1,1))
print("Model slope:    ", model.coef_[0])
print("Model intercept: ", model.intercept_)
