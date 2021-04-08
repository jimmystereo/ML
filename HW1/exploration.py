import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import normalize
df = pd.read_csv('./data/covid.train.csv').columns
df.shape
target_column = df[-1]
df = df[0:-1]
df
column_index = list(range(-1,len(df)-1))
len(column_index)
len(column_index)
from numpy import genfromtxt
my_data = genfromtxt('./data/covid.train.csv', delimiter=',')[1::,:]
target = my_data[:,-1]
my_data = my_data[:,0:-1]
target.shape
my_data.shape
my_data[:,1].shape
my_data[1::,41:-1].shape
# sns.heatmap(np.corrcoef(my_data[1::,41::]))
rel = []
for i in range(my_data.shape[1]):
    # x = [p**2 for p in my_data[:,i]]
    x = my_data[:,i]
    x = x/ np.linalg.norm(x)
    cor = np.corrcoef(x,target)[0][1]
    rel.append(cor)

abs_rel = [abs(x) for x in rel]
column_index_df = pd.DataFrame(column_index,columns=['or_index'])
columns = pd.DataFrame(df,columns=['name'])
df_rel_or = pd.DataFrame(abs_rel,columns=['rel'])
df_rel = pd.concat([column_index_df,columns,df_rel_or],axis=1)
res = df_rel.sort_values(ascending=False,by = "rel")
print(res)