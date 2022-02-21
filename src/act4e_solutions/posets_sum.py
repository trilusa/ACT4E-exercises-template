from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFinitePosetConstructionSum(I.FinitePosetConstructionSum):
    @overload
    def disjoint_union(self, ps: Sequence[I.FinitePoset[X]]) -> I.FinitePosetDisjointUnion[X, Any]:
        ...

    @overload
    def disjoint_union(self, ps: Sequence[I.Poset[X]]) -> I.PosetDisjointUnion[X, Any]:
        ...

    def disjoint_union(self, ps: Sequence[I.Poset[X]]) -> I.PosetDisjointUnion[X, Any]:
        raise NotImplementedError()
