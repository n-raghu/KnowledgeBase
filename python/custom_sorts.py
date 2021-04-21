class Sort:

    def __init__(self, _list=None):
        self._list = _list

    def ascender(self, _alist=None):
        print('alist', _alist)
        print('slf', dir(self))
        if _alist:
            _workingset = _alist
        elif self._list:
            _workingset = self._list
        else:
            return "WorkingSet missing"

        _resultset = _workingset.copy()
        cycles = len(_resultset)
        for idx in range(cycles):
            for latter in range(idx, cycles):
                try:
                    if _resultset[idx] > _resultset[latter]:
                        _tmp = _resultset[idx]
                        _resultset[idx] = _resultset[latter]
                        _resultset[latter] = _tmp
                except IndexError:
                    break
        return _resultset

    def descender(self):
        _resultset = self._list.copy()
        cycles = len(_resultset)
        for idx in range(cycles):
            for latter in range(idx, cycles):
                try:
                    if _resultset[idx] < _resultset[latter]:
                        _tmp = _resultset[idx]
                        _resultset[idx] = _resultset[latter]
                        _resultset[latter] = _tmp
                except IndexError:
                    break
        return _resultset

    def all_sorts(self):
        return {
            'source': self._list,
            'ascending': self.ascender(),
            'descending': self.descender()
        }

    def get_source(self):
        return self._list



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
        [12, 5, 99, 1, 36],
        [12, 44, 66, 99, 33, 11, 55],
        [69, 11, 88, 14, 16, 369, 199, 99, 116, 188]
    ]
"""
    for _list in all_lists:
        print(_list)
        print(sequence_sort(_list))
        print('')
        print("------------------------------------")
        print('')
"""