import subprocess as sub
import os
print("WELCOME TO PRAVEGA LORD OF THE STRINGS \n \n ")

print("SYSTEM REQUIRMENTS: ")
print("RAM: 512 MB")
print("Storage : 1 GB")
des = int(input("\nDoes your system meets the requirments: (If yes enter 1 otherwise enter 0): "))

p1 = sub.Popen(['Source.exe'],encoding = 'utf-8',stdin = sub.PIPE,bufsize=0)

print("\nSTARTING INSTALLATION\n")
print("NOTE: In the Installation process it is advised to go with recommended settings as the other options will just waste your time")
if not (os.path.isfile('pravega.txt') and os.path.getsize('pravega.txt') > 500000000):
    n = int(input("\nLength Of labelling of Cities in Krypton: (Recommended 400) "))

    print(n,file = p1.stdin)

    desicion = int(input("Do you want to customise the selection of functions(0 if no 1 is yes) : (Recommended 0) "))

    if desicion == 0:
        print(4,file=p1.stdin)
        for j in range(1,5):
           if j == 3 or j==4:
              j+=1
           print(j,file=p1.stdin)
           
    else:
        print("These are the available functions: ")
        print("1: Right Shift")
        print("2: Left Shift")
        print("3: Reverse")
        print("4: Alt Swap")
        print("5: Half Reverse")
        print("Recommended : 1 2 4 5")
        print("Note: Here the number on the side of the function name are thier respective indices.")
        print("")
        print("")
        m = int(input("How many functions do you want: "))
        print(m,file=p1.stdin)
        for i in range(m):
            m=int(input("Enter the index of the selected function: "))
            print(m,file=p1.stdin)

    print("\nDo not press any key")
    print("\nThis may take some time (approx. 20 minutes)... \n")

    p1.wait()

    print("INSTALLATION OF KRYPTON COMPLETED. \n")
else:
    print('KRYPTON IS ALREADY INSTALLED')
    d= input("\nPress enter to continue")

p2 = sub.Popen(['init.exe'],encoding = 'utf-8',stdin = sub.PIPE,bufsize=0)

config = int(input("Number Of Battle areans you want to create: (Recommended 4000): "))

number_of_cops = int(input("\nNumber of cops: "))

number_of_spys = int(input("\nNumber of spys: "))

print(config,file = p2.stdin)

print(number_of_cops,file = p2.stdin)

print(number_of_spys,file = p2.stdin)

print("\nThis may take some time... \n")

p2.wait()

print("BATTLE ARENA CREATED \n")

print("INSTALLATION COMPLETED.\n")

d= input("\nPress Enter to exit")

    




