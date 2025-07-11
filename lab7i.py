#!/usr/bin/env python3
# Student ID: rtang41 104448246
def function1():
    #added global keyword for check
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:',schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:',schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:',schoolName)
function1()
print('print() in main on schoolName:',schoolName)
function2()
print('print() in main on schoolName:',schoolName)