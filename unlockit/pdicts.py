import sys
from itertools import product, permutations


def default_keys():
    return [
        2014,
        2015,
        2016,
        'goa',
        'trip',
        '@', '!', '#', '$', '&', '*', '_'
    ]


def gen_key_combinations(keys: list) -> list:
    sp_list: list = []
    num_list: list = []
    all_combination_lists: list = []

    for k in keys:
        if isinstance(k, int):
            num_list.append(str(k))
        elif isinstance(k, str) and len(k) == 1:
            sp_list.append(k)
        else:
            kmap = map(''.join, product(*zip(k.upper(), k.lower())))
            all_combination_lists.append(list(kmap))

    all_combination_lists.append(num_list)
    all_combination_lists.append(sp_list)

    return all_combination_lists


def gen_pwd_combinations(combs):
    pwd: list = []
    all_key_combinations = list(product(*combs))
    for combination in all_key_combinations:
        clist = permutations(combination)
        for tup in clist:
            pwd.append(
                ''.join(tup)
            )

    return pwd


def sampler():
    list_1 = ['ab', 'Ab', 'AB', 'aB']
    list_2 = ['xy', 'Xy', 'XY', 'xY']
    list_3 = [1, 2, 3,]
    all_lists = [list_1, list_2, list_3]
    return list(product(*all_lists))


if __name__ == '__main__':
    keys = default_keys()
    all_keys = gen_key_combinations(keys)
    all_pwd = gen_pwd_combinations(all_keys)
    with open('dict_pwd.txt', 'w') as dfile:
        for pwd in all_pwd:
            dfile.write(pwd)
            dfile.write('\n')
