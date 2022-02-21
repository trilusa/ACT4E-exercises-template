from typing import Callable, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolEnumerableSetsOperations(I.EnumerableSetsOperations):
    def make_set_sequence(self, f: Callable[[int], X]) -> I.EnumerableSet[X]:
        raise NotImplementedError()

    def union_esets(self, a: I.EnumerableSet[X], b: I.EnumerableSet[X]) -> I.EnumerableSet[X]:
        """Creates the union of two EnumerableSet."""
        raise NotImplementedError()
