from typing import Any, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFiniteMakeSetProduct(I.FiniteMakeSetProduct):

    def product(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetProduct[X, Any]:
        raise NotImplementedError()  # implement here
