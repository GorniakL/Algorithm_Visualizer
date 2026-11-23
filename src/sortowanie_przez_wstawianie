"""Sortowanie przez wstawianie z zapisem kroków"""

from dataclasses import dataclass

from algorytmy import AlgorytmSortowania
from krok import Krok, RodzajKroku


@dataclass
class SortowaniePrzezWstawianie(AlgorytmSortowania):
    nazwa: str = "Sortowanie przez wstawianie"
    opis: str = "Wstawia kolejne elementy na właściwe miejsce w uporządkowanej części listy."

    def wykonaj(self, dane: list[int]) -> list[Krok]:
        """Sortuje rosnąco i zwraca zapis porównań oraz wstawień"""
        sortowana_lista = dane.copy()
        kroki: list[Krok] = []

        for pozycja in range(1, len(sortowana_lista)):
            wartosc = sortowana_lista[pozycja]
            miejsce = pozycja

            #szukamy miejsca od prawej strony uporządkowanego fragmentu
            while miejsce > 0:
                lewy = miejsce - 1
                kroki.append(
                    Krok(RodzajKroku.POROWNANIE, [lewy, pozycja], sortowana_lista.copy())
                )
                if sortowana_lista[lewy] <= wartosc:
                    break
                miejsce -= 1

            if miejsce != pozycja:
                #elementy między pozycjami przesuwają się o jedno miejsce w prawo
                sortowana_lista.pop(pozycja)
                sortowana_lista.insert(miejsce, wartosc)
                kroki.append(
                    Krok(RodzajKroku.WSTAWIENIE, [pozycja, miejsce], sortowana_lista.copy())
                )

        return kroki