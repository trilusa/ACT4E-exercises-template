from typing import TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class SolFiniteMapOperations(I.FiniteMapOperations):

    def identity(self, s: I.Setoid[A]) -> I.Mapping[A, A]:
        raise NotImplementedError()

    def compose(self, f: I.FiniteMap[A, B], g: I.FiniteMap[B, C]) -> I.FiniteMap[A, C]:
        raise NotImplementedError()
