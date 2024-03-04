# Copyright (c) 2024 Joshua Haller
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#imports
import os

#renames files in the directory according to user input
def batchRename(directory, appendText):
    for filename in os.listdir(directory):                                                              #iterate over each file in the specified directory
        if os.path.isfile(os.path.join(directory, filename)):                                           #checks to see if the current item in the directory is a file
            base_name, extension = os.path.splitext(filename)                                           #splits the file name into its base and extension
            newFilename = f"{base_name}{appendText}{extension}"                                        #constructs the new file name by appending the user specified text to the end
            os.rename(os.path.join(directory, filename), os.path.join(directory, newFilename))          #renames the current file
            print(f"Appended '{appendText}' to {filename}.")                                            #prints a success message
    print("File renaming completed.")                                                                   #outputs a success message

#removes a specified string from the filenames in the directory
def removeString(directory, removeText):
    for filename in os.listdir(directory):                                                              #iterate over each file in the specified directory
        if os.path.isfile(os.path.join(directory, filename)):                                           #checks if the curent item in the directory is a file
            if removeText in filename:                                                                  #check if the specified string exists in the filename
                newFilename = filename.replace(removeText, "")                                          #constructs the new file name
                os.rename(os.path.join(directory, filename), os.path.join(directory, newFilename))      #renames the curret file
                print(f"Removed '{removeText}' from {filename}.")                                       #prints a success message
            else:
                print(f"Skipping {filename} as it does not contain '{removeText}'")                     #prints an error message if the text to be removed is not in the file name
    print("String removal completed.")                                                                  #prints a success message for the entire process


if __name__ == "__main__":
    directory = input("Enter the directory path where the files are located (press Enter for current directory): ")                             #prompts the user for the directory of the files to be renamed
    if directory == "":
        directory = os.getcwd()                                                                                                                 #use current directory if enter is pressed
    else:                                                                                                                   
        if not os.path.exists(directory):                                                                                                       #checks to see if the directory exists
            print("Error: The specified directory does not exist.")                                                                             #outputs an error message if the directory does not exist
            exit()

    #presents the choice of operation to the user
    print("Select an option:")
    print("1. Append text to filenames")
    print("2. Remove text from filenames")
    option = input("Enter option (1 or 2): ")

    if option == "1":
        appendText = input("Enter the text to append to the file names: ")                                                                        #prompts user to input what to append to the filenames
        batchRename(directory, appendText)                                                                                                        #calls the batchRename function
    elif option == "2":
        removeText = input("Enter the text to remove from the file names: ")                                                                      #prompts user to input the string to be removed
        removeString(directory, removeText)                                                                                                       #calls the removeText function
    else:
        print("Invalid option")
