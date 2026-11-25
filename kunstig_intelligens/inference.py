import random
import json
from pathlib import Path

WORD_LENGTH = 12

def main():
    weights = json.loads(Path('weights_no.json').read_text(encoding="utf-8"))

    answer = infer(WORD_LENGTH, weights)
    print(answer)

def infer(word_length, weigths):
    res = ""

    for _ in range(word_length):
        next_letter = get_token_ai(res, weigths)
        res += next_letter

    return res

def get_token_ai(context, weights):
    
    relevant_context = context[-2:]
    vector = weights[relevant_context] # {  "a": 6, "b": 3, "c": 1 }
    
    letters = list(vector.keys())
    relative_prob = list(vector.values())

    random_letter = random.choices(letters, weights=relative_prob, k=1)[0]
    
    return random_letter

def get_token_deterministic(context):
    if context == "":
        return "a"
    
    last_letter = context[-1]
    next_letter = chr(ord(last_letter) + 1)

    return next_letter

def get_token_dumb():
    letters = "abcdefghijklmnopqrstuvwxyzæøå"
    return random.choice(letters)
    
if __name__ == "__main__":
    main()
