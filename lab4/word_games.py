def can_be_made_of_letters(word, letters):
    trues = letters.count("*")
    letters = "".join(letters.split("*"))
   
    for i in word:
        if i in letters and (letters.count(i) >= word.count(i)):
            trues += word.count(i)

    if trues >= len(word):
        return True
    else:
        return False
    
def test_can_be_made_of_letters():
    print('Tester can_be_made_of_letters... ', end='')
    assert can_be_made_of_letters('emoji', 'abcdefghijklmno') is True
    assert can_be_made_of_letters('smilefjes', 'abcdefghijklmnopqrs') is False
    assert can_be_made_of_letters('smilefjes', 'abcdeeefhijlmnopsss') is True
    assert can_be_made_of_letters('lese', 'esel') is True
    print('OK')

# Ekstra tester for mer avansert variant, med wildcard * i bokstavene
def test_can_be_made_of_letters_wildcard():
    print('Tester can_be_made_of_letters_wildcard... ', end='')
    assert can_be_made_of_letters('lese', 'ese*') is True
    assert can_be_made_of_letters('lese', 'esxz*') is False
    assert can_be_made_of_letters('smilefjes', 's*i*e*j*s') is True
    assert can_be_made_of_letters('smilefjes', 's*i*e*j*z') is False
    print('OK')

##########################################################################

def possible_words(wordlist, letters):
    valid_words = []

    for word in wordlist:
        if can_be_made_of_letters(word, letters):
            valid_words.append(word)

    return valid_words
def test_possible_words():
    print('Tester possible_words... ', end='')
    hundsk =['tur', 'mat', 'kos', 'hent', 'sitt', 'dekk', 'voff']
    kattsk =['kos', 'mat', 'pus', 'mus', 'purr', 'mjau', 'hiss']
    assert(['kos', 'sitt'] == possible_words(hundsk, 'fikmopsttuv'))
    assert(['kos', 'pus', 'mus'] == possible_words(kattsk, 'fikmopsttuv'))
    print('OK')

# Ekstra tester for mer avansert variant, med wildcard * i bokstavene
"""
def test_possible_words_wildcard():
    print('Tester possible_words_wildcard... ', end='')
    hundsk =['tur', 'mat', 'kos', 'hent', 'sitt', 'dekk', 'voff']
    kattsk =['kos', 'mat', 'pus', 'mus', 'purr', 'mjau', 'hiss']
    assert ['tur', 'mat', 'kos', 'sitt'] == possible_words(hundsk, 'ikmopstu*')
    assert ['kos', 'mat', 'pus', 'mus'] == possible_words(kattsk, 'ikmopstu*')
    print('OK')
""" 

if __name__ == "__main__":
    test_can_be_made_of_letters()
    test_can_be_made_of_letters_wildcard()

    test_possible_words()
    # test_possible_words_wildcard()

