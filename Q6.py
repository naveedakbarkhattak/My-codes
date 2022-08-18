# enter 2 lists of your choice and find common elements
import random as rn
lengthOfList1=int(input("Enter length of list1 =:"))
lengthOfList2=int(input("Enter length of list2 =:"))

list1=[]
for i in range(lengthOfList1):
    elementOf1=int(input("Enter elements of list1:"))
    list1.append(elementOf1)

list2=[]
for i in range(lengthOfList2):
    elementOf2=int(input("Enter elements of list2:"))
    list2.append(elementOf2)
commonList=[]
for i in list1:
    for j in list2:
        if i==j:
            commonList.append(i)
            continue
print(f"common element/s in both lists : {commonList}")


