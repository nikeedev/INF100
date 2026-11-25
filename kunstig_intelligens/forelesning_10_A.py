a = input()

for i in range(len(a)+1):
    left = a[0:i]
    right = a[i:len(a)]
    print(left+"-"+right)
    
