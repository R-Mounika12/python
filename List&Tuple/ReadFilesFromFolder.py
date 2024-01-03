#Redaing a list of files from list of folders
import os

def listOfFilesInFolder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, FileNotFoundError

def main():
    folders = input("Enter the folder names with whitespaces in between ").split()
    #print(folders)

    for folder in folders:
        files, errorMessage = listOfFilesInFolder(folder)
        if files:
            print(f"files in {folder} ")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder} ", errorMessage)

main()

