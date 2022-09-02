space,star=" ","*"  #spaces and sterics defined
def display():
    print(f"\n{space*3}{star*4}Welcome to PIAIC Student Portal {star*4}{space*3}\n\n1-login\n2-display result\n3-quit the program")#
    a=int(input("\nEnter your desired option (1,2,3) :"))  #entering desired option
    return a
def opening_text_file(login,x):
    with open('data.txt') as my_data:
        w = my_data.readlines()
        if x==1:
            for line in w:
                if f'{login}' in line:
                    return True
        else: 
            return w
def login_status():
    login=input("please Enter your name :")
    l=opening_text_file(login,1)
    if l == True:
        print("\nsuccessfull login\n")
        display_quiz()
    else:
        print("\nyou are not a student of PIAIC hence not allowed to login")
def display_quiz():
    disp=opening_text_file(login='ali',x=0)
    for lines in disp:
        print(lines)
    correct_answer()

def correct_answer():
    options=input("Enter desired option :")
    if options=="fruit":
        print("\nyour answer is correct ")
        with open(f"result.txt",'w')as new_file:
            new_file.write('ali is passed')
    else:
        print("you are failed")
        with open(f"result.txt",'w')as new_file:
            new_file.write('ali is failed')
def display_result():
    with open(f"result.txt")as new_file:
        n=new_file.readlines()
        for line in n:
            print(line)
def start_code():
    a=0
    while a!=3:
        a=display()
        if a==1:
            login_status()
        elif a==2:
            display_result()    
        elif a==3:
            print("Thanks for visiting PIAIC Portal")
        else:
            print("invalid input")

start_code()
                


                    


    
