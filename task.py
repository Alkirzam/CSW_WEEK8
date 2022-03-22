import pandas as pd
import numpy as np
import seaborn as sns
import re
from plotly.offline import init_notebook_mode,iplot
import matplotlib as mpl
import matplotlib.pyplot as plt
from subprocess import check_output

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

movies_df = pd.read_csv('C:/Users/csmmheyd/Documents/csws-week1/csws-week1/rotten_tomatoes_critic_reviews.csv')
a=plt.cm.spring
plt.figure(figsize=(15,10))
count = movies_df['publisher_name'].value_counts()[:15]
sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
for i, v in enumerate(count.values):
    plt.text(50.0,i,v,color='b',fontsize=10)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Studio name', fontsize=12)
plt.title("Distribution of publishers and critic reviews", fontsize=16)
plt.show()