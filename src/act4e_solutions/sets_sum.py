from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I


X = TypeVar("X")


class SolMakeSetDisjointUnion(I.MakeSetDisjointUnion):
    @overload
    def disjoint_union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetDisjointUnion[X, Any]:
        ...

    @overload
    def disjoint_union(self, components: Sequence[I.Setoid[X]]) -> I.SetDisjointUnion[X, Any]:
        ...

    def disjoint_union(self, components: Sequence[I.Setoid[X]]) -> I.SetDisjointUnion[X, Any]:
        raise NotImplementedError()
