def sequence_sort(list1: list) -> list:
    cycles = len(list1)
    for idx in range(cycles):
        for _ in range(idx, cycles):
            try:
                if list1[idx] > list1[_]:
                    _tmp = list1[idx]
                    list1[idx] = list1[_]
                    list1[_] = _tmp
            except IndexError:
                break
    return list1


if __name__ == '__main__':
    all_lists = [
        [12, 75, 99, 1, 36],
        [12, 44, 66, 99, 33, 11, 55],
    ]
    for _list in all_lists:
        print(_list)
        print(sequence_sort(_list))
        print('')
        print("------------------------------------")
        print('')
