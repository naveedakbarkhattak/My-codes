class Piaic_student_portal():
    def __init__(self,name,age,email,subject):
        self.name=name
        self.age=age
        self.email=email
        self.subject=subject
    def enter_data_in_dictionary(self):
        D["name"]=self.name;D["age"]=self.age;D["email"]=self.email;D["subject"]=self.subject
        return D
def display():
    space,star="","*"
    print(f"\n{space*3}{star*4}Welcome to PIAIC Student Portal {star*4}{space*3}\n\n1-Student Data Entry\n2-Student details\n3-quit the program")#
    return int(input("Enter your desired input :"))
D={}
def data_entry():
    a=input("Enter your name :");b=input("Enter you  age :");c=input("Enter your email :");star,space="*",""
    print(f"\n{star*2}Available courses:AI,IoT,Web3,BCC{star*2}")#print all subjects avaiable
    courses=[]  #list of all courses
    while True:  # loop for entering list of courses
        i=input("\nEnter your desired course(es) one by one and press enter when finished :")  #getting the courses one by one
        if i=="":  #empty condition for input data
            break  #breaking the while loop
        courses.append(i)  #adding courses to the list
    any_student=Piaic_student_portal(a,b,c,courses)
    any_student.enter_data_in_dictionary()
def initialize():
    x=0
    while x!=3:
        x=display()
        if x==1:
            data_entry()
        elif x==2:
            print(D)
        elif x==3:
            print("Thanks for using PIAIC Student Portal")
        else:
            print ("invalid input")
initialize()






