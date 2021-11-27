first_line = input().split()
second_line = input().split()
third_line = input().split()

if '1' == first_line[0] and '1' == first_line[1] and '1' == first_line[2] or '1' == second_line[0] and '1' == second_line[1] and '1' == second_line[2] or '1' == third_line[0] and '1' == third_line[1] and '1' == third_line[2] or '1' == first_line[0] and '1' == second_line[0] and '1' == third_line[0] or '1' == first_line[1] and '1' == second_line[1] and '1' == third_line[1] or '1' == first_line[2] and '1' == second_line[2] and '1' == third_line[2] or '1' == first_line[0] and '1' == second_line[1] and '1' == third_line[2] or '1' == first_line[2] and '1' == second_line[1] and '1' == third_line[0]:
    print('First player won')
elif '2' == first_line[0] and '2' == first_line[1] and '2' == first_line[2] or '2' == second_line[0] and '2' == second_line[1] and '2' == second_line[2] or '2' == third_line[0] and '2' == third_line[1] and '2' == third_line[2] or '2' == first_line[0] and '2' == second_line[0] and '2' == third_line[0] or '2' == first_line[1] and '2' == second_line[1] and '1' == third_line[1] or '2' == first_line[2] and '2' == second_line[2] and '2' == third_line[2] or '2' == first_line[0] and '2' == second_line[1] and '2' == third_line[2] or '2' == first_line[2] and '2' == second_line[1] and '2' == third_line[0]:
    print('Second player won')
else:
    print('Draw!')