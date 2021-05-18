from selection import SelectionSort as _ssort
from mergo import merge_sort
from quik import sort_quick, a, b

class Sort:

    def __init__(self, ilist):
        self._list = ilist

    def ascend(self, method):
        if method == 'selection':
            s = _ssort((self._list).copy())
        elif method == 'quick':
            s = sort_quick(self._list, 0, len(self._list)-1)
            return None
        return s.ascend()
    
    def dirst(self):
        return dir(self)
