with open('input/day_03.txt', 'r') as file_object:
    input_text = file_object.read()

#part 1
def houses(input_text):
    input_lines = input_text.splitlines()
    x,y = 0,0
    present = {(x, y): True}

    for line in input_lines:
        for santa in line:
            if santa == '>':
                x = x + 1
            elif santa == '<':
                x = x - 1
            elif santa == '^':
                y = y + 1
            elif santa == 'v':
                y = y - 1
            present[(x, y)] = True

    return len(present)

final_answer = houses(input_text)
print(f"Houses received at least one present: {final_answer}")


#part 2
def houses2(input_text):
    input_lines = input_text.splitlines()
    sx,sy = 0,0
    rx,ry = 0,0
    present = {(0, 0): True}

    for line in input_lines:
        for i in range(len(line)):
            if i%2 == 0:
                if line[i] == '>':
                    sx = sx + 1
                elif line[i] == '<':
                    sx = sx - 1
                elif line[i] == '^':
                    sy = sy + 1
                elif line[i] == 'v':
                    sy = sy - 1
                present[(sx, sy)] = True
            else:
                if line[i] == '>':
                    rx = rx + 1
                elif line[i] == '<':
                    rx = rx - 1
                elif line[i] == '^':
                    rx = ry + 1
                elif line[i] == 'v':
                    ry = ry - 1
                present[(sx, sy)] = True

    return len(present)

final_answer = houses2(input_text)
print(f"Houses received at least one present: {final_answer}")




