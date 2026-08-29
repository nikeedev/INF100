people = int(input("Hvor mange er dere på laget?\n"))
twist = int(input("Hvor mange twist er det i posen dere vant?\n"))

rest = twist % people

print(f"Det blir {(twist - rest)//people} twist til hver, og det blir {rest} twist til overs.")
