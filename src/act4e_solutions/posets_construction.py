from typing import Any, overload, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class MyPosetConstructionPower(I.PosetConstructionPower):
    @overload
    def powerposet(self, s: I.FiniteSet[X]) -> I.FinitePosetOfFiniteSubsets[X, Any]:
        ...

    @overload
    def powerposet(self, s: I.Setoid[X]) -> I.PosetOfFiniteSubsets[X, Any]:
        ...

    def powerposet(self, s: I.Setoid[X]) -> I.PosetOfFiniteSubsets[X, Any]:
        raise NotImplementedError()
