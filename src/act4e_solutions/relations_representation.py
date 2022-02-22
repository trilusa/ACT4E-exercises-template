from typing import TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")


class SolFiniteRelationRepresentation(I.FiniteRelationRepresentation):
    def load(self, h: I.IOHelper, data: I.FiniteRelation_desc) -> I.FiniteRelation[A, B]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, f: I.FiniteRelation[A, B]) -> I.FiniteRelation_desc:
        raise NotImplementedError()
