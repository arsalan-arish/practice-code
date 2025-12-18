# Imports
from pathlib import Path

# Functions

def table_writer(n,l):     # This function takes the path/directory and a number and creates a single txt file with the table of that number
    l = l + rf"\table{n}.txt"
    # Path(l).touch(exist_ok=True) 
    with open(l,"w") as p:
        for i in range (1,11):
            line = f"{n} x {i} = {n*i}"
            p.write(f"{line}\n")


def tables_writer(n1,n2,l):       # This function makes the above function generate table files for a set of numbers from n1 till n2
    while (n1<=n2):
        table_writer(n1,l)
        n1 += 1


def ask_location():        # This function collects a path/directory from the user as a string and returns it
    l = input("A --> Desktop\nB --> Downloads\nC --> Custom\n\nEnter the location to save it -->")
    if (l == "A"):
        l = r"C:\Users\Arsalan Arish\Desktop"
    elif (l == "B"):
        l = r"C:\Users\Arsalan Arish\Downloads"
    elif (l == "C"):
        l = input("\nEnter your custom path -->")
    
    temp = input("Do you want to save files in a new folder?(y/n)\n-->")
    if(temp == "y"):
        fo = input("Enter Folder name-->")
        l = l + rf"\{fo}"
        Path(l).mkdir()
    elif (temp == "n"):
        return
    return l


def ask_num():
    n = int(input("Enter the number of which table to make-->"))
    return n


def ask_numrange():
    n1 = int(input("Enter the first number-->"))
    n2 = int(input("Enter the last number-->"))
    return n1, n2




# Program
print("\n\n\n\n\n\n\nWelcome to table generator!👋")

a = int(input("Enter 1 if you want the table of a number\nEnter 2 if you want the tables for a set of numbers\n-->"))

if (a == 1):
    number = ask_num()
    location = ask_location()
    table_writer(number,location)
    print("Your table has been created!🎉")

elif (a == 2):
    first, last = ask_numrange()
    location = ask_location()
    tables_writer(first,last,location)
    print("\n\nYour tables have been created!🎉\n\n")
