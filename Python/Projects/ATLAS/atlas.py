from pathlib import Path
from copy import deepcopy
import json

# In this program there are various checks that i occasionally remember to put such as the check to lower the inputs and storage for correct  
# searching later, the check to see whether a task or note even exists before removing it. or if a task already exists before adding it
# There needs to be a proper solution to this problem like wrapping it into a function (impchecks)
# Also make your code consistent throughout as it is very rough now. Also fix some logic and find patterns

class atlas:

    @staticmethod
    def __init__():
        """ All the initializing functionality (files and folders made) that you want to be done before anything else """     
        

    def loadExistingData(self):
        pass
    

    def collectData(self):
        pass


    def impChecks(self):
        pass
    

    def successMessage(self):
        pass


    def create_user(self, userName : str):
        # Add the functionality for a username containing two words

        # Initiating the necessary files and folders if not present in sourcePath, and writing the new user id & userName in usersList
        userName = userName.lower()
        sourcePath = Path.home() / 'database'
        sourcePath.mkdir(exist_ok=True)
        listOfExistingFilesAndFolders = [n for n in sourcePath.iterdir()]
        usersList = sourcePath / 'users.txt'
        if 'users.txt' in str(listOfExistingFilesAndFolders):
            userID = len(listOfExistingFilesAndFolders)
        else:
            userID = len(listOfExistingFilesAndFolders)+1
            usersList.touch()
            
        userData = f'[{userID}, {userName}]\n'
        if userName in str(listOfExistingFilesAndFolders):
            print(f'User {userName} already exists! Please try with a different userName')
            return
        usersList.write_text(userData)


        # Initiating user files

        userPath = sourcePath / f'user_{userName}_{userID}'
        userPath.mkdir()
        items = ['books.json','notes.json','tasks.json','user_metadata.json','automationScripts']

        for item in items:
            tempPath = userPath / item
            if '.' in item:
                tempPath.touch()
            else:
                tempPath.mkdir()

        metadata = {
            'userID'   : userID,
            'userName' : userName,
            'preferences' :    {},
            'command_history': [],
            'search_history':  []
        }
        metadata = json.dumps(metadata, indent=4)

        tempPath = userPath / 'user_metadata.json' # In items[3]
        tempPath.write_text(str(metadata))

        print(f"User registered successfully! See at {userPath}")



    def add_book(self, userName, userID, book : str = '', author : str ='not specified'):
        book = book.lower()

        # Collect book and author name
        while not book:
            n = input("Please enter the book -->")
            if not n:
                n = input("book is must to enter -->")
            else:
                book = n.lower()
        if author == 'not specified':
            n = input("Do you want to specify the Author Name? Leave empty if not -->")
            if n:
                author = n.lower()
    
        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        booksPath = userPath / 'books.json'
        books = booksPath.read_text()
        try:
            books = json.loads(books)
        except:
            books = {}

        # Add new book
        if not books:
            books = {
                book : {
                    'author' : author,
                    'booknotes' : []
                }
            }
        else:
            if book in books.keys():
                print("The book already exists!")
                return 
            else:
                books[book] = {
                    'author' : author,
                    'booknotes' : []
                }
        books = json.dumps(books, indent=4)
        booksPath.write_text(books)
        print(f"The book {book} has been successfully added!")
    

    def remove_book(self, userName, userID, book : str = ''):
        book = book.lower()
        
        # Collect book
        while not book:
            n = input("Please enter the name of the book to remove -->")
            if not n:
                n = input("book is must to enter -->")
            else:
                book = n.lower()
            
        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        booksPath = userPath / 'books.json'
        books = booksPath.read_text()
        try:
            books = json.loads(books)
        except:
            books = {}

        # Remove the book
        if books:
            try:
                books.pop(book)
            except KeyError:
                print('Book not found!')
                return
            else:
                books = json.dumps(books, indent=4)
                booksPath.write_text(books)
        else:
            print('Book not found!')
            return
        
        print(f"The book {book} has successfully been removed")


    def add_note(self, userName, userID, note : str = ''):
        note = note.lower()
        
        # Collect the note
        while not note:
            n = input("Enter the note --> ")
            if not n:
                n = input("Enter the note it is must --> ")
            else:
                note = n.lower()

        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        notesPath = userPath / 'notes.json'
        notes = notesPath.read_text()
        try:
            notes = json.loads(notes)
        except:
            notes = []

        # Add the note
        if not notes:
            notes = [
                f'{note}'
            ]
            notes = json.dumps(notes, indent=4)
            notesPath.write_text(notes)
        else:
            if note in notes:
                print("The note already exists!")
                return
            else:
                notes.append(note)
                notes = json.dumps(notes, indent=4)
                notesPath.write_text(notes)
        print(f"The note {note} has been successfully added!")


    def remove_note(self, userName, userID, note : str = ''):
        note = note.lower()
        
        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        notesPath = userPath / 'notes.json'
        notes = notesPath.read_text()
        try:
            notes = json.loads(notes)
        except:
            notes = []
            print("No note exists!")

        # List the existing notes to the user if user did not specify a note
        if not note: 
            for index, note in enumerate(notes):
                print(f' {index} -> {note}')
            index = int(input('\n\n Enter the index of the note you want to remove --> '))
            while index == '' or index >= len(notes) or index < 0:
                index = int(input('Enter a valid index --> '))
            # Remove the note
            removed_note = notes.pop(index)
        else:
            if note in notes and notes:
                removed_note = note
                notes.remove(note)
            else:
                print("Note cannot be found!")
                return

        notes = json.dumps(notes, indent=4)
        notesPath.write_text(notes)
        print(f'Removed the note {removed_note}')



    def add_task(self, userName, userID, task : str = ''):
        task = task.lower()
        
        # Collect the task
        while not task:
            n = input("Enter the task to add --> ")
            if not n:
                n = input("Enter the task it is must --> ")
            else:
                task = n.lower()

        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        tasksPath = userPath / 'tasks.json'
        tasks = tasksPath.read_text()
        try:
            tasks = json.loads(tasks)
        except:
            tasks = {}

        # Add the task
        if not tasks:
            tasks = {
                "totalTasks" : 1,
                "completed" : {

                },
                "incomplete" : {
                    0 : f'{task}'
                }
            }
            tasks = json.dumps(tasks, indent=4)
            tasksPath.write_text(tasks)
        else:
            tasks['incomplete'][tasks["totalTasks"]] = f'{task}'
            tasks["totalTasks"] +=1
            tasks = json.dumps(tasks, indent=4)
            tasksPath.write_text(tasks)


    def remove_task(self, userName, userID, task : str = ''):
        task = task.lower()
        
        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        tasksPath = userPath / 'tasks.json'
        tasks = tasksPath.read_text()
        try:
            tasks = json.loads(tasks)
        except:
            tasks = {}

        # List the existing tasks to the user if user did not specify a task
        if not task:
            print("Incomplete tasks -->\n\n")
            for index, task in tasks["incomplete"].items():
                print(f' {index} -> {task}')
            print("Completed tasks -->\n\n")
            for index, task in tasks["completed"].items():
                print(f' {index} -> {task}')

            index = int(input('\n\n Enter the index of the note you want to remove --> '))
            while index == '' or index >= tasks["totalTasks"] or index < 0:
                index = int(input('Enter a valid index --> '))

            # Remove the task
            if index in tasks["completed"]:
                tasks["completed"].pop(index)
            if index in tasks["incomplete"]:
                tasks["incomplete"].pop(index)

        else:
            # Remove the task
            try: 
                index = [k for k,v in tasks["incomplete"].items() if v == task]
                if index:
                    tasks["incomplete"].pop(index[0])
                else:
                    raise Exception
            except Exception:
                index = [k for k,v in tasks["completed"].items() if v == task]
                if index:
                    tasks["completed"].pop(index[0])
                else:
                    print("Task not found!")
                    return
            
        tasks = json.dumps(tasks, indent=4)
        tasksPath.write_text(tasks)
        print(f"Task {task} has been removed successfully!")


    def complete_task(self, userName, userID, task : str = ''):
        task = task.lower()

        # Load existing data
        userPath = Path.home() / 'database' / f'user_{userName}_{userID}'
        tasksPath = userPath / 'tasks.json'
        tasks = tasksPath.read_text()
        try:
            tasks = json.loads(tasks)
        except:
            tasks = {}

        # Collect the task
        while not task:
            n = input("Enter the task to complete --> ")
            if not n:
                n = input("Enter the task it is must --> ")
            else:
                task = n.lower()

        # Complete the task by just moving the key value pair from uncompleted to completed
        if task in tasks["incomplete"].values():
            index = [k for k,v in tasks["incomplete"].items() if v == task]
            # Add the key value pair to the completed dict
            tasks["completed"][index] = task
            # Remove from the incomplete dict
            tasks["incomplete"].pop(index)
            tasks = json.dumps(tasks, indent=4)
        else:
            print("Task cannot be found!")
            return
        

# Testing

#x = atlas()
#x.create_user("Arsalan")
#x.add_book("arsalan", "1", "AtomicHabits")
#x.remove_book("arsalan", "1", "AtomicHabits")
#x.add_note("arsalan", "1")
#x.remove_note("arsalan", "1")