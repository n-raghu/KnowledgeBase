from time import time
from math import ceil as mceil
from itertools import product, chain, combinations, permutations

from probs import guess_word_sets, special_chars, numbers


def powerset(
    keys: list,
    sp_chars: list,
    numbers: list,
) -> list:
    permuts: list = []
    tup_generator = chain.from_iterable(combinations(keys, r) for r in range(1, len(keys) + 1))
    master_list = append_chars_nums(tup_generator, sp_chars, numbers)

    for tup in master_list:
        if len(tup) == 1:
            permuts.append(tup)
            continue
        permuts.extend(permutations(tup))

    return permuts


def append_chars_nums(tuplist, spc, num) -> list:
    _power: list = []
    for tup in tuplist:
        for n in num:
            for _char in spc:
                _power.append(tup)
                _xtup = tup + (n, _char)
                _power.append(_xtup)
                _xtup = tup + (n, )
                _power.append(_xtup)
                _xtup = tup + (_char, )
                _power.append(_xtup)

    return _power


def case_handlers(masterset: list) -> list:
    all_combinations: list = []
    for tup in masterset:
        for e in tup:
            if isinstance(e, str):
                cmap = map(''.join, product(*zip(e.lower(), e.upper())))
                for c in cmap:
                    cstring =''
                    for idx in range(len(tup)):
                        cstring += c if e == tup[idx] else str(tup[idx])
                    all_combinations.append(cstring)

    return all_combinations


def file_writer(combinations):
    factor = 1_000_000
    unique_set = list(set(combinations))
    number_of_files = mceil(len(unique_set) / factor)
    file_suffix = 'pwd_'
    for file_num in range(number_of_files):
        with open(f'{file_suffix}{file_num}.TXT', 'w') as wfile:
            for pwd in unique_set[file_num * factor:(file_num + 1) * factor]:
                wfile.write(pwd)
                wfile.write('\n')


def sampler(purpose='general'):
    if purpose.lower() == 'general':
        return ['water', 'park', 'kit'], ['!', '@', '#',], [2014, 2015, 2016]
    elif purpose.lower() == 'cases':
        return [
            ('water', 2014, 'park'),
            ('water', '@')
        ]


if __name__ == '__main__':
    t1 = time()
    master_sets: list = []
    for guess_set in guess_word_sets:
        master_sets.extend(powerset(guess_set, special_chars, numbers))
    time_for_master_sets = time() - t1
    combinations = case_handlers(master_sets)
    time_for_combinations = time() - t1 - time_for_master_sets
    file_writer(combinations)
    time_for_file_writing = time() - t1 - time_for_master_sets - time_for_combinations
    print(f'{len(master_sets)} permutations identified in {round(time_for_master_sets, 1)}')
    print(f'{len(combinations)} combinations identified in {round(time_for_combinations, 1)}')
    print(f'Time take to write: {round(time_for_combinations, 1)}')
