"""Graf, wierzchołek i krawędź"""
from __future__ import annotations

from dataclasses import dataclass, field


# Dataclass automatycznie tworzy konstruktor klasy, skraca kod
# frozen=True blokuje przypisywanie nowych wartosci do atrybutow, nie blokuje modyfikacji zawartosci list
@dataclass(frozen=True)
class Wierzcholek:
    """Wierzchołek grafu"""
    identyfikator: int
    etykieta: str


@dataclass(frozen=True)
class Krawedz:
    """Krawędź grafu z wagą domyślną równą 1."""
    poczatek: Wierzcholek
    koniec: Wierzcholek
    waga: int = 1


@dataclass
class Graf:
    """Graf skierowany lub nieskierowany, z wierzchołkami i krawędziami"""
    nazwa: str
    wierzcholki: list[Wierzcholek] = field(default_factory=list) #automatycznie tworzy pusta liste
    krawedzie: list[Krawedz] = field(default_factory=list)
    skierowany: bool = False

    def znajdzSasiadow(self, wierzcholek: Wierzcholek) -> list[Wierzcholek]:
        """Zwraca sąsiadów wierzchołka posortowanych rosnąco po identyfikatorze
        W grafie skierowanym uwzględnia tylko krawędzie wychodzące.
        W grafie nieskierowanym uwzględnia oba kierunki.
        Zgłasza ValueError, jeśli wierzchołek nie należy do grafu
        """
        if wierzcholek not in self.wierzcholki:
            raise ValueError(f"Wierzchołek {wierzcholek.etykieta} nie należy do grafu „{self.nazwa}”.")

        sasiedzi: dict[int, Wierzcholek] = {}
        for krawedz in self.krawedzie:
            if krawedz.poczatek == wierzcholek:
                sasiedzi[krawedz.koniec.identyfikator] = krawedz.koniec
            elif not self.skierowany and krawedz.koniec == wierzcholek:
                sasiedzi[krawedz.poczatek.identyfikator] = krawedz.poczatek
        return [sasiedzi[i] for i in sorted(sasiedzi)]
