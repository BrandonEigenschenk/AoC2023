import re
import pandas as pd

def check_game(input: str) -> int:
    flag = True
    rounds = input.split(":")[-1].split(";")
    game_idx = input.split(":")[0].split(" ")[-1]

    for game in rounds:
        for round in game.split(","):
            biter = re.finditer("blue", round)
            index = [m.start(0) for m in biter]
            if len(index) > 0:
                index = index[0]
                bnum = int(round[:index:])
                if bnum > 14:
                    flag = False

            riter = re.finditer("red", round)
            index = [m.start(0) for m in riter]
            if len(index) > 0:
                index = index[0]
                rnum = int(round[:index:])
                if rnum > 12:
                    flag = False

            giter = re.finditer("green", round)
            index = [m.start(0) for m in giter]
            if len(index) > 0:
                index = index[0]
                gnum = int(round[:index:])
                if gnum > 13:
                    flag = False

    if flag == False:
        return 0

    return int(game_idx)

output = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines: 
        output += check_game(line)

print(output)