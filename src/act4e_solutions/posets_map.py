from typing import TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")
X = TypeVar("X")


class SolFiniteMonotoneMapProperties(I.FiniteMonotoneMapProperties):
    def is_monotone(self, p1: I.FinitePoset[A], p2: I.FinitePoset[B], m: I.FiniteMap[A, B]) -> bool:
        raise NotImplementedError()

    def is_antitone(self, p1: I.FinitePoset[A], p2: I.FinitePoset[B], m: I.FiniteMap[A, B]) -> bool:
        raise NotImplementedError()
