from typing import Any, overload, TypeVar

import act4e_interfaces as I

C = TypeVar("C")
E = TypeVar("E")
X = TypeVar("X")


class SolFinitePosetConstructionTwisted(I.FinitePosetConstructionTwisted):
    @overload
    def twisted(self, s: I.FinitePoset[X]) -> I.FinitePosetOfIntervals[X, Any]:
        ...

    @overload
    def twisted(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        ...

    def twisted(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        raise NotImplementedError()


class SolFinitePosetConstructionArrow(I.FinitePosetConstructionArrow):
    @overload
    def arrow(self, s: I.FinitePoset[X]) -> I.FinitePosetOfIntervals[X, Any]:
        ...

    @overload
    def arrow(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        ...

    def arrow(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        raise NotImplementedError()
