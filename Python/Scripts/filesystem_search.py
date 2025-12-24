from pathlib import Path
from os import name

def get_roots():
    roots = []

    if name == "nt":  # Windows
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            drive = Path(f"{letter}:/")
            if drive.exists():
                roots.append(drive)
    else:  # Unix-like systems
        roots.append(Path("/"))

    return roots


def search_system(pattern):
    for root in get_roots():
        try:
            for path in root.rglob(pattern):
                print(path)
        except PermissionError as e:
            print(e)


#search_system("*.mp3")

# or we can only search the user directory

def search_user_dir(pattern):
    results = []

    p = Path.home()
    for path in  p.rglob(pattern):
        results.append(path)

    return results


for path in search_user_dir("*.mp3"):
    print(path)