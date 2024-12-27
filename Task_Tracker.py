# Task Tracker

from fileinput import close
import sys

file = 'tasks.txt.txt'
fhand = open(file, 'r')

def view_tasks(file):
    print("\n***Current Menu***\n")
    with open(file, 'r') as menu:
        lines = menu.readlines()
        #print()
        print(*lines)
    print("\n***Current Menu***\n")
        #for element in lines:
         #   print(element.split())

#view_tasks(fhand)

def new_tasks(fhand):
    fhand = open(file, 'a')
    new_t = input("What is the Task Name?\n")
    status_pend = '\n' + new_t + ':Pending'
    fhand.write(status_pend)
    fhand = close()
#storage = []

def delete_task(file_path, lines_to_delete):
    #delete = input("What lines to delete?")  
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() not in lines_to_delete:
                file.write(line)

def complete_task(file_path, mark_as_complete):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() not in mark_as_complete:
                file.write(line)
            else:
                compl = line.strip()
                finder = compl.find(":")
                temp_task = compl[:finder]
                print(temp_task)
                status_pend = temp_task + ':Completed' + '\n'
                print(status_pend)
                file.write(status_pend)



def task_menu(int):
    if int == 0:
        view_tasks(file)
    elif int == 1:
        new_tasks(fhand)
    elif int == 2:
        delete = input("What lines to delete?\n")  
        delete_task(file, delete)
    elif int == 3:
        mark_as_complete = input("What task would you like completed?\n")
        complete_task(file, mark_as_complete)
    elif int == 4:
        print("Goodbye!")
        quit(int)
    
    else:
        print("Number is not an option!\n")
        return False

#print(delete)
while True:
    try:
        task_num = int(input("\nWhat task would you like to do?\n 0. See the Menu\n 1. Create a New Task\n 2. Delete an Existing Task\n 3. Complete A Task\n 4. Exit Program\n:"))
        task_menu(task_num)
    except:
        print("Try Again! Numbers 0-4")
        exit()
