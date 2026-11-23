"""Sortowanie bąbelkowe z zapisem kroków."""

from dataclasses import dataclass

from algorytmy import AlgorytmSortowania
from krok import Krok, RodzajKroku


@dataclass
class SortowanieBabelkowe(AlgorytmSortowania):
    nazwa: str = "Sortowanie bąbelkowe"
    opis: str = "Porównuje sąsiednie elementy i zamienia je, gdy są w złej kolejności."

    def wykonaj(self, dane: list[int]) -> list[Krok]:
        """Sortuje rosnąco i zwraca zapis porównań oraz zamian"""
        sortowana_lista = dane.copy()
        kroki: list[Krok] = []

        #po każdym przebiegu największy element trafia na koniec badanego fragmentu
        for koniec in range(len(sortowana_lista) - 1, 0, -1):
            for lewy in range(koniec):
                prawy = lewy + 1
                #kopiujemy stan, aby późniejsze zamiany nie zmieniały zapisanych kroków
                kroki.append(
                    Krok(RodzajKroku.POROWNANIE, [lewy, prawy], sortowana_lista.copy())
                )

                if sortowana_lista[lewy] > sortowana_lista[prawy]:
                    sortowana_lista[lewy], sortowana_lista[prawy] = sortowana_lista[prawy], sortowana_lista[lewy]
                    kroki.append(
                        Krok(RodzajKroku.ZAMIANA, [lewy, prawy], sortowana_lista.copy())
                    )

        return kroki