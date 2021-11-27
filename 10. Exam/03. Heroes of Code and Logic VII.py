n = int(input())
hero_health = {}
hero_mana = {}

for _ in range(n):
    hero_name, health, mana = input().split()
    hero_health[hero_name] = int(health)
    hero_mana[hero_name] = int(mana)

command = input()
while command != "End":
    command = command.split(" - ")
    hero = command[1]
    if command[0] == "CastSpell":
        mana_needed = int(command[2])
        spell_name = command[3]
        if hero_mana[hero] >= mana_needed:
            hero_mana[hero] -= mana_needed
            print(f"{hero} has successfully cast {spell_name} and now has {hero_mana[hero]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        hero_health[hero] -= damage
        if hero_health[hero] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {hero_health[hero]} HP left!")
        else:
            del hero_health[hero]
            del hero_mana[hero]
            print(f"{hero} has been killed by {attacker}!")


    elif command[0] == "Recharge":
        amount = int(command[2])
        before_mana = hero_mana[hero]
        hero_mana[hero] += amount
        if hero_mana[hero] > 200:
            hero_mana[hero] = 200
        print(f"{hero} recharged for {hero_mana[hero] - before_mana} MP!")

    elif command[0] == "Heal":
        amount = int(command[2])
        before_healing = hero_health[hero]
        hero_health[hero] += amount
        if hero_health[hero] > 100:
            hero_health[hero] = 100
        print(f"{hero} healed for {hero_health[hero] - before_healing} HP!")

    command = input()

for x, y in hero_health.items():
    hero_health[x] = (y, hero_mana[x])
print(hero_health)
hero_health = dict(sorted(hero_health.items(), key=lambda x: (-x[1][0], -x[1][1])))

for key, value in hero_health.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")