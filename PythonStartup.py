

import re
import os


boolean = True     
class file_manipulation:

    def create_file(file_path): #file_path will be the name of the file
        try:
            with open(file_path, "x") as file:
                file.close()
        except Exception as e:
            print(f"Error: {e}")
    
    def delete_file(file_path): #file_path = name
        try:
            with open(file_path, "r"):
                os.remove(file_path)
        except Exception as e:
            print(f"Error: {e}")

    def read_file(file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
            return content
        except Exception as e:
            print(f"Error: {e}")

    def overwrite_file(file_path, data):
        try:
            with open(file_path, "w") as file:
                file.write(data)
        except Exception as e:
            print(f"Error: {e}")

    def analyze_file(file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read().lower().strip()
                words = re.findall(r'\b\w+\b', content) # w+ - list with any word with 1 or more occurences
                word_dictionary = {}
                for word in words:
                    if word in word_dictionary:
                        word_dictionary[word] += 1
                    else:
                        word_dictionary[word] = 1
                for word, occurence in sorted(word_dictionary.items(), key=lambda x: (-x[1], x[0])): #.items - (key,value) tuples | sorted key - use value from tuple for sorting | lambda = anonymous func - x[0] is the key x[1] is the value | negative x[1] - sort by descending value first | non-negative x[0] - sort keys alphabetically second
                    print(f"{word}: {occurence}")
            
        except Exception as e:
            print(f"Error: {e}")
            
class dir:

    def read_dir():
        print("Current Dirrectory: ")
        print(os.listdir(), "\n")
        return os.listdir()

    def change_dir(path):
            try:
                os.chdir(path)
            except Exception as e:
                print(f"Invalid dir: {e}.")



class main:
    while(True):
        os.system("CLS")
        dir.read_dir()
        file_choice = input("Input a File name or Directory:\n\n>>> ").strip()
        
        #Asks what to do & shows current dir
        #User inputs something irrlevat - nothing happens
        #User inputs file or directory - it checks whether its a directory
        #if yes: it goes to that directory
        #if no: it stores the path of the file
        #with the path of the file, the user can now read/write/etc.

        match file_choice[:4]: 

            case "exit":
                exit()

            case "crea": #create files
                while True:
                    dir.read_dir()
                    file_name = input("Enter the name of the file (exit to quit): ")
                    if(file_name == 'exit'):
                        break
                    file_manipulation.create_file(file_name)


            case _: # manipulate files or enter dir
                if(os.path.isfile(file_choice)):
                    while True:
                        choice = input("What would you like to do with this file?\n> Read\n> Overwrite\n> Analyze\n> Delete\n> Exit\n\n>>> ").strip().lower()[:4]
                        match choice:
                            case "exit":
                                break
                            case "read": # read file
                                print(file_manipulation.read_file(file_choice))
                            case "over": # overwrite file
                                file_manipulation.overwrite_file(file_choice, input("Input: "))  
                            case "anal": # analyze file
                                file_manipulation.analyze_file(file_choice)
                            case "dele": # delete file (doesn't work because youre accesing the file....)
                                file_manipulation.delete_file(file_choice)

                            case _:
                                print("Invalid Option.")

                elif(os.path.isdir(file_choice)):
                    dir.change_dir(file_choice)

                else:
                    print("Invalid Option.")

