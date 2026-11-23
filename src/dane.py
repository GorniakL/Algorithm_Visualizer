"""Dane wejściowe dla algorytmu sortowania"""
from __future__ import annotations

import random
from dataclasses import dataclass, field


#dataclass automatycznie tworzy konstruktor klasy, skraca kod
@dataclass
class DaneSortowania:
    #limity do ustalenia
    MIN_ELEMENTOW = 2
    MAKS_ELEMENTOW = 50
    MIN_WARTOSC = 1
    MAKS_WARTOSC = 100

    elementy: list[int] = field(default_factory=list) #automatycznie tworzy pusta liste

    #metoda statyczna nie wymaga utworzenia obiektu klasy
    @staticmethod
    def zTekstu(tekst: str) -> DaneSortowania:
        """Tworzy dane z tekstu, w którym liczby oddzielono przecinkami lub spacjami
        Zgłasza ValueError, jeśli któryś fragment nie jest liczbą całkowitą
        """
        fragmenty = tekst.replace(",", " ").split()
        elementy = []
        for fragment in fragmenty:
            try:
                elementy.append(int(fragment))
            except ValueError:
                raise ValueError(f"„{fragment}” nie jest liczbą całkowitą.") from None
        return DaneSortowania(elementy)

    @staticmethod
    def wygenerujLosowe(
        liczba: int, minWartosc: int = MIN_WARTOSC, maxWartosc: int = MAKS_WARTOSC
    ) -> DaneSortowania:
        """Losuje liczby całkowite z podanego przedziału, łącznie z jego granicami.
        Zgłasza ValueError dla błędnej liczby elementów lub granic przedziału.
        """
        if not DaneSortowania.MIN_ELEMENTOW <= liczba <= DaneSortowania.MAKS_ELEMENTOW:
            raise ValueError(
                f"Liczba elementów musi mieścić się w zakresie "
                f"{DaneSortowania.MIN_ELEMENTOW}–{DaneSortowania.MAKS_ELEMENTOW}."
            )
        if not DaneSortowania.MIN_WARTOSC <= minWartosc <= maxWartosc <= DaneSortowania.MAKS_WARTOSC:
            raise ValueError(
                f"Podaj granice od {DaneSortowania.MIN_WARTOSC} do {DaneSortowania.MAKS_WARTOSC}. "
                "Dolna granica nie może być większa od górnej."
            )
        return DaneSortowania(
            [random.randint(minWartosc, maxWartosc) for _ in range(liczba)]
        )

    def waliduj(self) -> list[str]:
        """Zwraca listę komunikatów o błędach
        Pusta lista oznacza poprawne dane
        """
        bledy = []
        if len(self.elementy) < self.MIN_ELEMENTOW:
            bledy.append(f"Podaj co najmniej {self.MIN_ELEMENTOW} liczby.")
        if len(self.elementy) > self.MAKS_ELEMENTOW:
            bledy.append(f"Podaj najwyżej {self.MAKS_ELEMENTOW} liczb.")
        if any(not self.MIN_WARTOSC <= x <= self.MAKS_WARTOSC for x in self.elementy):
            bledy.append(f"Liczby muszą mieścić się w zakresie {self.MIN_WARTOSC}–{self.MAKS_WARTOSC}.")
        return bledy
