import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('D:/headbrain.csv')
X = data['Head Size(cm^3)']
Y = data['Brain Weight(grams)']
#this is using statistics library
model = sm.OLS(Y,X).fit()
predictions = model.predict(Y)
print_model = model.summary()
print(print_model)
