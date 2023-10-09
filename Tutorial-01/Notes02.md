# Notes - 02

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
