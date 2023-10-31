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

* `Whitespace Matters:` Python uses indentation (whitespace) to define code blocks, unlike many other programming languages that use braces or keywords. This enforces a consistent and readable coding style.

* `Everything is an Object:` In Python, everything is an object, including integers, strings, functions, and even classes. This reflects the language's object-oriented nature.

* `No Mandatory Semicolons:` Unlike languages like C++ or Java, Python doesn't require semicolons at the end of statements. Statements are usually separated by newlines.

* `Python Enhancement Proposals (PEP):` PEPs are design documents that provide information to the Python community or propose new features. Major language changes and enhancements go through a PEP process.

* `Mutable and Immutable Objects:` Python objects are categorized as mutable (can be changed after creation) and immutable (cannot be changed after creation). For example, lists are mutable, while strings are immutable.

* `Duck Typing:` Python follows the philosophy of "duck typing," which means the type of an object is determined by its behavior rather than its explicit type. If it walks like a duck and quacks like a duck, it's a duck!

* `Global Interpreter Lock (GIL):` Python's GIL is a mutex that allows only one thread to execute in the interpreter at a time. This can limit the effectiveness of multi-threading for CPU-bound tasks.

* `Zen of Python:` "The Zen of Python" is a collection of guiding principles for writing computer programs in Python. You can access it by typing import this in a Python interpreter.

* `List Comprehensions:` Python supports list comprehensions, which provide a concise way to create lists. They combine the for loop and the creation of new elements into a single line.

* `Function Annotations:` You can add annotations to function parameters and return values to provide hints about their intended types or usage. However, these annotations are not enforced by the interpreter.

* `Private Variables and Methods:` Although Python doesn't have strict access modifiers like other languages, a common convention is to prefix "private" variables and methods with an underscore (e.g., _private_var).

* `Magic Methods:` Python has a set of special methods, often referred to as "magic methods" or "dunder methods" (double underscore), that allow you to define how objects behave in various contexts (e.g., __init__, __str__).

* `Keyword Arguments:` In function calls, you can use keyword arguments to specify values for parameters by name, regardless of their position in the parameter list.

* `Docstrings:` Python encourages the use of docstrings to document functions, classes, and modules. These docstrings can be accessed using the help() function.

* `Virtual Environments:` Python provides a way to create isolated environments for your projects using virtual environments. This helps manage dependencies and avoid conflicts.  

## Data Types in Python

Python is a dynamically typed language, meaning you don't need to explicitly declare the data type of a variable. Python has several built-in data types:

* `Integers (int):` Whole numbers without decimal points.
* `Floating-Point Numbers (float):` Numbers with decimal points.
* `Strings (str):` Sequence of characters, enclosed in single (' ') or double (" ") quotes.
* `Booleans (bool):` Represents the truth values True or False.
* `Lists (list):` Ordered collection of items.
* `Tuples (tuple):` Similar to lists, but immutable (can't be changed after creation).
* `Dictionaries (dict):` Collection of key-value pairs.
* `Sets (set):` Unordered collection of unique items.
* `NoneType (None):` Represents the absence of a value.

## Variables

Variables are used to store data values in Python. You don't need to declare the data type explicitly; Python determines it dynamically. To assign a value to a variable, you simply use the assignment operator =. Variable names must follow some rules:

* Must start with a letter (a-z, A-Z) or underscore _.
* Can contain letters, digits, and underscores.
* Must not be a Python keyword (e.g., if, while, def, etc.).
* Case-sensitive (e.g., myVariable and myvariable are different).

## Identifiers

Identifiers are names given to entities like variables, functions, classes, etc. They help in recognizing and distinguishing different entities in the code. Identifiers follow similar rules as variable names:

* Can start with a letter (a-z, A-Z) or underscore _.
* Can contain letters, digits, and underscores.
* Must not be a Python keyword.
* Case-sensitive.

## Type of Data type

```python
    a = 5
    print(type(a))
```

## Dynamically type langauge

You don't need to define the type of variable.

## Print function in python

```python

    # Multi line statement when you want to use more than one line 
    item_one = 5
    item_two = 4
    item_three = 6
    total = item_one + \
            item_two + \
            item_three

    print(total)

    # Waiting for the User
    # input("\n\nPress the enter key to exit.")
    # print("New line")

    print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    # Printing a simple string
    print("Hello, World!")

    # Printing multiple values with a custom separator
    name = "Alice"
    age = 30
    print("Name:", name, "Age:", age, sep=' - ')

    # Printing without moving to the next line (end='')
    print("Hello", end='')
    print(", World!")

    # Printing to a file (you can also use 'file' parameter)
    with open("output.txt", "w") as f:
        print("This will be written to the file", file=f)

    # Flushing the output buffer immediately
    print("Immediate flush", flush=True) 
```

* value1, value2, ...: These are the values you want to print. You can provide multiple values separated by commas.
* sep: The separator between the values. By default, it's a space (' '). You can change it to any character or string you want.
* end: The string that is printed at the end. By default, it's a newline character (\n), which moves the cursor to the next line. You can  change it to any string you want.
* file: Specifies where the output should be directed. By default, it's the standard output (sys.stdout).
* flush: If True, it flushes the output buffer, ensuring the output is displayed immediately.

## Types of operator

1. Arithmatical --> +, -, /, //, %, **
2. Relational --> >, <, >=, ==, !=
3. Logical
4. Conditional
5. Assignment --> +=, -=, /=, %=
6. Bitwise
7. Arithmatical Assighment
8. Identity operator --> is and is not
9. Membership operator --> in and not in

## Left shift and Right shift >>, <<

a = 5 << 3 --> shortcut for ans = (2^3 * 5 = 40)

* left shift always zerofill
* right shift can be zerofill or 1 fill depending about MSB
