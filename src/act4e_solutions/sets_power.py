from typing import Any, overload, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolMakePowerSet(I.MakePowerSet):
    @overload
    def powerset(self, s: I.FiniteSet[X]) -> I.FiniteSetOfFiniteSubsets[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def powerset(self, s: I.Setoid[X]) -> I.SetOfFiniteSubsets[X, Any]:
        ... # this is just a type declaration - do not implement

    def powerset(self, s: I.Setoid[X]) -> I.SetOfFiniteSubsets[X, Any]:
        raise NotImplementedError() # implement here
