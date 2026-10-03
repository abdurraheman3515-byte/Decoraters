
def Decorate(Func):
    def wrapper(*arg,**kwarg):
       print("==>  Good Morning.")
       print("==>  Admission in the Python Class.")
       print("==>  Python is  high-level, general-purpose programming language.")
       print("==>  Its syntax is simpler than many programming languages.")
       print("==>  Python is free to use.")
       Func(*arg,**kwarg)
       print("Thanks!")
    return wrapper


@Decorate
def Admission(classdate,classtime,classname,):
    print("Class name:  ",classname)
    print("Class Date:  ",classdate)
    print("Class Time:  ",classtime)

Admission("1 January","8 am to 9 am",classname="Upgrade Computers")


#============================================================================================================

def Decorate1(Func):
    def wrapper1(*arg):
        print("Admission in 11th")
        Func(*arg)
    return wrapper1

def Decorate2(Func):
    def wrapper2(*arg):
        if arg[0] >= 80:
            print("You are admit in Science")
        elif arg[0] >= 60:
            print("You are admit in Commerce")
        elif arg[0] >=40:
            print("You are admit in Arts")   
        else:
            print("Admission not available")
        Func(*arg)
    return wrapper2

@Decorate1
def College(College_Name):
     print("College_Name:",College_Name)
@Decorate2
def Admission(percent):
    print("Percentage:", percent)

College("MHS and JC")
Admission(85)