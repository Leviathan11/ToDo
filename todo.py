import os

test_file=open('test.txt', 'r+')
todolist=test_file.readlines()
test_file.close()

def printout(list):
    for i in range(0, len(list)):
        if list[i][-2]=='1':
            currentstring=str(i+1) + ".[X] " + list[i][:-2]
        else:
            currentstring=str(i+1) + ".[ ] " + list[i][:-2]
        print (currentstring)

def saving(list):
    os.remove("test.txt")
    test_file = open ('test.txt', 'w')
    for i in range(0, len(list)):
        test_file.write(list[i])
    test_file.close()

def isntdone(strng):
    if strng[-2]=='0':
        return 1
    else:
        return 0


oper=int(input("what you wanna do? (list[1], add[2], mark[3], archive[4])\n(Please give a number from the list above, or I cannot be executed!:():"))

if oper==1:
    printout(todolist)

elif oper==2:
    mustdo=str(input("What activity do you wanna add?: "))
    todolist.append(mustdo)
    todolist[-1]+="0\n"
    saving(todolist)
    print (mustdo, " added to the ToDo list.")

elif oper==3:
    printout(todolist)
    x=int(input("which of these do you wanna mark?:\n(Please give a number from the list above, or I cannot be executed!:():"))
    if isntdone(todolist[x-1]):
        todolist[x-1]=todolist[x-1][:-2] + "1\n"
        print("The selected activity got marked")
    else:
        print("That activity is already marked!:(")
    saving(todolist)

elif oper==4:
    newlist=[]
    for i in range(0, len(todolist)):
        if isntdone(todolist[i]):
            newlist.append(todolist[i])
    saving(newlist)
    print ("All the marked activities got deleted from the ToDo list.")
