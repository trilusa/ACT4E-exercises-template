from typing import overload, TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class SolFiniteMapOperations(I.FiniteMapOperations):
    @overload
    def identity(self, s: I.FiniteSet[A]) -> I.FiniteMap[A, A]:
        ... # this is just a type declaration - do not implement

    @overload
    def identity(self, s: I.Setoid[A]) -> I.Mapping[A, A]:
        ... # this is just a type declaration - do not implement

    def identity(self, s: I.Setoid[A]) -> I.Mapping[A, A]:
        raise NotImplementedError() # implement here

    #

    def compose(self, f: I.FiniteMap[A, B], g: I.FiniteMap[B, C]) -> I.FiniteMap[A, C]:
        raise NotImplementedError()

    def as_relation(self, f: I.FiniteMap[A, B]) -> I.FiniteRelation[A, B]:
        raise NotImplementedError()
