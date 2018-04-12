
class Location:
    def __init__(self,pick_up, drop_off):
        self._pick_up = pick_up
        self._drop_off = drop_off
    def get_pick_up(self):
        return self._pick_up
    def get_drop_off(self):
        return self._drop_off

