# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:55:34 2021

@author: ACER-SF315
"""

with open('IMDB-Movie-Data.csv','r') as f:
    content = f.readlines()
    MovieNums = len(content)
    Keys = content[0].rstrip("\n").split(",")#建立字典的鍵
    KeysNums = len(Keys) 
    Movie = []
    for i in range (1,MovieNums):
        NewContent = content[i].rstrip("\n").split(",")
        MovieDict = {}
        for j in range (0,KeysNums):
            if NewContent[j]=="":
                NewContent[j]=0
            MovieDict[Keys[j]]= NewContent[j]
        Movie.append(MovieDict)
    print(Movie[0])
f.close()

def second(x):#使用第二列元素
    return x[1]

#第一題
RatingList = {}
for i in range (0,MovieNums-1):
    if Movie[i].get("Year")== str(2016):#年份等於2016
        RatingList[Movie[i].get("Title")]=Movie[i].get("Rating")
RatingItem = list(RatingList.items())#字典轉陣列
RatingItem.sort(key=second,reverse=True)#評分由大排到小
print("Top-3 movies with the highest ratings in 2016",end="?\n")
for i in range(0,3):    
    print(RatingItem[i][0],end="\n")
    
#第二題
Actor = []#演員對收入(有重複)
for i in range(0,2):#二維化
    Actor.append([])
for i in range (0,MovieNums-1):#建立演員對收入陣列
    Actor[0].extend(Movie[i].get("Actors").split("|"))
    for j in range(0,len(Movie[i].get("Actors").split("|"))):
        Actor[1].append(float(Movie[i].get("Revenue (Millions)")))
NewActor = []#不重複演員清單
AppearTimes = []#演員出現次數
ActorRevenue = {}#演員收入字典
for i in range(0,len(Actor[0])):
    Actor[0][i]=Actor[0][i].lstrip()
for i in range(0,2):
    NewActor.append([])
for x in Actor[0]:#建立不重複演員清單
    if x not in NewActor[0]:
        NewActor[0].append(x)
ActorNum = len(NewActor[0])
for i in range(0,ActorNum):#將演員的收入加起來並記錄次數
    AppearTimes.append(0)
    NewActor[1].append(0)
    for j in range(0,len(Actor[0])):
        if Actor[0][j] == NewActor[0][i]:
            NewActor[1][i] = NewActor[1][i] + Actor[1][j]
            AppearTimes[i]=AppearTimes[i]+1
for i in range(0,ActorNum):#將收入平均並改成字典(因為前面寫成陣列懶得改)
    NewActor[1][i] = NewActor[1][i]/AppearTimes[i]
    ActorRevenue[NewActor[0][i]] = NewActor[1][i]
ActorRevenueItem = list(ActorRevenue.items())#字典轉陣列 
ActorRevenueItem.sort(key=second,reverse=True)#平均收入由大排到小
print("The actor generating the highest average revenue",end="?\n")
print(ActorRevenueItem[0][0])


#第三題
TotalRating=0
k=0#計數器
for i in range(0,MovieNums-1):#計算艾瑪華森出演電影之評價加總
   if Movie[i].get("Actors").find("Emma Watson")!=-1:
       TotalRating = TotalRating + float(Movie[i].get("Rating"))
       k = k+1
AvgRating = TotalRating/k  
print("The average rating of Emma Watson’s movies",end="?\n")
print(AvgRating)

#第四題
Directors = []#重複導演陣列
Director = []#不重複導演陣列
DirectorItem = {}#導演對合作演員個數字典
AppearTimes = []#出現導演與合作演員個數
k=0#計數器
for i in range(0,2):#二維化Director
    Director.append([])
for i in range (0,MovieNums-1):#建立不重複導演串列
    Directors.append(Movie[i].get("Director"))
    if Movie[i].get("Director") not in Director[0]:
        Director[0].append(Movie[i].get("Director"))
        Director[1].append("")
DirectorNum = len(Director[0])#導演數目
for i in range(0,DirectorNum):#初始化合作次數陣列
    AppearTimes.append(0)
for i in range(0,MovieNums-1):#完成導演和那些演員合作之陣列
    for j in range(0,len(Movie[i].get("Actors").split("|"))):
        if Actor[0][k] not in Director[1][Director[0].index(Directors[i])]:
            #判斷有沒有同演員同導演
            Director[1][Director[0].index(Directors[i])]+=Actor[0][k]
            Director[1][Director[0].index(Directors[i])]+=","
            AppearTimes[Director[0].index(Directors[i])]+=1
        k+=1
for i in range(0,DirectorNum):#建立導演對合作演員個數字典
    DirectorItem[Director[0][i]]=AppearTimes[i]
DirectorItem = list(DirectorItem.items())
DirectorItem.sort(key=second,reverse=True)
print("Top-3 directors who collaborate with the most actors",end="?\n")
for i in range(0,3):    
    print(DirectorItem[i][0],end="\n") 


#第五題
ActorGenre = []#演員對類型陣列
Genre = []#不重複類型陣列
GenreItem = {}#演員對類型個數字典
AppearTimes = []#演員對類型個數
k=0#計數器
for i in range(0,2):#二維化Genre
    ActorGenre.append([])
for i in range(0,MovieNums-1):#建立Genre陣列
    Genre.append(Movie[i].get("Genre").split("|"))
for i in range(0,ActorNum):#初始化演員對類型個數陣列
    ActorGenre[0].append(NewActor[0][i])
    ActorGenre[1].append("")
    AppearTimes.append(0)
for i in range(0,MovieNums-1):#建立演員對類型陣列
    for j in range(0,len(Movie[i].get("Actors").split("|"))):
        for m in range(0,len(Genre[i])):
            if Genre[i][m] not in ActorGenre[1][ActorGenre[0].index(Actor[0][k])]:
                ActorGenre[1][ActorGenre[0].index(Actor[0][k])]+=Genre[i][m]
                ActorGenre[1][ActorGenre[0].index(Actor[0][k])]+=","
                AppearTimes[ActorGenre[0].index(Actor[0][k])]+=1
        k+=1
for i in range(0,DirectorNum):#建立演員對類型個數字典
    GenreItem[ActorGenre[0][i]]=AppearTimes[i]
GenreItem = list(GenreItem.items())
GenreItem.sort(key=second,reverse=True)
print("Top-2 actors playing in the most genres of movies",end="?\n")
for i in range(0,2):    
    print(GenreItem[i][0],end="\n") 
    

#第六題
ActorYear = []#演員對年份陣列
Year = []
ActorYearItem = {}
k=0
for i in range(0,2):
    ActorYear.append([])
for i in range(0,MovieNums-1):
    Year.append(Movie[i].get("Year"))
YearNum = len(Year)
for i in range(0,ActorNum):#初始化演員對年分陣列
    ActorYear[0].append(NewActor[0][i])
    ActorYear[1].append("")
for i in range(0,MovieNums-1):#建立演員對年分陣列
    for j in range(0,len(Movie[i].get("Actors").split("|"))):
        if Year[i] not in ActorYear[1][ActorYear[0].index(Actor[0][k])]:
            ActorYear[1][ActorYear[0].index(Actor[0][k])]+=Year[i]
            ActorYear[1][ActorYear[0].index(Actor[0][k])]+=","
        k+=1
for i in range(0,ActorNum):
    ActorYear[1][i] = ActorYear[1][i].rstrip(",")
    ActorYear[1][i] = int(max(ActorYear[1][i].split(",")))-int(min(ActorYear[1][i].split(",")))
for i in range(0,ActorNum):#建立演員對年分字典
    ActorYearItem[ActorYear[0][i]]=ActorYear[1][i]
ActorYearItem = list(ActorYearItem.items())#陣列化
ActorYearItem.sort(key=second,reverse=True)#由大到小排序
print("actors whose movies lead to the largest maximum gap of years",end="?\n")#最大gapyear演員
i=0
while ActorYearItem[i][1]==ActorYearItem[0][1]:#由前面開始印直到數值不同 
    print(ActorYearItem[i][0],end=",")
    i+=1 
print("\n")
#第七題
RelatedActors = ["Johnny Depp"]
AllActors = []
RelateActorsNum = len(RelatedActors)
k=0 
kNow=-1
flag=True
for i in range(0,MovieNums-1):#建立關係演員陣列
    AllActors.append(Movie[i].get("Actors").split("|"))
    for j in range(0,len(Movie[i].get("Actors").split("|"))):
        AllActors[i][j]=AllActors[i][j].lstrip()      
while(k!=kNow):
    kNow+=1
    for i in range(0,MovieNums-1):
        if RelatedActors[kNow] in AllActors[i]:
            for j in range(0,len(AllActors[i])):
                if AllActors[i][j] not in RelatedActors:#在裡面代表已經有關係了
                    RelatedActors.append(AllActors[i][j])
                    k+=1
RelatedActors.pop(0)
print("Find all actors who collaborate with Johnny Depp in direct and indirect ways",end=":\n")
print(RelatedActors)  
