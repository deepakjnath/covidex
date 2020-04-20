import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#link = 'data_stock.csv'
#link = 'https://docs.google.com/spreadsheets/d/1p2MhLy_P2W5Tw0NJ1pJGbIbVWhnizg9FQMbUIyGIHRU/export?format=csv&gid=301720168'
#link = 'https://docs.google.com/spreadsheets/d/1p2MhLy_P2W5Tw0NJ1pJGbIbVWhnizg9FQMbUIyGIHRU/export?format=csv&gid=490377085'
#link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQHA4Xe6nGGrXeCj8es7U609RBysrwjaAasNSjwwI97yLuWw6ADCdBMWxEv-bQJlo8PCbUci5zFxIfZ/pub?gid=490377085&single=true&output=csv'
link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQHA4Xe6nGGrXeCj8es7U609RBysrwjaAasNSjwwI97yLuWw6ADCdBMWxEv-bQJlo8PCbUci5zFxIfZ/pub?gid=301720168&single=true&output=csv'
cols = [x for x in range(150) if x%2 == 1]
data = pd.read_csv(link,usecols=cols,index_col=0,engine='python')
data.head()
#data = pd.read_csv('https://www.dropbox.com/s/4jgheggd1dak5pw/data_visualization.csv?raw=1', index_col=0)
corr = data.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()