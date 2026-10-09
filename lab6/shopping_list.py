from pathlib import Path


def shopping_list_to_dict(shopping_list):
    new_dict = {}

    for item in shopping_list.split("\n"):
        if not item.strip() == "":
            info = item.split(" ")
            new_dict[info[1]] = int(info[0])
    
    #print(f"\n{new_dict}")
    return new_dict

def shopping_list_file_to_dict(path):
    shopping_list = Path(path).read_text(encoding='utf-8')
    
    return shopping_list_to_dict(shopping_list)


def test_shopping_list_to_dict():
    print('Tester shopping_list_to_dict... ', end='')
    arg = '2 brød\n3 pizza\n10 poteter\n1 kaffe\n1 ost\n14 epler\n'
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 14,
    }
    actual = shopping_list_to_dict(arg)
    assert expected == actual
    print('OK')

def test_shopping_list_file_to_dict():
    print('Tester shopping_list_file_to_dict... ', end='')
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 13,
    }
    actual = shopping_list_file_to_dict('handleliste.txt')
    assert expected == actual
    print('OK')

if __name__ == '__main__':
    test_shopping_list_to_dict()
    test_shopping_list_file_to_dict()
