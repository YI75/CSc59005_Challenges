import os
import fileinput
#Function to remove \n
def stringGen(n):
    st = ""
    while n>0:
        st = st + "*"
        n -= 1
    return st
#Removes space in a line of text file
def removeSpace(f):
    newList = []
    for line in f:
        newList.append(line.strip())
    return newList
#Counts the number of taboo words in the text file
def checkNum(tabooList, lineList):
    tabooCount = 0
    for i in range(0, len(lineList)):
        for j in range(0, len(tabooList)):                
            if tabooList[j] in lineList[i]:
                    tabooCount += 1
    print(tabooCount)
    return (tabooCount>5)
#Opens the text file containing the taboo words
#Opens the text file that needs censoring
#Replaces all taboo words in the given text file with array manipulation
with open("taboo.txt", "r") as f: 
    with open("example.txt","r") as wf:
        tabooList = removeSpace(f.readlines())
        lineList = removeSpace(wf.readlines())
        boo = checkNum(tabooList, lineList)
        print(boo)
        print(lineList)
        for i in range(0, len(lineList)):
            for j in range(0, len(tabooList)):                
                if tabooList[j] in lineList[i]:
                    lineList[i] = lineList[i].replace(tabooList[j],stringGen(len(tabooList[j])))
#Writes the updated array to the given text file 
with open("example.txt","w") as wf:
    for n in lineList:
        wf.write(n)
        wf.write("\n")
#Debugging
print(tabooList)
print(lineList)
