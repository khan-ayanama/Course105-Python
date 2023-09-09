# Strings are immutable

string = "string"
# string[1] = "T"     ----> It's not how you can change string

print(string.replace('t', "T"))
print(string)  # String is not changed above change not applied

# Assignment operator

name = 'Ayan'
name = 'Ayan' + "khan"
print(name)
name += "khan2"
print(name)
