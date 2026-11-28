"""Porównanie dwóch algorytmów sortowania."""

from __future__ import annotations
from dataclasses import dataclass

from algorytmy import AlgorytmSortowania
from dane import DaneSortowania
from wizualizacja import Wizualizacja


@dataclass
class PorownanieAlgorytmow:
    algorytm1: AlgorytmSortowania
    algorytm2: AlgorytmSortowania
    dane: DaneSortowania
    wizualizacja1: Wizualizacja | None = None
    wizualizacja2: Wizualizacja | None = None

    def uruchom(self) -> None:
        """Uruchamia oba sortowania i zapisuje ich wizualizacje."""
        if type(self.algorytm1) is type(self.algorytm2):
            raise ValueError("Wybierz dwa różne algorytmy sortowania.")
        if self.algorytm1.nazwa == self.algorytm2.nazwa:
            raise ValueError("Wybierz dwa algorytmy o różnych nazwach.")

        #kazdy algorytm pracuje na wlasnej kopii tego samego stanu poczatkowego
        stan = self.dane.elementy
        kroki1 = self.algorytm1.wykonaj(stan.copy())
        kroki2 = self.algorytm2.wykonaj(stan.copy())

        #zapisujemy oba wyniki po zakończeniu obu sortowań
        wizualizacja1 = Wizualizacja(kroki1, stan.copy())
        wizualizacja2 = Wizualizacja(kroki2, stan.copy())
        self.wizualizacja1 = wizualizacja1
        self.wizualizacja2 = wizualizacja2

    def policzOperacje(self) -> dict[str, int]:
        """Zwraca liczbę operacji pod nazwą każdego algorytmu."""
        if self.wizualizacja1 is None or self.wizualizacja2 is None:
            raise RuntimeError("Najpierw uruchom porównanie metodą uruchom().")

        return {
            self.algorytm1.nazwa: self.wizualizacja1.policzOperacje(),
            self.algorytm2.nazwa: self.wizualizacja2.policzOperacje(),
        }