with open('input/day_06.txt', 'r') as file_object:
    input_text = file_object.read()

import pandas as pd
grid = pd.DataFrame(0, index=range(1000), columns=range(1000))

def turn_on(df, x1, y1, x2, y2):
    df.loc[x1:x2, y1:y2] = 1

def turn_off(df, x1, y1, x2, y2):
    df.loc[x1:x2, y1:y2] = 0

def toggle(df, x1, y1, x2, y2):
    df.loc[x1:x2, y1:y2] = 1 - df.loc[x1:x2, y1:y2]

for instruction in input_text.splitlines():
    word = instruction.split()
    if word[0] == 'toggle':
        start = word[1].split(',')
        end = word[3].split(',')
        # usage of int() from deepseek
        # prompt:How to convert the coordinate format here?
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(end[0])
        y2 = int(end[1])
        toggle(grid, x1, y1, x2, y2)
    else:
        action = word[1]
        start = word[2].split(',')
        end = word[4].split(',')
        x1 = int(start[0])
        y1 = int(start[1])
        x2 = int(end[0])
        y2 = int(end[1])
        if action == 'on':
            turn_on(grid, x1, y1, x2, y2)
        elif action == 'off':
            turn_off(grid, x1, y1, x2, y2)

lights = grid.sum().sum()
print(f'The number of lit lights is: {lights}')