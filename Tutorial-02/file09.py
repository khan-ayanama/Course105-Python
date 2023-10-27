# break and continue keyword

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("NEW")

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# step argument in range function

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
