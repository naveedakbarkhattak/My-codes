# *********Assignment for entering students data who are joining PIAIC************
space,star=" ","*"  #spaces and sterics defined
student_data={}  #dictionary to store students info
def Receiving_data():  #function to receive data
    b,c,d=input("\nEnter student name:"),int(input("Enter student age:")),input("Enter student email address:")  #Enter Basic data
    student_data["name"]=b;student_data["age"]=c;student_data["email"]=d  #inserting basic data into dictionary
    print(f"\n{star*2}Available courses:AI,IoT,Web3,BCC{star*2}")#print all subjects avaiable
    courses=[]  #list of all courses
    while True:  # loop for entering list of courses
        i=input("\nEnter your desired course(es) one by one and press enter when finished :")  #getting the courses one by one
        if i=="":  #empty condition for input data
            break  #breaking the while loop
        courses.append(i)  #adding courses to the list
    student_data["courses"]=courses;print("\nData Entry is finised. Thanks \n") #assiging courses and printing
    initialize_code() #looping if invalid
def initialize_code(): #starting the code
    print(f"\n{space*3}{star*4}Welcome to PIAIC Student Portal {star*4}{space*3}\n\n1-Student Data Entry\n2-Student details\n3-quit the program")#
    a=int(input("\nEnter your desired option (1,2,3) :"))  #entering desired option
    while a!=3:  #condition for infinite loop
        if a==1:
            Receiving_data();break  #breaking the loop
        elif a==2:
            print(f"\n Student Data :{student_data}\n\n")
            initialize_code();break  #breaking the loop
        else:
            print("\n ##Caution :invalid input##");initialize_code()  #looping for invalid inputs
initialize_code()  #starting the programe
print("\nThanks for visiting PIAIC Student Portal.")  ##closing statement


    







