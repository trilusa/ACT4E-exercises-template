from typing import Any, overload, TypeVar

import act4e_interfaces as I

C = TypeVar("C")
E = TypeVar("E")
X = TypeVar("X")


class SolFinitePosetConstructionTwisted(I.FinitePosetConstructionTwisted):
    def twisted(self, s: I.FinitePoset[X]) -> I.FinitePosetOfIntervals[X, Any]:
        raise NotImplementedError()


class SolFinitePosetConstructionArrow(I.FinitePosetConstructionArrow):
    def arrow(self, s: I.FinitePoset[X]) -> I.FinitePosetOfIntervals[X, Any]:
        raise NotImplementedError() # implement here
