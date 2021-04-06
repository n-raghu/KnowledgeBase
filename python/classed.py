class Water:
    def __init__(self, name, color, taste):
        self._name = name
        self._color = color
        self._taste = taste

    def _info(self):
        return {
            'name': self._name,
            'color': self._color,
            'taste': self._taste
        }


class Krishna(Water):
    def __init__(self, **kwargs):
        if 'area' in kwargs:
            _area = kwargs['area']
            del kwargs['area']
        else:
            _area = 'kmm'
        self._area = _area
        super().__init__(kwargs['name'], kwargs['color'], kwargs['taste'])

    def ginfo(self):
        return {
            'name': self._name,
            'area': self._area
        }

    def winfo(self):
        return self._info()
