"""Stan początkowy i kroki algorytmu."""

from dataclasses import dataclass

from krok import Krok, RodzajKroku


@dataclass
class Wizualizacja:
    kroki: list[Krok]
    #stan poczatkowy to dane sprzed wykonania pierwszej operacji
    stanPoczatkowy: list[int]

    def policzOperacje(self) -> int:
        """Zwraca liczbę wszystkich zapisanych operacji."""
        return len(self.kroki)

    def policzOperacjeRodzaju(self, rodzaj: RodzajKroku) -> int:
        """Zwraca liczbę operacji wybranego rodzaju."""
        liczba = 0
        for krok in self.kroki:
            if krok.rodzaj == rodzaj:
                liczba += 1
        return liczba