import sys

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
    if len(sys.argv) < 3:
        with open("john.txt", "r") as file:
            counter = 1
            for file_data in file:
                print(str(counter)+". "+ file_data)
                counter += 1

    elif len(sys.argv) < 4:
        print("No value is required after -l")
elif sys.argv[1] == "-a":
    if len(sys.argv) < 4:
        with open("john.txt", "a") as file:
            append = sys.argv[2] + "\n"
            file_data = file.write(append)
    elif len(sys.argv) < 3:
        print("Unable to add: no task provided")

elif sys.argv[1] == "-r":
    if len(sys.argv) < 4:
        with open("john.txt", "r+") as file:
            var = file.readlines()
            index = int(sys.argv[2]) - 1
            remove_element = var[index]
            var.remove(remove_element)
            file.seek(0)
            file.truncate()
            file_data = file.writelines(var)
    elif len(sys.argv) < 3:
        print("Unable to remove: no index provided")

elif sys.argv[1] == "-c" and len(sys.argv) < 4:
    if len(sys.argv) < 4:
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
    elif len(sys.argv) < 3:
        print("Unable to check: no index provided")
