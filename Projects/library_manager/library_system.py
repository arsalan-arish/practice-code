'''
Current Condition -->
The logic of the program is working great I just need to make it more interactive and make it error handling and make it more modular
1- Add error handling
2- Improve interaction generally and by Add colors, delays, and friendly output
3- Break it into more reusable modules
4- Break it into multiple files making it more structured
5- Create a save all function and add it after every operation to make it safer
6- Rewrite in OOP

'''





import json,os
from datetime import datetime

if not os.path.exists("Data"):
    os.mkdir("Data")
if not os.path.exists("Data\Books.json"):
    with open("Data\Books.json", "w") as f:
        pass

if not os.path.exists("Data\Users.json"):
    with open("Data\Users.json", "w") as f:
        pass

if not os.path.exists("Data\Records.json"):
    with open("Data\Records.json", "w") as f:
        pass

with open("Data\Books.json","r") as f:
    try:
        Books = json.load(f)
        i1 = Books[list(Books.keys())[-1]]["id"] + 1
    except Exception:
        Books = {}
        i1 = 1
    
with open("Data\Users.json","r") as x:
    try:
        Users = json.load(x)
        i2 = Users[list(Users.keys())[-1]]["id"] + 1
    except Exception:
        Users = {}
        i2 = 1
with open("Data\Records.json","r") as t:
    try:
        Records = json.load(t)
        i3 = Records[list(Records.keys())[-1]]["id"] + 1
    except Exception:
        Records = {}
        i3 = 1




def add_book():
    global i1
    name = input("Enter book name-->")
    author = input("Enter author name-->")
    year = int(input("Enter publishing year-->"))

    tempdict = {}
    tempdict["id"] = i1
    tempdict["author"] = author
    tempdict["year"] = year
    i1+=1
    Books[name] = tempdict
    print("Book has been added!")


def remove_book():
    name = input("Enter the name of the book to remove-->")
    Books.pop(name, None)
    print("your book has been removed!")


def list_books():
    if not Books == {}:
        for k,v in Books.items():
            print(k," --> ",end="")
            for s,j in v.items():
                print(j,"   ",end="")
            print("\n")
    else:
        print("No books currently")

def search_book():
    name = input("Enter the name of the book to search-->")
    if name in Books:
        print(name," --- ",end="")
        for k,v in Books[name].items():
            print(v,"   ",end="")
        print("\n")
    else:
        print("Book not found")




i2 = 1
def add_user():
    global i2
    name = input("Enter user name-->")
    age = int(input("Enter age -->"))
    

    tempdict = {}
    tempdict["id"] = i2
    tempdict["age"] = age
    i2+=1
    Users[name] = tempdict
    print("User has been added!")


def remove_user():
    name = input("Enter the name of the user to remove-->")
    if name in Users:
        Users.pop(name, None)
        print("This user has been removed!")
    

def list_users():
    for k,v in Users.items():
        print(k," --> ",end="")
        for s,j in v.items():
            print(j,"   ",end="")
        print("\n")

def search_user():
    name = input("Enter the name of the user to search-->")
    if name in Users:
        print(name," --- ",end="")
        for k,v in Users[name].items():
            print(v,"   ",end="")
    else:
        print("User not found")




i3 = 1
def borrow_book():
    global i3
    name = input("Enter the name of the book to borrow-->")
    if name in Books:
        user = input("Enter the name of the user-->")
        if user in Users:
            tempdict = {}
            tempdict["id"] = i3
            tempdict["time"] = datetime.now()
            tempdict["user"] = user
            i3+=1
            Records[name] = tempdict


def return_book():
    name = input("Enter the name of the book to return-->")
    if name in Records:
        Records.pop(name, None)


def list_borrows():
    for k,v in Records.items():
        print(k," --> ",end="")
        for s,j in v.items():
            print(j,"   ",end="")
        print("\n")



#Program
print("Hi, I am the librarian\nCommand me with the following commands")
print('''\n
1 ---> Add Book
2 ---> Remove Book
3 ---> Search Book
4 ---> List all Books

5 ---> Add User
6 ---> Remove User
7 ---> Search User
8 ---> List all Users

9 ---> Borrow a book
10---> Return a book
11---> List all Borrows 
12---> Exit
      

''')
while True:
    n = int(input("Enter the relevant number -->"))

    if   n == 1:
        add_book()
    elif n == 2:
        remove_book()
    elif n == 3:
        search_book()
    elif n == 4:
        list_books()
    elif n == 5:
        add_user()
    elif n == 6:
        remove_user()
    elif n == 7:
        search_user()
    elif n == 8:
        list_users()
    elif n == 9:
        borrow_book()
    elif n == 10:
        return_book()
    elif n == 11:
        list_borrows()
    elif n == 12:
        with open("Data\Books.json","w") as f:
            json.dump(Books, f)
        with open("Data\Users.json","w") as x:
            json.dump(Users, x)
        with open("Data\Records.json","w") as t:
            json.dump(Records, t)
        break
    else:
        print("Enter a correct number from the options")