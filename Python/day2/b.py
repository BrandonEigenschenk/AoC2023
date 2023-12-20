import re
import pandas as pd

def check_game(input: str) -> int:
    bmin = 1
    gmin = 1
    rmin = 1
    rounds = input.split(":")[-1].split(";")

    for game in rounds:
        for round in game.split(","):
            biter = re.finditer("blue", round)
            index = [m.start(0) for m in biter]
            if len(index) > 0:
                index = index[0]
                bnum = int(round[:index:])
                if bnum > bmin:
                    bmin = bnum


            riter = re.finditer("red", round)
            index = [m.start(0) for m in riter]
            if len(index) > 0:
                index = index[0]
                rnum = int(round[:index:])
                if rnum > rmin:
                    rmin = rnum


            giter = re.finditer("green", round)
            index = [m.start(0) for m in giter]
            if len(index) > 0:
                index = index[0]
                gnum = int(round[:index:])
                if gnum > gmin:
                    gmin = gnum

    return gmin*rmin*bmin

output = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines: 
        output += check_game(line)

print(output)