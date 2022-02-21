from typing import Any, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFinitePosetConstructionProduct(I.FinitePosetConstructionProduct):
    def product(self, ps: Sequence[I.FinitePoset[X]]) -> I.FinitePosetProduct[X, Any]:
        raise NotImplementedError()
