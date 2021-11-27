string = input().split(' ')
find_the_word = input()

palindrome = [el for el in string if el == el[::-1]]
print(palindrome)

occ = palindrome.count(find_the_word)
print(f'Found palindrome {occ} times')