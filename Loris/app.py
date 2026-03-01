import os
import platform
import time
import run_code as r

directory_path = "."

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

print("##############################################")
print("LORIS . . . A LANGUAGE THAT UNDERSTAND YOU")
print("##############################################")
time.sleep(1)
clear()

while True:
    file_directory = []
    index = 0
    for entry in os.listdir(directory_path):
        full_path= os.path.join(directory_path, entry)
        if os.path.isfile(full_path):
            temporary = full_path
            if temporary.endswith(".loris"):
                file_directory.append(temporary)
    if len(file_directory) == 0:
        print("No .loris files found.")
        break
    try:
        clear()
        print("##############################")
        print("Which you want to run? ")
        print("##############################")

        print("\n ")
        for index in range(0, len(file_directory)):
            print(index,".","[", file_directory[index],"]")
        file_selector = int(input("Type the number that corespond to the file directory(Or -1 to exit): "))
    except:
        print("That's not an number, Try again!")
        time.sleep(2)
        continue
    if file_selector >= len(file_directory):
        print("That file does not exist, Try again!")
        time.sleep(2)
        continue
    else:
        if file_selector == -1:
            clear()
            print("Bye!")
            exit()
        elif file_selector < -1:
            print("You can't go beyond that, Try again!")
            time.sleep(2)
            continue
        else:
            break
clear()
program = r.read_file_content(file_directory[file_selector])
r.run_program(program)
print("\n############################################")
print("End of program . . . Press Enter to Exit")
print("############################################")
input()
