from typing import Any, overload, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolPosetConstructionPower(I.PosetConstructionPower):
    @overload
    def powerposet(self, s: I.FiniteSet[X]) -> I.FinitePosetOfFiniteSubsets[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def powerposet(self, s: I.Setoid[X]) -> I.PosetOfFiniteSubsets[X, Any]:
        ... # this is just a type declaration - do not implement

    def powerposet(self, s: I.Setoid[X]) -> I.PosetOfFiniteSubsets[X, Any]:
        raise NotImplementedError() # implement here
