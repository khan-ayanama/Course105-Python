# Python Day - 01

## Software

Software is a collection of programs and programs are the set of instructions.

### Software types:-

* System Software --> OS, Compiler, Driver, Coder, Linker.
* Application --> Desktop Windows
* Web Application
* Device Application
* AI/IOT

## Where we use Python

1. Desktop Application
2. Web Application
3. Network Application
4. Gaming Application
5. Data Science

## What is python?

Python is:

* Open Source --> Anyone can see the source code
* free ware --> No need to purchase
* Procedure + function + OOP's
* Platform independent

## .py vs .pyc

PY files contain Python source code file for a program, while . pyc files contain interpreted bytecode of an application.

## Platform dependent language

If any language creates .exe file they are platform dependent language, while compilation C/C++ code it needs .dll(document linking library file) file which will be provided by OS.

## Platform Independent Language

Software which is on server and which can run on any platform which is provide by an application like python and java  

Python is a Interpreter language it uses JIT (Just in Time) compiler which translate python source code to bytecode(.pyc)

Every OS has Python Virtual Machine (PVM) which only requires bytecode to run the program.  

PVM is a part of Python runtime environment.  

Python do not create .exe fiile

## Features of python

1. High Level Language
2. Expandable --> It can use with other language.
3. Portable --> (loosely coupled) It can portable between different platform.
4. Interpreted language
5. Rich Library

## Limitation of Python

1. Python is slow --> Because it is interpreter based language after using JIT compiler it is better than before.

## Flavour of python

1. CPython
2. JPython | JYThon --> with Java
3. RubyPython
4. IronPython --> with .Net App
5. Anaconda Python --> For BigData Application
6. StackPython --> Multithreaded application
7. PyPy --> Python for Python

## Step by Step Python Code Execution

1. Source Code in python editor | Notepad
2. JIT Compiler --> Converts source code to byte code with extension .pyc
3. PRE(Python runtime Environment) runs the bytecode in the Python Virtual Machine(PVM)

4. Python goes from the two environment:

   * Compile Time environement --> Syntax error
   * Runtime Envrionment --> Exception (error)

## Compile python code in command prompt

```cmd
    python -m py_comiple file.py
```

## Step of python execution right from beginning

The execution of Python code involves several steps, starting from writing the code to the actual execution by the Python interpreter. Here's a step-by-step overview of the process:

### 1. Writing Code

You write your Python code in a plain text file using a code editor or an Integrated Development Environment (IDE).

### 2. Lexical Analysis (Tokenization)

The Python interpreter first performs lexical analysis, which involves breaking your code into smaller units called tokens. Tokens can be keywords (e.g., if, while, def), identifiers (variable names), operators (e.g., +, -), and more.

### 3. Parsing (Syntax Analysis)

The tokens are then organized into a hierarchical structure based on the syntax rules of the Python language. This hierarchical structure is called the Abstract Syntax Tree (AST), and it represents the syntactic structure of your code.

### 4. Semantic Analysis

The interpreter checks the code for semantic errors, such as undeclared variables or incorrect data types. If any errors are found, the interpreter raises exceptions.

### 5. Bytecode Compilation

The Python code is compiled into bytecode. This bytecode is a lower-level representation of your code that is easier for the interpreter to execute. The bytecode is stored in .pyc files (compiled Python files) or in memory if the code is being executed interactively.

### 6. Execution by the Interpreter

The Python interpreter reads the bytecode and executes it line by line. It interacts with the Python Virtual Machine (PVM) to manage memory, variables, and other runtime aspects.

### 7. Runtime Execution

As the interpreter executes the bytecode, it performs various tasks, including variable assignments, function calls, and control flow (loops and conditionals).

### 8. Memory Management

The interpreter manages memory usage, creating and deleting objects as needed. Python has a built-in garbage collector that automatically deallocates memory for objects that are no longer in use.

### 9. Output and Interaction

If your code includes print() statements or other forms of output, the interpreter will display the output in the console. If your code interacts with the user through input functions like input(), the interpreter waits for user input.

### 10. Program Termination

Once the interpreter reaches the end of the script or encounters an explicit exit() call, the program execution terminates. At this point, any resources held by the program are released, and memory is deallocated.

## Here are some minute details and interesting aspects about Python

* Whitespace Matters: Python uses indentation (whitespace) to define code blocks, unlike many other programming languages that use braces or keywords. This enforces a consistent and readable coding style.

* Everything is an Object: In Python, everything is an object, including integers, strings, functions, and even classes. This reflects the language's object-oriented nature.

* No Mandatory Semicolons: Unlike languages like C++ or Java, Python doesn't require semicolons at the end of statements. Statements are usually separated by newlines.

* Python Enhancement Proposals (PEP): PEPs are design documents that provide information to the Python community or propose new features. Major language changes and enhancements go through a PEP process.

* Mutable and Immutable Objects: Python objects are categorized as mutable (can be changed after creation) and immutable (cannot be changed after creation). For example, lists are mutable, while strings are immutable.

* Duck Typing: Python follows the philosophy of "duck typing," which means the type of an object is determined by its behavior rather than its explicit type. If it walks like a duck and quacks like a duck, it's a duck!

* Global Interpreter Lock (GIL): Python's GIL is a mutex that allows only one thread to execute in the interpreter at a time. This can limit the effectiveness of multi-threading for CPU-bound tasks.

* Zen of Python: "The Zen of Python" is a collection of guiding principles for writing computer programs in Python. You can access it by typing import this in a Python interpreter.

* List Comprehensions: Python supports list comprehensions, which provide a concise way to create lists. They combine the for loop and the creation of new elements into a single line.

* Function Annotations: You can add annotations to function parameters and return values to provide hints about their intended types or usage. However, these annotations are not enforced by the interpreter.

* Private Variables and Methods: Although Python doesn't have strict access modifiers like other languages, a common convention is to prefix "private" variables and methods with an underscore (e.g., _private_var).

* Magic Methods: Python has a set of special methods, often referred to as "magic methods" or "dunder methods" (double underscore), that allow you to define how objects behave in various contexts (e.g., __init__, __str__).

* Keyword Arguments: In function calls, you can use keyword arguments to specify values for parameters by name, regardless of their position in the parameter list.

* Docstrings: Python encourages the use of docstrings to document functions, classes, and modules. These docstrings can be accessed using the help() function.

* Virtual Environments: Python provides a way to create isolated environments for your projects using virtual environments. This helps manage dependencies and avoid conflicts.  
