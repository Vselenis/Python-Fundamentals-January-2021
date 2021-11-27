# n = int(input())
# plant_discover = {}
# for _ in range(n):
#     pl, rarity = input().split("<->")
#     if pl not in plant_discover:
#         plant_discover[pl] = [int(rarity)]
#     else:
#         plant_discover[pl] = [int(rarity)]
# command = input()
# while command != "Exhibition":
#     command = command.split(": ")
#     if command[0] == "Rate":
#         plant, rating = command[1].split(" - ")
#         rating = int(rating)
#         plant_discover[plant] += [rating]
#     # elif command[0] == "Update":
#     #     plants, new_rarity = command[1].split(" - ")
#     #     new_rarity = int(new_rarity)
#     #     plant_discover[plants] = new_rarity
#     # elif command[0] == "Reset":
#     #     remove_plants =
#


test_dict = {'is': [1, 2], 'gfg': [3], 'best': [1, 3, 4]}


print("The original dictionary is : " + str(test_dict))

# using sorted() + join() + lambda
# Sort dictionary by value list length
res = ' '.join(sorted(test_dict, key=lambda key: len(test_dict[key])))

# printing result
print("Sorted keys by value list : " + res)

