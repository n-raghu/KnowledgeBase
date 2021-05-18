class SelectionSort:

    def __init__(self, _list):
        self._list = _list

    def _getmax(self, wkset):
        _m = wkset[0]
        for x in wkset:
            if x > _m:
                _m = x
        return _m

    def __ascender__(self, n):
        _size = len(self._list)
        iterations = _size - 1 if n == -1 else n
        for i in range(iterations):
            _mx = self._getmax(self._list[:(_size - i)])
            _idx = self._list.index(_mx)
            self._list[_idx] = self._list[(_size -1 -i)]
            self._list[(_size -1 -i)] = _mx
        return self._list

    def ascend(self):
        return self.__ascender__(-1)

    def largest(self, n):
        return self.__ascender__(n)[-n]


if __name__ == '__main__':
    from time import time
    from copy import deepcopy
    all_lists = [
        [12, 5, 99, 1, 36],
        [12, 44, 66, 99, 33, 11, 55],
        [69, 11, 88, 14, 16, 369, 199, 99, 116, 188]
    ]
    dcopy = deepcopy(all_lists)
    system_sorted = []
    algo_sorted = []
    t1 = time()
    for _list in all_lists:
        _list.sort()
        system_sorted.append(_list)
    t2 = time()
    for _list in all_lists:
        s = SelectionSort(_list)
        algo_sorted.append(s.ascend())
    t3 = time()

    print(f'System is {round((t3-t2) - (t2-t1), 16)} seconds faster than Algorithm')

    print(algo_sorted)
    print(system_sorted)
