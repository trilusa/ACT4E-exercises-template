from typing import Any, overload, TypeVar

import act4e_interfaces as I

C = TypeVar("C")
E = TypeVar("E")
X = TypeVar("X")


class SolFinitePosetConstructionTwisted(I.FinitePosetConstructionTwisted):
    @overload
    def twisted(self, s: I.FinitePoset[X]) -> I.FinitePosetOfIntervals[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def twisted(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        ... # this is just a type declaration - do not implement

    def twisted(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        raise NotImplementedError() # implement here


class SolFinitePosetConstructionArrow(I.FinitePosetConstructionArrow):
    @overload
    def arrow(self, s: I.FinitePoset[X]) -> I.FinitePosetOfIntervals[X, Any]:
        ... # this is just a type declaration - do not implement

    @overload
    def arrow(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        ... # this is just a type declaration - do not implement

    def arrow(self, s: I.Poset[X]) -> I.PosetOfIntervals[X, Any]:
        raise NotImplementedError() # implement here
