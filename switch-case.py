__author__ = 'evgeny'

def enter():
    e=raw_input()

def goto_q0():
    print "Insert card"
    enter()
    switch[1]()


def goto_q1():
    pin = int(raw_input("Enter the PIN: "))
    if pin == 1234:
        switch[2]()
    else:
        switch[1]()


def goto_q2():
    choice = int(raw_input("1. Cancel\n2. Balance\n3. Cash\nEnter the choice: "))
    if choice == 1:
        switch[11]()
    elif choice==2:
        switch[4]()
    elif choice==3:
        switch[3]()

def goto_q4():
    print "Balance: 100$"
    enter()
    switch[11]()

def goto_q3():
    money=raw_input("Money: ")
    switch[5]()

def goto_q5():
    print "Take a money"
    enter()
    switch[6]()

def goto_q6():
    print "Take a check"
    enter()
    switch[11]()

def goto_q11():
    print "Take card\n\n\n"
    enter()
    switch[0]()

switch = {0 : goto_q0,
                1 : goto_q1,
                2 : goto_q2,
                3 : goto_q3,
                4 : goto_q4,
                5 : goto_q5,
                6 : goto_q6,
                11 : goto_q11
}

switch[0]()
