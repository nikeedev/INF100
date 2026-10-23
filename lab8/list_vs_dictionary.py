def key_value_getter(d):
    print("Dictionary keys:")
    for key in d.keys():
        print(key)
    
    print("\nDictionary values:")
    for key in d.values():
        print(key)
    
    print("\nDictionary keys/value:")
    for i in range(len(d.keys())):
        print(list(d.keys())[i], list(d.values())[i])

def index_value_getter(a):
    print("List indices:")
    for i in range(len(a)):
        print(i)

    print("\nList values:")
    for i in a:
        print(i)

    print("\nList indices/value:")
    for i in range(len(a)):
        print(i, a[i])

