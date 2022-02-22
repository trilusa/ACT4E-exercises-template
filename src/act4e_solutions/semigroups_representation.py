from typing import Any, TypeVar

import act4e_interfaces as I

X = TypeVar("X")


class SolFiniteSemigroupRepresentation(I.FiniteSemigroupRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteSemigroup_desc) -> I.FiniteSemigroup[Any]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteSemigroup[Any]) -> I.FiniteSemigroup_desc:
        raise NotImplementedError()


class SolFiniteMonoidRepresentation(I.FiniteMonoidRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteMonoid_desc) -> I.FiniteMonoid[X]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteMonoid[Any]) -> I.FiniteMonoid_desc:
        raise NotImplementedError()


class SolFiniteGroupRepresentation(I.FiniteGroupRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteGroup_desc) -> I.FiniteGroup[X]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteGroup[Any]) -> I.FiniteGroup_desc:
        raise NotImplementedError()
