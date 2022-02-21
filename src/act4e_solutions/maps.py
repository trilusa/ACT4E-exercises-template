from typing import overload, TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class SolFiniteMapOperations(I.FiniteMapOperations):
    @overload
    def identity(self, s: I.FiniteSet[A]) -> I.FiniteMap[A, A]:
        ...

    @overload
    def identity(self, s: I.Setoid[A]) -> I.Mapping[A, A]:
        ...

    def identity(self, s: I.Setoid[A]) -> I.Mapping[A, A]:
        raise NotImplementedError()

    def compose(self, f: I.FiniteMap[A, B], g: I.FiniteMap[B, C]) -> I.FiniteMap[A, C]:
        raise NotImplementedError()

    def as_relation(self, f: I.FiniteMap[A, B]) -> I.FiniteRelation[A, B]:
        raise NotImplementedError()
