from typing import Any, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFinitePosetConstructionPower(I.FinitePosetConstructionPower):
    def powerposet(self, s: I.FiniteSet[X]) -> I.FinitePosetOfFiniteSubsets[X, Any]:
        raise NotImplementedError()
