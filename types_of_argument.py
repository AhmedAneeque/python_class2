
# positional arguments
def display_result(name,roll,marks):
    print ("Name=",name)
    print ("roll_no.=",roll)
    print ("marks=",marks)
    print("percentage=",sum(marks)/len(marks))

display_result("Aneeque",10,[85,74,98,57,79])

#keyword arguments
def display_result(name,roll,marks):
    print ("Name=",name)
    print ("roll_no.=",roll)
    print ("marks=",marks)
    print("percentage=",sum(marks)/len(marks))

display_result(marks=[85,74,98,57,79],roll=24,name="ali")

#arbitrary Arguments
def calculate_result(name,*marks):
    print (name)
    print(marks)
    print("total=",sum(marks))
    print("percentage=",sum(marks)/len(marks))

calculate_result("Ahmed",55,96,75,56,85)

#Arbitrary keyword arguments
def calculate_result(**marks):
    print(marks)
    # print("total=",sum(marks))
    # print("percentage=",sum(marks)/len(marks))

calculate_result(english=67,maths=87,urdu=98,hindi=78,marathi=93)
