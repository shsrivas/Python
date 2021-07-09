# Health management
def getdate():
    import datetime
    return datetime.datetime.now()


print("Do you want to : retrieve or lock?\n")
a = input()
print(f"whose file you want to {a} : harry, carry or merry\n")
b = input()


if a == "retrieve":
    print("what do you want to retrieve: exercise, diet\n")
    d = input()
    f = open(f"{b}_{d}.txt")
    for line in f:
        print(line, end="")
    f.close()

elif a == "lock":
    print("what do you want to lock: press 1 for Exercise, press 2 for Diet\n")
    c = int(input())

    if c == 1:
        print("How many exercise(s) you want to enter: ")
        ex = int(input())
        for item in range(0, ex):
            e = input(f"Exercise name {item+1}: ")
            with open(f"{b}_exercise.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + e + "\n")
        print("updated successfully")

    elif c == 2:
        print("How many food name(s) you want to enter: ")
        fo = int(input())
        fil = open(f"{b}_diet.txt", "a")
        for item in range(0, fo):
            food = input(f"Food name {item+1}: ")
            fil.write(str([str(getdate())])+ ": " + food + "\n")
        print("updated successfully")
        fil.close()
