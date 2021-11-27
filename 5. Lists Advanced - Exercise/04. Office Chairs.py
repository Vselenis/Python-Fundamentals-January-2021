n = int(input())
total_free_chairs = 0
enough_chairs = True
for i in range(1, n + 1):
    chairs = input().split(' ')
    chairs_n = len(chairs[0])
    num_of_people = int(chairs[1])
    if chairs_n >= num_of_people:
        total_free_chairs += chairs_n - num_of_people

    else:
        enough_chairs = False
        print(f"{num_of_people - chairs_n} more chairs needed in room {i}")


if enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")