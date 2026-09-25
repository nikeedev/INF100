file = open("input.txt", "r")

content = file.read()
file.close()
new = content.replace("   ", ",").split("\n");

loc_ids=[[],[]]

part1 = False
part2 = True


for i in range(len(new)-1):
    temp_str = new[i].split(",");
    
    for i in range(len(temp_str)):
        loc_ids[i].append(int(temp_str[i]))


    loc_ids[0].sort()
    loc_ids[1].sort()

if part1:
    sums = 0

    for i in range(len(loc_ids[0])):
        sums += abs(loc_ids[0][i] - loc_ids[1][i])

    print(f"Part 1: {sums}")

if part2:
    sums = 0

    for i in range(len(loc_ids[0])):
        sums += loc_ids[0][i] * loc_ids[1].count(loc_ids[0][i])

    print(f"Part 2: {sums}")


    

