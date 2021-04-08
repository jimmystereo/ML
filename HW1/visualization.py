import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels import iolib
import csv
# with open('./data/covid.train.csv', 'r') as fp:
#             data = list(csv.reader(fp))
#             data = np.array(data[1:])[:, 1:].astype(float)
#             target = data[:,-1]
df = pd.read_csv('./data/covid.train.csv')
df_test = pd.read_csv('./data/covid.test.csv')
Y = df['tested_positive.2']
arr=[]
for i in df.columns:
    if(i!='tested_positive.2'):
        arr.append(df[i])
X = sm.add_constant(df.loc[:, df.columns != 'tested_positive.2'])
est = sm.OLS(Y,X).fit()
est.summary()
Xt = sm.add_constant(df_test[:])
preds = est.predict(Xt)
with open('pred_stat.csv', 'w') as fp:
    writer = csv.writer(fp)
    writer.writerow(['id', 'tested_positive'])
    for i, p in enumerate(preds):
        writer.writerow([i, p])
df['tested_positive']