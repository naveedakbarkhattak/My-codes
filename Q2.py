# Q no 2 100 random no list then list of greater that 40 in that list
import random as rn
# inputNo=int(input("Enter no:"))
randomNumbersList=[]
for i in range(100):
    randomNumber=rn.randint(1,101)
    randomNumbersList.append(randomNumber)
print("randomNumbersList =",randomNumbersList)
greaterThan40=[]
for j in randomNumbersList:
    if j>=40:
        greaterThan40.append(j)
        continue
print("greaterThan40 =",greaterThan40)