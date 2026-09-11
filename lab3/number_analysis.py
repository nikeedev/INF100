from pathlib import Path
import json

input_file = 'numbers.json'
file_content = Path(input_file).read_text(encoding='utf-8')
numbers = json.loads(file_content)

total = 1
for num in numbers:

    # Delelig på tre
    if num % 3 == 0:
        kind = 'deles'
    else:
        kind = 'ikke deles'

    total *= num
    
    print(f'Tittei! {num} kan {kind} på 3')

print(f'Produktet av tallene {numbers} er {total}')
