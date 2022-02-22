from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFinitePosetConstructionSum(I.FinitePosetConstructionSum):
    @overload
    def disjoint_union(self, ps: Sequence[I.FinitePoset[X]]) -> I.FinitePosetDisjointUnion[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def disjoint_union(self, ps: Sequence[I.Poset[X]]) -> I.PosetDisjointUnion[X, Any]:
        ... # this is just a type declaration - do not implement

    def disjoint_union(self, ps: Sequence[I.Poset[X]]) -> I.PosetDisjointUnion[X, Any]:
        raise NotImplementedError() # implement here
