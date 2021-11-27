def solve(a, b, todo):
    result = None
    if todo == 'multiply':
        result = a * b
    elif todo == 'divide':
        result = a / b
    elif todo == 'add':
        result = a + b
    elif todo == 'subtract':
        result = a - b
    return result


todo = input()
a = float(input())
b = float(input())
print(f'{(solve(a, b, todo)):.0f}')
