import csv
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data.csv')

def Validation():
    global certifiedFresh, fresh, rotten, total, genre
    print("1- Comedy\n2- Drama\n3- Horror\n4- Classics\n5- Documentary\n6- Art House & International\n7- Action & Adventure\n")

    userInput = input("Please select a genre from 1-7\n")
    while userInput not in ["1", "2", "3", "4", "5", "6", "7"]:
        userInput = input("Please a valid input from 1-7\n")
        

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


    certifiedFresh =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Certified-Fresh')])
    fresh =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Fresh')])
    rotten =len(df[(df['genres']==genre)&(df['tomatometer_status']=='Rotten')])
    total = certifiedFresh+fresh+rotten

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

ax1.pie(data1, labels=labels, autopct='%.1f%%', colors=['green','orange','red',])
ax2.pie(data2, labels=labels, autopct='%.1f%%', colors=['green','orange','red',])

ax1.set_title(firstGenre)
ax2.set_title(secondGenre)
plt.show()