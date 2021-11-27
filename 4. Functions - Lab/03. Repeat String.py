def repeat(string, num):
    mulyiply = ''
    for i in range(num):
        mulyiply += string
    return mulyiply
string = input()
num = int(input())
print(repeat(string, num),end = '')