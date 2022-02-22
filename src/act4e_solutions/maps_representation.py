from typing import Any, TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteMapRepresentation(I.FiniteMapRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteMap_desc) -> I.FiniteMap[A, B]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteMap[Any, Any]) -> I.FiniteMap_desc:
        raise NotImplementedError()
