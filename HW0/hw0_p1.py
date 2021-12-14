# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:55:13 2021

@author: ACER-SF315

限制條件:只能使用abcABC或xyzXYZ 不能混搭 e.g. a+z 
        必須照字母順序填寫
        如出現變數出現在有次方項之變數後須寫出乘號 e.g. x^2y必須寫成x^2*y
        所有相乘符號"*"需寫出來  e.g. 2y(不行) -> 2*y(可以) 兩變數相乘可以 e.g. xy(可以) x*y(可以)
        所有次方符號"^"需寫出來  e.g. x2(不行) -> x^2(可以)
"""
Polynomial = input("Input the Polynomials:")
Polynomial = Polynomial.strip("(").strip(")").upper().replace("-","+-")\
.replace("XY","X*Y").replace("YZ","Y*Z").replace("XZ","X*Z")\
.replace("AB","A*B").replace("AC","A*C").replace("BC","B*C").split(")(")#分割多項式
Answer = []
Group = []
Group2=[]
Coefficient = []
Power = 0
Element = []
for i in range(0,len(Polynomial)):
    Polynomial[i] = Polynomial[i].split("+")#分割多項式
for i in range(0,len(Polynomial)):#初始化
    Group.append([])
for i in range(0,len(Polynomial[0])):#在第一層放入多項式的第一個分式
    Group[0].append(Polynomial[0][i])
for i in range(0,2):
    Element.append([])
for i in range(1,len(Polynomial)):#多項式展開
    Runs = 0
    length = len(Group[i-1])
    for m in range(0,length):
        for n in range(0,len(Polynomial[i])):
            Group[i].append(Group[i-1][m]+"*"+Polynomial[i][n])
            Runs+=1
for i in range(0,len(Group[len(Group)-1])):
    Group[len(Group)-1][i] = Group[len(Group)-1][i].replace("-", "-1*")
Group2.extend(Group[len(Polynomial)-1])#將最終結果複製至另一陣列
for i in range(0,len(Group[len(Polynomial)-1])):#分割及按照數字字母順序排序
    Group2[i]=Group2[i].split('*')
    Group2[i].sort()
for i in range(0,len(Group2)):
    m=0
    n=0
    Coefficient.append(1)#初始化係數陣列
    for j in range(0,len(Group2[i])):
        if Group2[i][j].isdigit() == True or Group2[i][j] == "-1":#紀錄係數
            Coefficient[i] = Coefficient[i]*int(Group2[i][j])
        if Group2[i][j].find("^")!=-1:#把有次方的元素拆分成各個單元素(ex:x^2=x,x)
            Group2[i][j]=Group2[i][j].split("^")
            for k in range(0,int(Group2[i][j][1])):
                Group2[i].extend(Group2[i][j][0])
    Group2Len = len(Group2[i])
    while m < Group2Len:#把原本有次方的元素刪除
        if type(Group2[i][m]) == list:
            del Group2[i][m]
            Group2Len-=1
            m-=1
        m+=1
    Group2[i].sort()
    for n in range(len(Group2[i])):#計算各元素次方項
        if Group2[i][n].isalpha()==True:
           if Group2[i][n] not in Element[0]:
               Element[0].append(Group2[i][n])
               Element[1].append(1)
           else:
               Element[1][Element[0].index(Group2[i][n])]+=1
    flag = 1
    for p in range(0,len(Element[0])):#把各個單元素組合回多項式的樣子(ex:x,會變成x^2x)
        if Element[1][p]!=0:
            if  flag == 1 :
                Answer.append(Element[0][p])
                if Element[1][p] != 1:
                    Answer[i]+="^"
                    Answer[i]+=str(Element[1][p])
                flag = 0
            else:
                Answer[i]+=str(Element[0][p])
                if Element[1][p]!=1:
                    Answer[i]+="^"+str(Element[1][p])
        Element[1][p] = 0
FinalAnswer = []
for i in range(0,2):
    FinalAnswer.append([])
for i in range(0,len(Coefficient)):#合併係數與項
    if Coefficient[i] != "":
        Coefficient[i] = int(Coefficient[i])
    if Answer[i] not in FinalAnswer[0]:
        FinalAnswer[0].append(Answer[i])
        FinalAnswer[1].append(Coefficient[i])
    else:
        FinalAnswer[1][FinalAnswer[0].index(Answer[i])]+=Coefficient[i]
FinalResult = ""
for i in range(0,len(FinalAnswer[0])):#
    FinalAnswer[1][i] = str(FinalAnswer[1][i]).replace("1","")#拿掉係數是1的
    for j in range(0,2):
        FinalResult+=str(FinalAnswer[1-j][i])
        if j==1:  
            FinalResult+="+"
FinalResult=FinalResult.replace("+-", "-").rstrip("+")#如果有+-移除變成減的      
print("Output Results:"+FinalResult)