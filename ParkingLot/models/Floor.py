class Floor:
    def __init__(self, floor_num: int):
        self._floor_num = floor_num
        self._slots = []

    @property
    def floor_num(self):
        return self._floor_num

    @property
    def slots(self):
        return self._slots
