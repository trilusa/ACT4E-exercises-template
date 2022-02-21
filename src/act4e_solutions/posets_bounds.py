from typing import Any, List, Optional, overload, TypeVar

import act4e_interfaces as I

E = TypeVar("E")
X = TypeVar("X")

__all__ = ["MyFinitePosetMeasurement"]


class MyFinitePosetMeasurement(I.FinitePosetMeasurement):
    def height(self, fp: I.FinitePoset[Any]) -> int:
        raise NotImplementedError()

    def width(self, fp: I.FinitePoset[Any]) -> int:
        raise NotImplementedError()


class MyFinitePosetConstructionOpposite(I.FinitePosetConstructionOpposite):
    @overload
    def opposite(self, p: I.FinitePoset[X]) -> I.FinitePoset[X]:
        ...

    @overload
    def opposite(self, p: I.Poset[X]) -> I.Poset[X]:
        ...

    def opposite(self, m: I.Poset[X]) -> I.Poset[X]:
        raise NotImplementedError()


class MyFinitePosetSubsetProperties(I.FinitePosetSubsetProperties):
    def is_chain(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()

    def is_antichain(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()


class MyFinitePosetSubsetProperties2(I.FinitePosetSubsetProperties2):

    def is_lower_set(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()

    def is_upper_set(self, fp: I.FinitePoset[X], s: List[X]) -> bool:
        raise NotImplementedError()


class MyFinitePosetClosures(I.FinitePosetClosures):
    def upper_closure(self, fp: I.FinitePoset[X], s: List[X]) -> List[X]:
        raise NotImplementedError()

    def lower_closure(self, fp: I.FinitePoset[X], s: List[X]) -> List[X]:
        raise NotImplementedError()


class MyFinitePosetInfSup(I.FinitePosetInfSup):
    def lower_bounds(self, fp: I.FinitePoset[E], s: List[E]) -> List[E]:
        raise NotImplementedError()

    def upper_bounds(self, fp: I.FinitePoset[E], s: List[E]) -> List[E]:
        raise NotImplementedError()

    def infimum(self, fp: I.FinitePoset[E], s: List[E]) -> Optional[E]:
        raise NotImplementedError()

    def supremum(self, fp: I.FinitePoset[E], s: List[E]) -> Optional[E]:
        raise NotImplementedError()


class MyFinitePosetMinMax(I.FinitePosetMinMax):
    def minimal(self, fp: I.FinitePoset[E], S: List[E]) -> List[E]:
        raise NotImplementedError()

    def maximal(self, fp: I.FinitePoset[E], S: List[E]) -> List[E]:
        raise NotImplementedError()
