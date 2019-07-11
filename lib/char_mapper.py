from constants.hex_codes import HEX_CODES


class CharMapper:
    def __init__(self):
        self._includes = HEX_CODES["includes"]
        self._excludes = HEX_CODES["excludes"]

    @property
    def includes(self):
        return self._includes

    @property
    def excludes(self):
        return self._excludes