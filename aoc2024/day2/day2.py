file = open("input.txt", "r")

content = file.read()
file.close()

part1 = True
part2 = False

if part1:
    safe_reports = 0
    
    new_text = content.split("\n")

    for i in range(len(new_text) - 1):
        nums = 0

        temp = new_text[i].split(" ")
        for j in range(len(temp) - 1):
            print(f"{int(temp[j])} - {int(temp[j+1])} = {abs(int(temp[j]) - int(temp[j+1]))}")
            if 0 < abs(int(temp[j]) - int(temp[j+1])) < 3:
                nums += 1

        print(nums)
        if nums == len(temp) - 1:
            safe_reports += 1
            nums = 0

    print(f"Part 1: {safe_reports}")

if part2:
    sums = 0

    prnt(f"Part 2: {sums}")


    
