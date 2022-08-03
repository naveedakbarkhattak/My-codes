# Question no 1 = get no as input, generate and print table of that no upto 10
import random as rn
inputNo=int(input("Enter no:"))
randomNumbersList=[]
for i in range(inputNo):
    randomNumber=rn.randint(1,11)
    randomNumbersList.append(randomNumber)
print("randomNumbersList =",randomNumbersList)
