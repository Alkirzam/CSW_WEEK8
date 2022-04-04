import pandas as pd
import numpy as np
import seaborn as sns
import re
from plotly.offline import init_notebook_mode,iplot
import matplotlib as mpl
import matplotlib.pyplot as plt
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
init_notebook_mode(connected=True)
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None




movie_genres_df= pd.read_csv('C:/Users/hanis/workshop coursework/CSW_ week 8/CSW_WEEK8/rotten_tomatoes_movies (2).csv')
#movies_df.head(5)
#reviews_df.head(5)

#reviews_df = reviews_df[reviews_df.review_date.notnull()]
#reviews_df['review_date'] = pd.to_datetime(reviews_df['review_date'])
#reviews_df['review_year'] = reviews_df['review_date'].apply(lambda x: x.year)
#reviews_df = reviews_df[reviews_df.review_year.astype(int) >= 2000]

#plt.figure(figsize=(15,10))
#plt.title('Reviews by the year', size=20)
#sns.distplot(reviews_df.review_year, bins=20, kde=False)
#plt.ylabel('Number of critic reviews', size=15)
#plt.xlabel('Year of review posted',size=15)
#plt.axis([2000, 2019, 0, 75000])
#plt.xticks(np.arange(2000, 2019, step=1),rotation=45, ha='right')
#plt.show()





#a = plt.cm.cool
#group_names = movie_genres_df.genres.value_counts().head(7).index
#group_size = movie_genres_df.genres.value_counts().head(7)
#subgroup_names = ['Certified-Fresh','Fresh','Rotten', 'Certified-Fresh','Fresh','Rotten', 'Certified-Fresh','Fresh','Rotten', 'Certified-Fresh', 'Fresh', 'Rotten',
 #                 'Certified-Fresh','Fresh','Rotten', 'Certified-Fresh','Fresh','Rotten', 'Certified-Fresh','Fresh','Rotten']
#size_list = []
#for element in group_names:
 #   size_list.append(movie_genres_df.loc[element]['Certified-Fresh'])
  #  size_list.append(movie_genres_df.loc[element]['Fresh'])
   # size_list.append(movie_genres_df.loc[element]['Rotten'])
#subgroup_size = size_list

#fig, ax = plt.subplots()
#ax.axis('equal')
#outter_pie, _ = ax.pie(group_size, radius=4, labels=group_names,
 #                      colors=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7)])
#plt.setp(outter_pie, width=1, edgecolor='white') 
#inner_pie, _ = ax.pie(subgroup_size, radius=3, labels=subgroup_names, labeldistance=0.83,
 #                     colors=['green','gold','red', 'green','gold','red', 'green','gold','red', 'green','gold','red',
  #                          'green','gold','red', 'green','gold','red', 'green','gold','red'])
#plt.setp(inner_pie, width=0.4, edgecolor='white')
#plt.margins(0,0)
#plt.show()
count = movie_genres_df.value_counts()[:7]


a = plt.cm.cool
group_names = movie_genres_df.genres.value_counts().head(7).index
group_size = movie_genres_df.genres.value_counts().head(7)
subgroup_names = ['Upright','Spilled', 'Upright','Spilled', 'Upright','Spilled', 'Upright','Spilled',
                  'Upright','Spilled', 'Upright','Spilled', 'Upright','Spilled']
size_list = []
for element in group_names:
    size_list.append(movie_genres_df.loc[element]['Upright'])
    size_list.append(movie_genres_df.loc[element]['Spilled'])
subgroup_size = size_list

fig, ax = plt.subplots()
ax.axis('equal')
outter_pie, _ = ax.pie(group_size, radius=4, labels=group_names,
                       colors=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7)])
plt.setp(outter_pie, width=1, edgecolor='white') 
inner_pie, _ = ax.pie(subgroup_size, radius=3, labels=subgroup_names, labeldistance=0.83,
                      colors=['green','red', 'green','red', 'green','red', 'green','red',
                              'green','red', 'green','red', 'green','red'])
plt.setp(inner_pie, width=0.4, edgecolor='white')
plt.margins(0,0)
plt.show()




#a = plt.cm.cool

#plt.figure(figsize=(15,10))
#count = reviews_df['publisher_name'].value_counts()[:10]
#sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
#for i, v in enumerate(count.values):
 #   plt.text(0.8,i,v,color='k',fontsize=14)
#plt.xlabel('Count', fontsize=12)
#plt.ylabel('Studio name', fontsize=12)
#plt.title("Distribution of Publisher names in critic reviews", fontsize=16)
