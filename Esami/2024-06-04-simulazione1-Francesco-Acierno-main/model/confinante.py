from dataclasses import dataclass

from model.paese import Paese


@dataclass
class Confine:
    _c1: Paese
    _c2: Paese

    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2

    def __hash__(self):
        return hash((self._c1.id, self._c2.id))

    def __str__(self):
        return f"Border: {self._c1} - {self._c2}"