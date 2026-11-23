"""Klasy bazowe algorytmów"""

from __future__ import annotations

#tworzenie abstrakcyjnych klas
from abc import ABC, abstractmethod
from dataclasses import dataclass

from graf import Graf, Wierzcholek
from krok import Krok


@dataclass
class Algorytm(ABC):
    """Przechowuje nazwę i opis algorytmu"""

    nazwa: str
    opis: str


class AlgorytmSortowania(Algorytm):
    """Klasa bazowa dla algorytmów sortowania"""

    #metoda abstrakcyjna – klasa potomna musi ją zaimplementować
    @abstractmethod
    def wykonaj(self, dane: list[int]) -> list[Krok]:
        """Zwraca kolejne kroki sortowania."""
        #zostanie zaimplementowana w konkretnej klasie algorytmu.
        raise NotImplementedError


class AlgorytmGrafowy(Algorytm):
    """Klasa bazowa dla algorytmów grafowych"""

    @abstractmethod
    def wykonaj(
        self, graf: Graf, start: Wierzcholek, cel: Wierzcholek | None = None
    ) -> list[Krok]:
        """Zwraca kolejne kroki algorytmu grafowego"""
        #zostanie zaimplementowana w konkretnej klasie algorytmu.
        raise NotImplementedError