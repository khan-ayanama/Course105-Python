# compare list
# is vs equal(==)

fruits1 = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
fruits2 = ["banana", "fruit2"]
fruits3 = ["banana", "fruit2"]

print(fruits1 == fruits2)
print(fruits2 == fruits3)  # if value is same or not not calculate address

print(fruits2 is fruits3)  # Checks values are at same address


# split method
# convert string to list


# split method
# user_info = "harshit,24".split(",")
# print(user_info)
# name, age = 'harshit,24'.split(',')
# print(name)
# print(age)

names = "Ayan Anand Aster Andrew"
print(names.split(" "))  # here names will  turn into list

names = "Ayan Anand Aster Andrew".split(" ")
print(names)


# if you want to change string into list
# then use split method at the time of declaring the string not after that
# names = "Ayan Anand Aster Andrew".split(" ")
# print(names)


# join method  ---> Changes list into string
user_info = ["harshit", "24"]
ans = " ".join(user_info)
print(ans)
