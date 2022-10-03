# Basics, import, work with os module

def count_lines(file_inp):
    with open(file_inp, 'r') as f:
        return len(f.readlines())


def count_chars(file_inp):
    with open(file_inp, 'r') as f:
        num_ch = 0
        for line in f:
            num_ch += len(line) - line.count('\n')
    return num_ch


def test(file_inp):
    assert count_lines('test3') == 3
    assert count_chars('test3') == 15
    print('Lines in the file: ',count_lines(file_inp))
    print('Chars in the file: ', count_chars(file_inp))


if __name__ == '__main__':
    file_input = input('Please, input the path to file [for example file = test3]: ')
    test(file_input)
