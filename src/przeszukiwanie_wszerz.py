"""Przeszukiwanie wszerz z zapisem kolejności odwiedzin"""

from __future__ import annotations

#pozwala usuwac i dodawac elementy z obu koncow
from collections import deque
from dataclasses import dataclass

from algorytmy import AlgorytmGrafowy
from graf import Graf, Wierzcholek
from krok import Krok, RodzajKroku


#dataclass automatycznie tworzy konstruktor klasy, skraca kod
@dataclass
class PrzeszukiwanieWszerz(AlgorytmGrafowy):
    nazwa: str = "Przeszukiwanie wszerz"
    opis: str = "Odwiedza wierzchołki warstwami, zaczynając od podanego wierzchołka."

    def wykonaj(
        self, graf: Graf, start: Wierzcholek, cel: Wierzcholek | None = None
    ) -> list[Krok]:
        """Zwraca kroki odwiedzin od startu do celu lub do wyczerpania kolejki"""
        if start not in graf.wierzcholki:
            raise ValueError("Wierzchołek początkowy nie należy do grafu.")
        if cel is not None and cel not in graf.wierzcholki:
            raise ValueError("Wierzchołek docelowy nie należy do grafu.")
        
        kolejka = deque([start])
        odkryte = {start.identyfikator}
        kolejnosc: list[int] = []
        kroki: list[Krok] = []

        while kolejka:
            #z początku kolejki pobieramy wierzchołek, który czeka najdłużej
            aktualny = kolejka.popleft()
            numer = aktualny.identyfikator
            kolejnosc.append(numer)
            kroki.append(Krok(RodzajKroku.ODWIEDZENIE, [numer], kolejnosc.copy()))

            if aktualny == cel:
                break

            for sasiad in graf.znajdzSasiadow(aktualny):
                #oznaczamy sąsiada od razu, żeby trafił do kolejki tylko raz
                if sasiad.identyfikator not in odkryte:
                    odkryte.add(sasiad.identyfikator)
                    kolejka.append(sasiad)

        return kroki