"""
Første raden:
What a pleasure to
Andre raden:
right justify a haiku
Tredje raden:
as an exercise

@@@@@@@@@@@@@@@@@@@@@@@@@
@    What a pleasure to @
@ right justify a haiku @
@        as an exercise @
@@@@@@@@@@@@@@@@@@@@@@@@@
"""

row = ["", "", ""]

row[0] = input("Første raden:\n")
row[1] = input("Andre raden:\n")
row[2] = input("Tredje raden:\n")

len_of_longest_row = max(len(row[0]), len(row[1]), len(row[2]))

print()

print("@"*(len_of_longest_row + 4))

for i in row:
    len_of_row = len(i)

    print(f"@{(len_of_longest_row - len_of_row) * " "} {i} @")

print("@"*(len_of_longest_row + 4))
