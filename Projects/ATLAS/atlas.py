from pathlib import Path


class atlas:
    
    def create_user(self, name):
        lst = ['books.py','notes.py','tasks.py','user.py','scripts']
        
        for i in lst:
            p = Path('database') / f'user_{name}_' / f'{i}'
            p.parent.mkdir(exist_ok=True, parents=True)
            if i.__contains__('.'):
                p.touch()
            else:
                p.mkdir()

        p = Path('database') / f'user_{name}' / 'user.py'

        with open(p,"w") as f:
            pass
