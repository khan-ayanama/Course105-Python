# Strip method

name = "            Ayan Khan          "
dots = "..........."

# lstrip() method   ----->  To remove space from left side
print(name.lstrip()+dots)

# rstrip method
print(name.rstrip()+dots)

# strip() method
print(name.strip()+dots)

# replace() method
print(name.replace(" ", "")+dots)

# replace() method
# find() method

string = "she is beautiful and she is good is dancer"
print(string.replace(" ", "_"))
print(string.replace("is", "was", 3))


# find() method

print(string.find("is"))
print(string.find("is", 6))
is_pos1 = string.find("is")  # is_pos1 ---> number
is_pos2 = string.find("is", is_pos1+1)
print(is_pos2)
