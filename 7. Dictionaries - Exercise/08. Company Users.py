command = input()
company_users = {}
while command != 'End':
    company,_, user = command.split()
    if company not in company_users:
        company_users[company] = []
    if user not in company_users[company]:
        company_users[company] += [user]

    command = input()
companies = dict(sorted(company_users.items(), key=lambda x: x[0]))
for companyName, idN in companies.items():
    print(f'{companyName}')
    for id in idN:
        print(f"-- {id}")
