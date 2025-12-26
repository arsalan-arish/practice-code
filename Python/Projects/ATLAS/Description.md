🚀 CLIENT REQUIREMENT — PYTHON MEGA PROJECT
Project Name: Atlas: A Modular Personal Knowledge OS
I want a local, offline, command-line personal knowledge operating system that:
1) Acts as a Database
You must implement your own mini-database engine using:


Python files

Data structures (dicts, lists, sets)

Optional JSON
The database must support:


Creating “entities” (Notes, Books, Tasks, Users)

CRUD operations

Indexing (search by keyword)

Tags

Versioning (each update creates a new version)
2) Acts as a CLI Application
I want a fully interactive terminal interface with commands like:
add note "Python references" --tags coding python list notes search "memory leak" show note 23 rollback note 23 to v2 add book "Clean Code" --author Martin list tasks --status incomplete 
You must build:


Command parser

Error handling

Help system

Interactive mode + one-shot command mode
3) Uses Clean Architecture
Your code must follow:


OOP (classes for Note, Book, Task, User, Tag, Database, CommandRunner)

Separation of concerns

No spaghetti code

No global variables

Modules for:


database/

models/

cli/

utils/
4) Handles References & Copies Properly
There will be many objects referencing each other (tags, users, notes).
You must avoid:


Accidental shared-state bugs

Mutating one object unintentionally affecting others

Shallow copy pitfalls
Examples:


Notes can share tags

A tag rename should update all connected notes

Versioning must clone objects properly without breaking references
This specifically tests your reference vs copy mastery.
5) Has a Full Version Control System (Mini-Git)
For every object:


Every update creates a new version

Versions stored as snapshots

User can rollback

Version numbers must be consistent
This forces:


Deep copying

Data diffing

History tracking

File storage consistency
6) Implements User Profiles
Each user has:


Name

Preferences

History of commands

Saved searches
User switching must be supported:
switch user arsalan 
7) Robust Search Engine
Must support:


Keyword search

Tag search

Fuzzy search (approx match)

Recent items

Regex search (optional but recommended)
This forces you to use:


Lists

Dictionaries

Sets

Higher-order functions

Custom sort keys
8) Import/Export System
Allow users to export:


Notes

Tasks

Books
To:

JSON

Plain text
Also allow importing JSON dumps.
This tests:


Serialization

Parsing

File handling

Clean API design
9) Automation Scripting
I want a scripts/ folder where users can write Python scripts that hook into the OS.
Example:
on_startup.py daily_summary.py weekly_backup.py 
Your system must run these scripts automatically.
10) Optional but Highly Requested
If you want to go even more insane:


Add encryption for notes

Add a sync protocol between two devices

Add a simple local flask API

Add a curses UI (terminal UI)
