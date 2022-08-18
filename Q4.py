# in 100 nos list print the minimum
import random as rn
# inputNo=int(input("Enter no:"))
randomNumbersList=[]
for i in range(100):
    randomNumber=rn.randint(1,101)
    randomNumbersList.append(randomNumber)
print("randomNumbersList =",randomNumbersList)
min=min(randomNumbersList)
print(f"Minimum no in the list is {min}")