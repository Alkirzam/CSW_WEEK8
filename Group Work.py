import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

movies_df = pd.read_csv('data.csv')

def Distribution_of_Studio_names_BY_Ali():
 movies_df = pd.read_csv('data.csv')

 a = plt.cm.Wistia

 plt.figure(figsize=(10,5))
 count = movies_df['production_company'].value_counts()[:10]
 sns.barplot(count.values, count.index, palette=[a(0.1),a(0.2),a(0.3),a(0.4),a(0.5),a(0.6),a(0.7),a(0.8),a(0.9),a(0.99)])
 for i, e in enumerate(count.values):
     plt.text(10.0,i,e,color='k',fontsize=10)
 plt.xlabel('Count', fontsize=10)
 plt.ylabel('Studio name', fontsize=10)
 plt.title("Distribution of Studio names", fontsize=15)
 plt.show()

 
def TomatoMeter_rating_per_Studio_BY_Ali():
 movies_df = pd.read_csv('data.csv')
 movies_df['Studio'] = movies_df['production_company'].str.split(' ').str[0]
 
 count = movies_df['Studio'].value_counts()[:7]
 top_Studio = list(count.index)
 movie_Studio_df = movies_df[movies_df['Studio'].isin(top_Studio)]

 plt.figure(figsize=(15, 10))
 sns.set_style("whitegrid")
 sns.boxplot(x='Studio', y='tomatometer_rating', data=movie_Studio_df)
 plt.xlabel("Studio names",fontsize=10)
 plt.ylabel("TomatoMeter Rating",fontsize=10)
 plt.title("Boxplot of TomatoMeter rating per Studio ", fontsize=15)
 plt.show()

 
def Movies_by_the_year_BY_Sura():
 movies_df = pd.read_csv('data.csv')   
 movies_df = movies_df[movies_df.original_release_date.notnull()]
 movies_df['original_release_date'] = pd.to_datetime(movies_df['original_release_date'])
 movies_df['movie_year'] = movies_df['original_release_date'].apply(lambda x: x.year)
 
 plt.figure(figsize=(10,5))
 plt.title('Movies by the year', size=15)
 sns.distplot(movies_df.movie_year, kde=False)
 plt.ylabel('Number of movies', size=10)
 plt.xlabel('Year of release',size=10)
 plt.axis([1920, 2019, 0, 1750])
 plt.xticks(np.arange(1920, 2018, step=5),rotation=45, ha='right')
 plt.show()
 
def By_Ibby():

 reviews = pd.read_csv('reviews.csv')
 reviews['review_date'] = pd.to_datetime(reviews['review_date'])
 reviews['review_year'] = reviews['review_date'].apply(lambda x: x.year)
 reviews = reviews[reviews.review_year.astype(int) >= 2000]

 sns.set_color_codes()

 plt.figure(figsize=(15,10))
 plt.title('Reviews by the year', size=20)
 sns.distplot(reviews.review_year, bins=20, kde=False, color='m')
 plt.ylabel('Number of critic reviews', size=20)
 plt.xlabel('Year of review posted',size=20)
 plt.axis([2000, 2019, 0, 75000])
 plt.xticks(np.arange(2000, 2019, step=1),rotation=45, ha='right')
 plt.show()
 
def distribution_of_publishers_and_critic_reviws_BY_Said():
 movies_df = pd.read_csv('reviews.csv')
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
 
 def Distribution_of_Movie_Genres_BY_Karl():
  movies_df = pd.read_csv('data.csv')

 k = plt.cm.Wistia

 plt.figure(figsize=(15,10))
 count = movies_df['movie_genre'].value_counts()[:7]
 sns.barplot(count.values, count.index, palette=[k(0.1),k(0.2),k(0.3),k(0.4),k(0.5),k(0.6),k(0.7)])
 for i, e in enumerate(count.values):
     plt.text(12.0,i,e,color='p',fontsize=12)
 plt.title("Distribution of Movie Genres", fontsize=15)
 plt.ylabel('Genre name', fontsize=12)
 plt.xlabel('Count', fontsize=12)
 plt.show()
 
