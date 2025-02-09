with open('input/day_01.txt', 'r') as file_object:
    input_text = file_object.read()


#part 1
def answer(input_text):
    floor = 0
    for i in input_text:
        if i == '(':
            floor = floor + 1
        elif i == ')':
            floor = floor - 1
    return floor

final_answer = answer(input_text)
print(f"Final floor: {final_answer}")



#part 2
def basement(input_text):
    floor = 0
    position = 1
    for i in input_text:
        if i == '(':
            floor = floor + 1
        elif i == ')':
            floor = floor - 1
        if floor == -1:
            return position
        position = position + 1

bp = basement(input_text)
print(f"First position: {bp}")