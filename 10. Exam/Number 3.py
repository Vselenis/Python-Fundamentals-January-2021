random_words = input()
favorite_meals = {}
counter = 0
while random_words != "Stop":
    command, guest, meal = random_words.split("-")

    if command == "Like":
        if guest not in favorite_meals:
            favorite_meals[guest] = [meal]
        else:
            for key, value in favorite_meals.items():
                if meal not in value:
                    favorite_meals[guest] += [meal]

    if command == "Unlike":
        if guest not in favorite_meals:
            print(f"{guest} is not at the party.")

        else:
            for k, v in favorite_meals.items():
                if meal not in v:
                    print(f"{guest} doesn't have the {meal} in his/her collection.")
                else:
                    print(f"{guest} doesn't like the {meal}.")
                    favorite_meals[k].remove(meal)
                    counter += 1
    random_words = input()

new_dict = dict(sorted(favorite_meals.items(), key = lambda x: (-len(x[1]), x[0])))
for g, m in new_dict.items():
    print(f"{g}: {', '.join(m)}")


print(f"Unliked meals: {counter}")