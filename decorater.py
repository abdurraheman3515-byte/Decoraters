
def morning():
    print("Good Morning!")


def greetings(fun):
    def wrapper():
       fun()
       print("Welcome to the python class")
       print("Thanks!")
    return wrapper

a=greetings(morning)
a()

        
#============================================

def evening():
    print("Good Evening")

def greetings(fun):
    def wrapper():
       fun()
       print("Welcome to the python class")
       print("Thanks!")
    return wrapper

b=greetings(morning)
b()



















