import sys
import os

def Show_list():
    if len(sys.argv) < 3:
        with open("john.txt", "r") as file:
            filesize = os.path.getsize("john.txt")
            if filesize == 0:
                print("No todos to show")
            else:
                counter = 1
                for file_data in file:
                    print(str(counter)+". "+ file_data)
                    counter += 1

    elif len(sys.argv) < 4:
        print("No value is required after -l")

def Add_task():
    if len(sys.argv) < 3:
        print("Unable to add: no task provided")
    elif len(sys.argv) < 4:
        with open("john.txt", "a") as file:
            append = sys.argv[2] + "\n"
            file_data = file.write(append)

def Remove_task():
    if len(sys.argv) < 3:
        print("Unable to remove: no index provided")
    elif len(sys.argv) < 4:
        with open("john.txt", "r+") as file:
            var = file.readlines()
            index = int(sys.argv[2]) - 1
            remove_element = var[index]
            var.remove(remove_element)
            file.seek(0)
            file.truncate()
            file_data = file.writelines(var)

def Check_task():
    if len(sys.argv) < 3:
        print("Unable to check: no index provided")
    elif len(sys.argv) < 4:
        with open("john.txt", "r+") as file:
            var = file.readlines()
            index = int(sys.argv[2]) - 1
            counter1 = 0
            for f_contents in range(len(var)):
                if counter1 == index:
                    var[f_contents] = "[ x ]" + var[f_contents]
                counter1 += 1
            file.seek(0)
            file.truncate()
            file_data = file.writelines(var)

if len(sys.argv) < 2:
    print("$ todo" "\n"
           "Command Line Todo application" "\n"
           "=============================" "\n"
           "                             " "\n"
           "Command line arguments:" "\n"
           "   -l   Lists all the tasks" "\n"
           "   -a   Adds a new task" "\n"
           "   -r   Removes an task" "\n"
           "   -c   Completes an task""\n" )

elif sys.argv[1] == "-l":
    Show_list()

elif sys.argv[1] == "-a":
    Add_task()

elif sys.argv[1] == "-r":
    Remove_task()

elif sys.argv[1] == "-c" and len(sys.argv) < 4:
    Check_task()