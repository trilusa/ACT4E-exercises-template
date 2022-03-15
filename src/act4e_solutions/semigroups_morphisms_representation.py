from typing import Any, TypeVar

import act4e_interfaces as I


class SolFiniteSemigroupMorphismRepresentation(I.FiniteSemigroupMorphismRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteSemigroupMorphism_desc) -> I.FiniteSemigroupMorphism[Any, Any]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteSemigroupMorphism[Any, Any]) -> I.FiniteSemigroupMorphism_desc:
        raise NotImplementedError()


class SolFiniteMonoidMorphismRepresentation(I.FiniteMonoidMorphismRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteMonoidMorphism_desc) -> I.FiniteMonoidMorphism[Any, Any]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteMonoidMorphism[Any, Any]) -> I.FiniteMonoidMorphism_desc:
        raise NotImplementedError()


class SolFiniteGroupMorphismRepresentation(I.FiniteGroupMorphismRepresentation):
    def load(self, h: I.IOHelper, s: I.FiniteGroupMorphism_desc) -> I.FiniteGroupMorphism[Any, Any]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, m: I.FiniteGroupMorphism[Any, Any]) -> I.FiniteGroupMorphism_desc:
        raise NotImplementedError()
