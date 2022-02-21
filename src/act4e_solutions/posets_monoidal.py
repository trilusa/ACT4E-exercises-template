from typing import TypeVar

import act4e_interfaces as I

A = TypeVar("A")
B = TypeVar("B")
X = TypeVar("X")


class SolMonoidalPosetOperations(I.MonoidalPosetOperations):
    def is_monoidal_poset(self, fp: I.FinitePoset[X], fm: I.FiniteMonoid[X]) -> bool:
        raise NotImplementedError()
