__author__ = 'evgeny'

def enter():
    e=raw_input()

def goto_q0():
    print "Insert card"
    enter()
    ifSwitchTable[1,0]=goto_q1()
    ifSwitchTable[1,0]()


def goto_q1():
    pin = int(raw_input("Enter the PIN: "))
    if pin == 1234:
        ifSwitchTable[2,1]=goto_q2()
        ifSwitchTable[2,1]()
    else:
        ifSwitchTable[0,1]=goto_q1()
        ifSwitchTable[0,1]()


def goto_q2():
    choice = int(raw_input("1. Cancel\n2. Balance\n3. Cash\nEnter the choice: "))
    if choice == 1:
        ifSwitchTable[5,2]=goto_q11()
        ifSwitchTable[5,2]()
    elif choice==2:
        ifSwitchTable[3,2]=goto_q4()
        ifSwitchTable[3,2]()
    elif choice==3:
        ifSwitchTable[4,2]=goto_q3()
        ifSwitchTable[4,2]()

def goto_q4():
    print "Balance: 100$"
    enter()
    ifSwitchTable[5,2]=goto_q11()
    ifSwitchTable[5,2]()

def goto_q3():
    money=raw_input("Money: ")
    ifSwitchTable[6,3]=goto_q5()
    ifSwitchTable[6,3]()

def goto_q5():
    print "Take a money"
    enter()
    ifSwitchTable[7,5]=goto_q6()
    ifSwitchTable[7,5]()

def goto_q6():
    print "Take a check"
    enter()
    ifSwitchTable[8,6]=goto_q11()
    ifSwitchTable[8,6]()

def goto_q11():
    print "Take card\n\n\n"
    enter()
    ifSwitchTable[0,11]=goto_q0()
    ifSwitchTable[0,11]()



ifSwitchTable=[]

ifSwitchTable[0,0]=goto_q0()
ifSwitchTable[0,0]()