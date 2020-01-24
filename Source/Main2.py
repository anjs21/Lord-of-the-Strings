import subprocess as sub
import os
import pickle
import sys
def file_input():
    cop_file = input("Enter the location of Jor-El's Source File: ")
    spy_file = input("Enter the location of Zod's Source File: ")

    path,filename=os.path.split(cop_file)
    filename = filename.split('.')[0]

    sys.path.insert(1,path)

    cop_module = __import__(filename)
    
    path2,filename2=os.path.split(spy_file)
    filename2 = filename2.split('.')[0]

    sys.path.insert(1,path2)

    spy_module = __import__(filename2)

    return cop_module,spy_module

p1 = sub.Popen(['Main.exe'],encoding = 'utf-8',stdin = sub.PIPE,bufsize=0)

number = int(input("Enter the index of Battle Arena you want: "))

print(number,file = p1.stdin)

binary = int(input("Do you want any time restrictions? ( 0 if no and 1 if yes ): "))

print(binary,file = p1.stdin)

cop_handle , spy_handle = file_input()

cop_data,spy_data = pickle.dumps(cop_handle),pickle.dumps(spy_handle)

print(cop_data,file = p1.stdin)

print(spy_data,file = p1.stdin)

max_steps = int(input("How much time is left before the planet dies: (Recommended 500)"))

print(max_steps ,file = p1.stdin)

revelation = int(input("After how much time does the Kryptonians will get the location (Recommended 5)"))

print(revelation,file = p1.stdin)
