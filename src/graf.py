"""Graf, wierzchołek i krawędź"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Wierzcholek:
    identyfikator: int
    etykieta: str


@dataclass(frozen=True)
class Krawedz:
    poczatek: Wierzcholek
    koniec: Wierzcholek


@dataclass
class Graf:
    nazwa: str
    wierzcholki: list[Wierzcholek] = field(default_factory=list)
    krawedzie: list[Krawedz] = field(default_factory=list)

    def pobierzSasiadow(self, wierzcholek: Wierzcholek) -> list[Wierzcholek]:
        """Zwraca sąsiadów wierzchołka posortowanych rosnąco po identyfikatorze
        Krawędzie są nieskierowane, więc liczą się w obu kierunkach
        Zgłasza ValueError, jeśli wierzchołek nie należy do grafu
        """
        if wierzcholek not in self.wierzcholki:
            raise ValueError(f"Wierzchołek {wierzcholek.etykieta} nie należy do grafu „{self.nazwa}”.")

        sasiedzi: dict[int, Wierzcholek] = {}
        for krawedz in self.krawedzie:
            if krawedz.poczatek == wierzcholek:
                sasiedzi[krawedz.koniec.identyfikator] = krawedz.koniec
            elif krawedz.koniec == wierzcholek:
                sasiedzi[krawedz.poczatek.identyfikator] = krawedz.poczatek
        return [sasiedzi[i] for i in sorted(sasiedzi)]
