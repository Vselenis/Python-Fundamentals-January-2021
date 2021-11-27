import sys
def min_size(min):
    min = sys.maxsize
    for n in range(3):
        i = int(input())
        if i < min:
            min = i
    return min
print(min_size(min))