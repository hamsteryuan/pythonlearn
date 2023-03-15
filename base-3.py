#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
     print ("Name : ", self.name,  ", Salary: ", self.salary)
     "创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp1.displayCount()
emp2.displayEmployee()
emp2.displayCount()
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name,"destroy")
 
pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # 打印对象的id
del pt1
del pt2
del pt3      

 
import re
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

a = "Hello"
b = "Python"
 
print ("a + b 输出结果：", a + b )
print ("a * 2 输出结果：", a * b)
print ("a[1] 输出结果：", a[1]) 
print ("a[1:4] 输出结果：", a[1:4]) 
 
if( "H" in a) :
    print ("H 在变量 a 中") 
else :
    print ("H 不在变量 a 中") 
 
if( "M" not in a) :
    print ("M 不在变量 a 中" )
else :
    print ("M 在变量 a 中")
 
print (r'\n')
print (R'\n')