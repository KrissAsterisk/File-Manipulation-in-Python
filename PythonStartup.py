import re
import os
     
class file_manipulation:

    def create_file(file_path): #file_path will be the name of the file
        try:
            open(file_path, "x")
                
        except Exception as e:
            print(f"Error: {e}")
    
    def delete_file(file_path): #file_path = name
        try:
                os.remove(file_path)
                print("Deletion complete.")
        except Exception as e:
            print(f"Error: {e}")
        
    def read_file(file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
                if(content == ""):
                    return("This file is empty")
                else: 
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
                    print(f"{word}: {occurence}") #TODO: Implement a sorting algorithm for maximum style points
            
        except Exception as e:
            print(f"Error: {e}")
            
class dir:

    def read_dir(): #make this more readable
        #i = 0
        print("Current Directory: ") 
        entries = os.listdir()
        for entry in entries:
            print(f">  {entry}")
            # i += 1
            # if(i == 3):
            #     print()
            #     i = 0
            # if(entry == entries[len(entries)-1]):
            #     print(f" {entry}\n")

            # else:
            #     print(f" {entry}" , end=",")

        print()

    def change_dir(path):
            try:
                os.chdir(path)
            except Exception as e:
                print(f"Invalid dir: {e}.")


def sys_check(): # for clarity purposes
    if(os.name == "nt"): # Windows
        return True
    elif(os.name == "posix"): # Mac or Linux
        return False
    else:
        return True

class main:
    if(sys_check()): # for cmd purposes
        def clear(): os.system("CLS")
    else:
        def clear(): os.system("clear")


    while(True):
        clear() # ide doesnt clear properly, run in cmd
        dir.read_dir()
        file_choice = input(f"Input a File name / Directory to navigate (.. to go back)\nTo create a file/dir:\n> Create File\n> Make Directory\n\n>>> ").strip()
        


        match file_choice[:4]: 

            case "exit":
                exit()

            case "crea": #create files
                file_name = input("Enter the name of the file to be created: ")
                file_manipulation.create_file(file_name)
                if(file_name.endswith(".txt")):
                    print("You've created a text file!")

            case "make": # TBD: make dirs
                pass

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
                            case "dele": # delete file 
                                file_manipulation.delete_file(file_choice)
                                break
                            case _:
                                print("Invalid Option.")

                elif(os.path.isdir(file_choice)):
                    dir.change_dir(file_choice)

                else:
                    print("Invalid Option.")

