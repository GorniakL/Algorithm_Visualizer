"""Krok algorytmu i jego rodzaj"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RodzajKroku(Enum):
    """Rodzaj czynności wykonanej w kroku algorytmu"""

    POROWNANIE = "POROWNANIE"
    ZAMIANA = "ZAMIANA"
    WSTAWIENIE = "WSTAWIENIE"
    ODWIEDZENIE = "ODWIEDZENIE"


#dataclass automatycznie tworzy konstruktor klasy, skraca kod
#frozen=True blokuje przypisywanie nowych wartosci do atrybutow, nie blokuje modyfikacji zawartosci list
@dataclass(frozen=True)
class Krok:
    """Pojedynczy krok algorytmu. Po utworzeniu pola są zablokowane, ale zawartość list można zmieniać.
    rodzaj    -- rodzaj wykonanej czynności (na jego podstawie liczymy operacje),
    elementy  -- indeksy danych lub identyfikatory wierzchołków, których dotyczy krok (wizualizacja wyróżnia je graficznie),
    stan      -- stan danych po wykonaniu kroku
    """

    rodzaj: RodzajKroku
    elementy: list[int]
    stan: list[int]