def BY_Abubaker():
 
 movies_df = pd.read_csv('data.csv')

 sns.set_color_codes()
 f,ax = plt.subplots(3,1, figsize=(15, 50))
 sns.distplot(movies_df[(movies_df['tomatometer_status'] == 'Certified-Fresh') &
 (movies_df['tomatometer_count'] <= 400)].tomatometer_count, ax=ax[0], bins=30, color='g')
 ax[0].set_xlabel("TomatoMeter Count",fontsize=0)
 ax[0].set_title('TomatoMeter count in Certified Fresh', fontsize=12)
 ax[0].set_xlim([0,400])
 sns.distplot(movies_df[(movies_df['tomatometer_status'] == 'Fresh') & 
 (movies_df['tomatometer_count'] <= 400)].tomatometer_count, ax=ax[1], bins=30, color='y')
 ax[1].set_xlabel("TomatoMeter Count",fontsize=0)
 ax[1].set_title('TomatoMeter count in Fresh', fontsize=12)
 ax[1].set_xlim([0,400])
 sns.distplot(movies_df[(movies_df['tomatometer_status'] == 'Rotten') &
 (movies_df['tomatometer_count'] <= 400)].tomatometer_count, ax=ax[2], bins=30, color='r')
 ax[2].set_xlabel("TomatoMeter Count",fontsize=0)
 ax[2].set_title('TomatoMeter count in Rotten', fontsize=12)
 ax[2].set_xlim([0,400])
 plt.show()

def Validation():
     df =movies_df= pd.read_csv('data.csv')
    
     global certifiedFresh, fresh, rotten, total, genre
     print("1- Comedy\n2- Drama\n3- Horror\n4- Classics\n5- Documentary\n6- Art House & International\n7- Genre\n8-  Action & Adventure\n")

     userInput = input("Please select a genre from 1-7\n")
     while userInput not in ["1", "2", "3", "4", "5", "6", "7","8"]:
         userInput = input("Please a valid input from 1-8\n")
        

     if (userInput == "1"):
         genre = "Comedy"
     elif (userInput=="2"):
         genre = "Drama"
     elif (userInput=="3"):
         genre = "Horror"
     elif (userInput=="4"):
         genre = "Classics"
     elif (userInput=="5"):
         genre = "Documentary"
     elif (userInput=="6"):
         genre = "Art House & International"
     elif (userInput=="7"):
         genre = "Action & Adventure"
     elif (userInput=="8"):
         genre = "Genre"

     certifiedFresh =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Certified-Fresh')])
     fresh =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Fresh')])
     rotten =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Rotten')])
     total = certifiedFresh+fresh+rotten
 
def Ye_BY_Yusef():
    
 df =movies_df= pd.read_csv('data.csv')


 print("\nPlease choose the first genre you would like to compare")
 Validation()
 firstCertifiedFresh = certifiedFresh/total
 firstFresh = fresh/total
 firstRotten = rotten/total
 firstGenre = genre

 print("\nPlease choose the second genre you would like to compare")
 Validation()
 secondCertifiedFresh = certifiedFresh/total
 secondFresh = fresh/total
 secondRotten = rotten/total
 secondGenre = genre

 data1 = [firstCertifiedFresh, firstFresh, firstRotten]
 data2 = [secondCertifiedFresh, secondFresh, secondRotten]

 labels = 'Certified Fresh', 'Fresh', 'Rotten'

 fig, (ax1, ax2) = plt.subplots(1, 2)

 ax1.pie(data1, labels=labels, autopct='%.2f%%')
 ax2.pie(data2, labels=labels, autopct='%.2f%%')

 ax1.set_title(firstGenre)
 ax2.set_title(secondGenre)
 plt.show()

 
print('------------The Option-----------')
print('Enter 1 for Movies by the year')
print('Enter 2 for Reviews by the year')
print('Enter 3 for Distribution of Studio names')
print('Enter 4 for TomatoMeter rating per Studio')
print('Enter 5 for distribution of publishers and critic reviws')
print('Enter 6 for Distribution of Tomato meter count per tomato meter status')
print('Enter 7 for comparing by different genres  ')
src= int(input('Select option:  '))
while src not in [1, 2, 3, 4, 5, 6, 7, 8] :
    src=int(input('Invalid option please enter another here: '))
    
if src==1:
    Movies_by_the_year_BY_Sura()
elif src==2:
    By_Ibby()
elif  src==3:
    Distribution_of_Studio_names_BY_Ali()
elif src ==4:
    TomatoMeter_rating_per_Studio_BY_Ali()
elif src==5:
     distribution_of_publishers_and_critic_reviws_BY_Said()
elif src==6:
    BY_Abubaker()
elif src==7:
    Ye_BY_Yusef()
elif src==8:
    Distribution_of_Movie_Genres_BY_Karl()