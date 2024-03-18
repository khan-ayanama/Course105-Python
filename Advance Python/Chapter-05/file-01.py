# Module
# A module is a file containg python definations and statements.
# A moudle is a file containg gruop of variables, methods, function and classes etc.
# They are executed only te first time the module name is encountered in an import statemetn
# The file name is the moudle name with the suffix .py appended.
# Example: myMoudle.py

# Type of Modules:
# User defined modules
# Built-in Modules: array, math, numpy, sys

# When and Why use Module
# In a very large project where your should seperate similar logic
# helps to debug
# It can be reused

# How to use Module
# import module_name
# import module_name as alias_name
# from module_name import func1,func2,func3,class1
# from module_name import *

# Modules can import other Modules

# Using function or method in module
# import module_name
# module_name.Func(param)


# If you are importing * names will not imported if it begins with underscore.
# NOTE: When naming folder name don't use space between them

# Moudle Search Path
# First searches built-in moudle
# searches file name in the directory given by sys.path of PYTHONPATH
# Installation dependent default path

# PYTHONPATH is a list of directory names, with the same syntax as the shell variable PATH.