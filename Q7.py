import random as rn
# inputNo=int(input("Enter no:"))
randomNumbersList=[]
for i in range(1):
    randomNumber=rn.randint(1,3)
    randomNumbersList.append(randomNumber)
# print("randomNumbersList =",randomNumbersList)
for i in range(3):
    for j in randomNumbersList:
        guess=int(input("Enter your guess :"))
        if guess==j:
            print("User Guess is true")
            break
        else:
            print("Bad luck")
    



