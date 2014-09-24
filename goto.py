__author__ = 'sikachov evgeny'

def enter():
    e=raw_input()

def q0():
    print "Insert card"
    enter()
    q1()


def q1():
    pin = int(raw_input("Enter the PIN: "))
    if pin == 1234:
        q2()
    else:
        q1()


def q2():
    choice = int(raw_input("1. Cancel\n2. Balance\n3. Cash\nEnter the choice: "))
    if choice == 1:
        q11()
    elif choice==2:
        q4()
    elif choice==3:
        q3()

def q4():
    print "Balance: 100$"
    enter()
    q11()

def q3():
    money=raw_input("Money: ")
    q5()

def q5():
    print "Take a money"
    enter()
    q6()

def q6():
    print "Take a check"
    enter()
    q11()

def q11():
    print "Take card\n\n\n"
    enter()
    q0()

q0()