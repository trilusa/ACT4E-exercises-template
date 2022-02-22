from typing import Any

import act4e_interfaces as I


class SolFinitePosetRepresentation(I.FinitePosetRepresentation):
    def load(self, h: I.IOHelper, s: I.FinitePoset_desc) -> I.FinitePoset[Any]:
        raise NotImplementedError()

    def save(self, h: I.IOHelper, p: I.FinitePoset[Any]) -> I.FinitePoset_desc:
        raise NotImplementedError()
