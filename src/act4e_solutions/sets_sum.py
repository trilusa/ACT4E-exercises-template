from typing import Any, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFiniteMakeSetDisjointUnion(I.FiniteMakeSetDisjointUnion):
    def disjoint_union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetDisjointUnion[X, Any]:
        raise NotImplementedError()  # implement here
