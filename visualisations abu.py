import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns, numpy as np

movie_genres_df= pd.read_csv('C:/Users/hanis/workshop coursework/CSW_ week 8/CSW_WEEK8/rotten_tomatoes_movies (2).csv')


sns.set_color_codes()


f,ax = plt.subplots(3,1, figsize=(15, 50))
sns.distplot(movie_genres_df[(movie_genres_df['tomatometer_status'] == 'Certified-Fresh') &

                             (movie_genres_df['tomatometer_count'] <= 400)].tomatometer_count, ax=ax[0], bins=30, color='g')
ax[0].set_xlabel("TomatoMeter Count",fontsize=0)
ax[0].set_title('TomatoMeter count in Certified Fresh', fontsize=9)
ax[0].set_xlim([0,400])
sns.distplot(movie_genres_df[(movie_genres_df['tomatometer_status'] == 'Fresh') & 

                             (movie_genres_df['tomatometer_count'] <= 400)].tomatometer_count, ax=ax[1], bins=30, color='y')
ax[1].set_xlabel("TomatoMeter Count",fontsize=0)
ax[1].set_title('TomatoMeter count in Fresh', fontsize=9)
ax[1].set_xlim([0,400])
sns.distplot(movie_genres_df[(movie_genres_df['tomatometer_status'] == 'Rotten') &

                             (movie_genres_df['tomatometer_count'] <= 400)].tomatometer_count, ax=ax[2], bins=30, color='r')
ax[2].set_xlabel("TomatoMeter Count",fontsize=0)
ax[2].set_title('TomatoMeter count in Rotten', fontsize=9)
ax[2].set_xlim([0,400])
plt.show()






