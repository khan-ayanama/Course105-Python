# Global Variables and Global Keywords

a = 50


def func():
    a = 5
    # global a
    print("Value of local a ", a)
    print("Value of global a ", globals()['a'])

func()