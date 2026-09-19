def can_be_made_of_letters(word, letters):
    for i in word:
        if letters.count(i) < (word.count(i) + word.count("*")):
            return False
        
    return True
    
def test_can_be_made_of_letters():
    print('Tester can_be_made_of_letters... ', end='')
    assert can_be_made_of_letters('emoji', 'abcdefghijklmno') is True
    assert can_be_made_of_letters('smilefjes', 'abcdefghijklmnopqrs') is False
    assert can_be_made_of_letters('smilefjes', 'abcdeeefhijlmnopsss') is True
    assert can_be_made_of_letters('lese', 'esel') is True
    # print(can_be_made_of_letters('potato', 'pooota'))
    print('OK')

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

if __name__ == "__main__":
    test_can_be_made_of_letters()

    test_possible_words()

