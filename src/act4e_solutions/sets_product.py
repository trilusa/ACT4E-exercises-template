from typing import Any, overload, Sequence, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolMakeSetProduct(I.MakeSetProduct):
    @overload
    def product(self, components: Sequence[I.FiniteSet[X]]) -> I.FiniteSetProduct[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def product(self, components: Sequence[I.Setoid[X]]) -> I.SetProduct[X, Any]:
        ... # this is just a type declaration - do not implement

    def product(self, components: Sequence[I.Setoid[X]]) -> I.SetProduct[X, Any]:
        raise NotImplementedError() # implement here
