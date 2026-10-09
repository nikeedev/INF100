from pathlib import Path

def alignment_difference(genome, sequence, i):
    difference = 0

    for j in range(len(sequence)):
        if genome[i+j] != sequence[j]:
            difference += 1

    return difference


def best_alignment(genome, sequence):
    best_i = 0 
    diff = alignment_difference(genome, sequence, 0)

    for i in range(1, len(genome) - len(sequence) + 1):
        new_diff = alignment_difference(genome, sequence, i) 
        if new_diff < diff:
            best_i = i
            diff = new_diff
         
    return best_i

def best_alignment_to_file(path, sequence):
    genome = Path(path).read_text(encoding='utf-8')

    return best_alignment(genome, sequence)

def test_aligment_difference():
    print('Testing alignment_difference...', end='')
    genome = 'AAACCC'
    sequence = 'ACC'
    assert 2 == alignment_difference(genome, sequence, 0)
    assert 1 == alignment_difference(genome, sequence, 1)
    assert 0 == alignment_difference(genome, sequence, 2)
    assert 1 == alignment_difference(genome, sequence, 3)
    print(' OK')   

def test_best_alignment():
    print('Testing best_alignment...', end='')
    genome = 'AAACACCCCCGGGGGTGTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    sequence = 'ACACCCCCGGGGATGT'
    assert 2 == best_alignment(genome, sequence)

    genome = 'AAAAAAAAAAAAAAAAACACCCCCGGGGGTGTTTTTTTTTTTTTT'
    sequence =                     'CCGGGGATGT'
    assert 22 == best_alignment(genome, sequence)

    genome = 'TTTAAG'
    sequence = 'AAGT'
    assert 2 == best_alignment(genome, sequence)
    print(' OK')

def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

if __name__ == "__main__":
    test_aligment_difference()
    test_best_alignment()
    test_best_alignment_to_file()


