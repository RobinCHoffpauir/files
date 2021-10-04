import pandas as pd
from pandas import plotting 
df=pd.read_csv('/Users/Robin/Documents/detailed standings.csv')
fd=pd.DataFrame(df)
fig=pd.plotting.scatter_matrix(fd)
print(fig)
input('press<enter>')
