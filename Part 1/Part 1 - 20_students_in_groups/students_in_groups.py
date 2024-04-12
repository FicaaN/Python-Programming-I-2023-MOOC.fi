students = int(input("How many students on the course? "))
groups = int(input("Desired group size? "))

groups_formed = students // groups

if groups_formed * groups < students:
    print(f"Number of groups formed: {groups_formed + 1}")
else:
    print(f"Number of groups formed: {groups_formed}")