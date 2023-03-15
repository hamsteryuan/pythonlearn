#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import support
import time
print("Hello!\n")
num_a=1000
print("num_a is:",num_a,type(num_a))
#list induction
names=['Bob','Tom','Peter','Alice']
names_long=[name for name in names if len(name)>3]
print(names_long)
#dictionary induction
dic={x:x**2 for x in {2,4,6}}
print(dic)
#set
seta={x for x in 'aehduhbc'if x not in 'abcd'}
print(seta)
#tuple
a=(x for x in range(1,10))
print(tuple(a))
#[]list （）tuple {:,:}dic
numbers=[12,33,21,22,32,89]
even=[]
odd=[]
while len(numbers)>0:
    number = numbers.pop()
    if(number%2==0):
        even.append(number)
    else:
        odd.append(number)
        
        
ticks=time.time #从1970.1.1以来经历了多少时间
localtime=time.localtime(time.time())
print ("local time is",localtime)

def printme(str):
    print (str) 
    return

printme(str="yuan")

#模块名.函数名
support.print_func("Run")

strin=input("Please input:")
print("You imput: ",strin)