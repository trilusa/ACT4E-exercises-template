from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolMakeSetUnion(I.MakeSetUnion):
    @overload
    def union(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetUnion[X, Any]:
        ...

    @overload
    def union(self, components: Sequence[I.EnumerableSet[X]]) -> I.EnumerableSetUnion[X, Any]:
        ...

    def union(self, components: Sequence[I.EnumerableSet[X]]) -> I.EnumerableSetUnion[X, Any]:
        raise NotImplementedError()


class SolSetoidOperations(I.SetoidOperations):
    @classmethod
    def union_setoids(cls, a: I.Setoid[X], b: I.Setoid[X]) -> I.Setoid[X]:
        raise NotImplementedError()

    @classmethod
    def intersection_setoids(cls, a: I.Setoid[X], b: I.Setoid[X]) -> I.Setoid[X]:
        raise NotImplementedError()
