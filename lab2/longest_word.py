word1 = input("Skriv et ord:\n")
word2 = input("Skriv et annet ord:\n")
word3 = input("Skriv et siste ord:\n")


len_word1 = len(word1)
len_word2 = len(word2)
len_word3 = len(word3)

biggest_len = max(len_word1, len_word2, len_word3)

print()

if len_word1 == biggest_len:
    print(word1)
elif len_word2 == biggest_len:
    print(word2)
elif len_word3 == biggest_len:
    print(word3)
