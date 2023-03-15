#!/usr/bin/python3
# -*- coding: UTF-8 -*-


fo=open("desktop/codetrying/pythons/fileb.txt","w+")
fo.write("Welcome!\nHello!")
fo.flush()
print(fo.name)
print(fo.mode)
fo.close()
fo=open("fileb.txt","r")
line=fo.readline()
print(line)