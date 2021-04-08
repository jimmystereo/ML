import pandas as pd



last_df = pd.read_csv('./result/pred_100.csv')
test = [50]
for i in test:
    df = pd.read_csv('./result/pred_{}.csv'.format(i))
    last_df['tested_positive'] = df['tested_positive']+last_df['tested_positive']
last_df['tested_positive'] = last_df['tested_positive'].apply(lambda x:x/2)
last_df.to_csv('./result/pred_mean.csv',index=None)