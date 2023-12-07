import re

total = 0

with open("input.txt") as f:
    data = f.readlines()

    for lines in data:
        lines = (
            lines.replace("one", "one1one")
            .replace("two", "two2two")
            .replace("three", "three3three")
            .replace("four", "four4four")
            .replace("five", "five5five")
            .replace("six", "six6six")
            .replace("seven", "seven7seven")
            .replace("eight", "eight8eight")
            .replace("nine", "nine9nine")
        )
        temp = [char for char in lines if (char.isnumeric() == True)]
        temp = temp[0] + temp[-1]
        total += (int("".join(temp)))

print(total)