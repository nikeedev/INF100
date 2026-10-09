from pathlib import Path

def filter_wordlist(path, search_string): 
    filtered_words = []
    
    words = Path(path).read_text(encoding='utf-8').split("\n")
     
    for word in words:
        if search_string in word:
            filtered_words.append(word)

    return filtered_words



def test_filter_wordlist():
    print('Tester filter_wordlist... ', end='')

    # Test 1
    expected = ['database', 'baser']
    actual = filter_wordlist('sample.txt', 'base')
    assert expected == actual
    
    # Test 2
    expected = [
      'småstad', 'småstaden', 'småstas', 'småstasen', 'småstat', 'småstaten',
      'småstatene', 'småstater',
    ]
    actual = filter_wordlist('nsf2025.txt', 'småsta')
    assert expected == actual

    # Test 3
    expected = [
      'stjerneskudd', 'stjerneskudda', 'stjerneskuddene', 'stjerneskuddet', 
    ]
    actual = filter_wordlist('nsf2025.txt', 'stjerneskudd')
    assert expected == actual
    
    print('OK')

if __name__ == "__main__":
    test_filter_wordlist()
