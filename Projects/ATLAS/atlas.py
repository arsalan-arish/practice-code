from pathlib import Path
from copy import deepcopy

class atlas:
    
    def create_user(self, name):

        # Iniiating the necessary files and folders if not present
        name = name.lower()
        p1 = Path.home() / 'database'
        p1.mkdir(parents=True, exist_ok=True)
        temp = [n for n in p1.iterdir()]

        if 'users.txt' in str(temp):
            id = len(temp) # Debug this and the below line
            temp1 = p1 / 'users.txt'
            user = f'[{id}, {name}]\n'
            with open(temp1,"a") as f:
                f.write(user)

        elif 'users.txt' not in str(temp):
            temp1 = p1 / 'users.txt'
            temp1.parent.mkdir(exist_ok=True,parents=True)
            temp1.touch(exist_ok=True)
            id = len(temp)+1
            user = f'[{id}, {name}]\n'
            with open(temp1,"a") as f:
                f.write(user)


        # Initiating user files

        p2 = p1 / f'user_{name}_{id}'
        p2.parent.mkdir(exist_ok=True, parents=True)
        lst = ['books.py','notes.py','tasks.py','user_metadata.py','scripts']

        for i in lst:
            p3 = p2 / i
            if i.__contains__('.'):
                p3.parent.mkdir(exist_ok=True,parents=True)
                p3.touch(exist_ok=True)
            else:
                p3.mkdir(exist_ok=True)

        metadata = {
            'id'   : id,
            'name' : name,
            'preferences' :    {},
            'command_history': [],
            'search_history':  []
        }
        
        p4 = p2 / 'user_metadata.py'
        with open(p4,"w") as p4:
            p4.write(str(metadata))

        print(f"User registered successfully! See at {p2}")



    def add_book(self, user_name, user_id, bookname=None, authorname=None):
        pass

