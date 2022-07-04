print("******Welcome to Board of intermediat and Secondary Education Peshawar*********")
print("###Caution###")
print("Dear Student kindly enter your credentials according to the following rules:\n 1-Each Arts subjects carry a total of 100 marks\n 2-Each Science subject carry a total of 75 marks\n 3-Each Practical carry a total of 25 Marks")
print("*****Best of Luck*****")
name=input("Enter your name: ")
fatherName=input("Enter your father name: ")
collegeName=input("Enter your school name: ")
yearOfPassing=int(input("Enter your year of passing: "))
while yearOfPassing>2021:
    print("invalid year, Enter again")
    yearOfPassing=int(input("Enter your year of passing: "))
studentType=input("regular or private (Student): ")
while studentType!=("regular" or "private"):
    print("invalid Type, Enter again")
    studentType=input("regular or private (Student): ")
english=int(input("Enter your English marks: "))
while english>100:
    print("invalid marks, Enter again")
    english=int(input("Enter your English marks: "))
urdu=int(input("Enter your Urdu marks: "))
while urdu>100:
    print("invalid marks, Enter again")
    urdu=int(input("Enter your Urdu marks: "))
islamiat=int(input("Enter your islamiat marks: "))
while islamiat>100:
    print("invalid marks, Enter again")
    islamiat=int(input("Enter your islamiat marks: "))
physics=int(input("Enter your physics marks: "))
while physics>75:
    print("invalid marks, Enter again")
    physics=int(input("Enter your physics marks: "))
physicsPracticalMarks=int(input("Enter your physicsPracticalMarks marks: "))
while physicsPracticalMarks>25:
    print("invalid marks, Enter again")
    physicsPracticalMarks=int(input("Enter your physicsPracticalMarks marks: "))
chemistry=int(input("Enter your chemistry marks: "))
while chemistry>75:
    print("invalid marks, Enter again")
    chemistry=int(input("Enter your chemistry marks: "))
chemistryPracticalMarks=int(input("Enter your chemistryPracticalMarks marks: "))
while chemistryPracticalMarks>75:
    print("invalid marks, Enter again")
    chemistryPracticalMarks=int(input("Enter your chemistryPracticalMarks marks: "))
biology=int(input("Enter your biology marks: "))
while biology>75:
    print("invalid marks, Enter again")
    biology=int(input("Enter your biology marks: "))
biologyPracticalMarks=int(input("Enter your biologyPracticalMarks marks: "))
while biologyPracticalMarks>25:
    print("invalid marks, Enter again")
    biologyPracticalMarks=int(input("Enter your biologyPracticalMarks marks: "))
print("*************** BISE Peshawar***************")
print ("***** Intermediat Exam Pre-Medical-2022******")
print("****Detail Marks Sheet****")
print ("     ","Mr.",name,"Son/Daughter of ","Mr./Mrs.",fatherName,"\n","of",collegeName, "Has secured the marks shown against each subject in HSSC exam held in the month of \n", yearOfPassing,"as a", studentType,"Student")
print("   Subject           Subject Marks        Practical Marks")
print("   English           ",english           )
print("   Urdu              ",urdu           )
print("   Islamiat          ",islamiat           )
print("   Physics           ",physics,"                 ",physicsPracticalMarks           )
print("   Chemistry         ",chemistry,"                 ",chemistryPracticalMarks         )
print("   Biology           ",biology,"                 ",biologyPracticalMarks         )
totalmarksObtained = english+urdu+islamiat+physics+physicsPracticalMarks+chemistry+chemistryPracticalMarks+biology+biologyPracticalMarks
print("   Total Marks Obtained =",totalmarksObtained,"/600")
print("   Percentage Obtained  =",totalmarksObtained/600*100)
if totalmarksObtained > 300:
    print("congratulations! you have passed the exam. ")
else:
    print("Sorry! you are failed. Better luck next time,")
