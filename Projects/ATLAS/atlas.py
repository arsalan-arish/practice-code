from pathlib import Path
from copy import deepcopy
import json

class atlas:
    
    def create_user(self, name):

        # Initiating the necessary files and folders if not present in sourcePath, and writing the new user id & name in usersList
        name = name.lower()
        sourcePath = Path.home() / 'database'
        sourcePath.mkdir(exist_ok=True)
        listOfExistingFilesAndFolders = [n for n in sourcePath.iterdir()]
        usersList = sourcePath / 'users.txt'
        if 'users.txt' in str(listOfExistingFilesAndFolders):
            userID = len(listOfExistingFilesAndFolders)
        else:
            userID = len(listOfExistingFilesAndFolders)+1
            usersList.touch()
            
        userData = f'[{userID}, {name}]\n'
        if name in str(listOfExistingFilesAndFolders):
            print(f'User {name} already exists! Please try with a different name')
            return
        usersList.write_text(userData)


        # Initiating user files

        userPath = sourcePath / f'user_{name}_{userID}'
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
            'name' : name,
            'preferences' :    {},
            'command_history': [],
            'search_history':  []
        }
        
        tempPath = userPath / 'user_metadata.json' # In items[3]
        tempPath.write_text(str(metadata))

        print(f"User registered successfully! See at {userPath}")



    def add_book(self, userName, userID, bookName, authorName='Not specified'):
        pass