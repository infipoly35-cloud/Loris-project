import os
import platform
import time
import run_code as r

directory_path = "."


def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")


def get_loris_files(path):
    files = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path) and entry.endswith(".loris"):
            files.append(full_path)
    return files


print("##############################################")
print("LORIS . . . A LANGUAGE THAT UNDERSTANDS YOU")
print("##############################################")
time.sleep(1)

while True:
    clear()
    file_directory = get_loris_files(directory_path)

    if not file_directory:
        print("No .loris files found.")
        break

    print("##############################")
    print("Which file do you want to run?")
    print("##############################\n")

    for i, file in enumerate(file_directory):
        print(f"{i}. [ {file} ]")

    choice = input("\nType the number (or -1 to exit): ")

    # Validate number
    if not choice.lstrip("-").isdigit():
        print("That's not a number. Try again!")
        time.sleep(2)
        continue

    file_selector = int(choice)

    if file_selector == -1:
        clear()
        print("Bye!")
        break

    if file_selector < 0 or file_selector >= len(file_directory):
        print("That file does not exist. Try again!")
        time.sleep(2)
        continue

    # Valid selection → break loop
    break


# Run selected program
clear()
program = r.read_file_content(file_directory[file_selector])
r.run_program(program)

print("\n############################################")
print("End of program . . . Press Enter to Exit")
print("############################################")
input()