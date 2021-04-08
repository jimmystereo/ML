import numpy as np
df = np.loadtxt('prediction.csv',delimiter=',',skiprows=1)
# df[0,1]

for i in range(1,df.shape[0]-1):
    if(df[i-1,1] == df[i+1,1]):
        df[i,1] = df[i-1,1]

# df = np.array([1,1])
with open('post.csv', 'w') as f:
            f.write('Id,Class\n')
            for i in df:
                f.write('{},{}\n'.format(int(i[0]), int(i[1])))