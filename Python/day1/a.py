total = 0

with open("input.txt") as f:
    data = f.readlines()

    for lines in data:
        temp = [char for char in lines if (char.isnumeric() == True)]
        temp = temp[0] + temp[-1]
        total += (int("".join(temp)))

print(total)