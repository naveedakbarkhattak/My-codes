# sum of the list of 100 numbers
import random as rn
# inputNo=int(input("Enter no:"))
randomNumbersList=[]
for i in range(100):
    randomNumber=rn.randint(1,101)
    randomNumbersList.append(randomNumber)
print("randomNumbersList =",randomNumbersList)
sum=0
for j in randomNumbersList:
    sum+=j
print(f"Sum of the numbers is {sum}")