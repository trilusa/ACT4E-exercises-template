from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I


X = TypeVar("X")


class SolMakeSetDisjointUnion(I.MakeSetDisjointUnion):
    @overload
    def disjoint_union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetDisjointUnion[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def disjoint_union(self, components: Sequence[I.Setoid[X]]) -> I.SetDisjointUnion[X, Any]:
        ... # this is just a type declaration - do not implement

    def disjoint_union(self, components: Sequence[I.Setoid[X]]) -> I.SetDisjointUnion[X, Any]:
        raise NotImplementedError() # implement here
