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


@dataclass(frozen=True)
class Krok:
    """Pojedynczy krok algorytmu. Po utworzeniu nie jest zmieniany
    rodzaj    -- rodzaj wykonanej czynności (na jego podstawie liczymy operacje),
    elementy  -- indeksy w danych lub identyfikatory wierzchołków, których dotyczy krok
                 (wizualizacja wyróżnia je graficznie),
    stan      -- stan danych po wykonaniu kroku
    """

    rodzaj: RodzajKroku
    elementy: list[int]
    stan: list[int]
