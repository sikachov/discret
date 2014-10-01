__author__ = 'evgeny'

def enter():
    e=raw_input()

def goto_q0():
    print "Insert card"
    enter()
    goto_q1()


def goto_q1():
    pin = int(raw_input("Enter the PIN: "))
    if pin == 1234:
        goto_q2()
    else:
        goto_q1()


def goto_q2():
    choice = int(raw_input("1. Cancel\n2. Balance\n3. Cash\nEnter the choice: "))
    if choice == 1:
        goto_q11()
    elif choice==2:
        goto_q4()
    elif choice==3:
        goto_q3()

def goto_q4():
    print "Balance: 100$"
    enter()
    goto_q11()

def goto_q3():
    money=raw_input("Money: ")
    goto_q5()

def goto_q5():
    print "Take a money"
    enter()
    goto_q6()

def goto_q6():
    print "Take a check"
    enter()
    goto_q11()

def goto_q11():
    print "Take card\n\n\n"
    enter()
    goto_q0()

ifSwitchTable=[[]]