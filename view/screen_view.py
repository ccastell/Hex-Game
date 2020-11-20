

class ScreenView:
    
    _screen = None

    def __init__(self, screen, size):
        self._screen = screen   
        self._width, self._height = size

    def update(self):
        raise NotImplementedError