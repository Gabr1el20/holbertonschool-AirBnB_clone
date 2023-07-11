# AirBnB clone: The CONSOLE
## Requirements
-  Allowed editors: vi, vim, emacs
-  All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-  All your files should end with a new line
-  The first line of all your files should be exactly #!/usr/bin/python3
-  A README.md file, at the root of the folder of the project, is mandatory
-  Your code should use the pycodestyle (version 2.7.*)
-  All your files must be executable
-  The length of your files will be tested using wc
-  All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
-  All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
-  All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
-  A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
  
## Description of the proyect
The objective of this instance of the project is to replicate the management of the airBnB page console, and to implement the persistency of all our previous objects already created, with the help of the file storages engine.
### Command interpreter
Used to manipulate data without a visual interface, like in a Shell.

## Content of the repository
### directories

| Directory | Description |
| --- | --- | 
| [models](models) | Contains all the classes used for the project. |
| [tests](tests)  | Contains all the Unit Tests files of the project. |
| [models/engine](models/engine)  | Contains the FileStorage class, the one in charge of the storage engine. |

### Files

| File | Description |
| --- | --- | 
| [console.py](console.py) | Command interpreter |
| [models/base_model](models/base_model) | Contains the BaseModel Class |
| [models/engine/filestorage.py](models/engine/file_storage.py) | Contains the FileStorage Class |

# Usage of the Console
The console works in two modes:
### Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```


#### AUTHORS
[Alejandro Martinez](github.com/alemao51092)

[Gabriel Delgado](github.com/gabr1el20)

[Franco Correa](github.com/francorr1)
