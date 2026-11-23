"""Katalog algorytmów dostępnych w aplikacji."""

from dataclasses import dataclass, field

from algorytmy import Algorytm


#dataclass automatycznie tworzy konstruktor klasy, skraca kod
@dataclass
class KatalogAlgorytmow:
    algorytmy: list[Algorytm] = field(default_factory=list)

    def listaAlgorytmow(self) -> list[Algorytm]:
        #kopia pozwala zmienić kolejnosc wyniku bez przestawiania wpisow w katalogu
        return self.algorytmy.copy()

    def znajdz(self, nazwa: str) -> Algorytm:
        for algorytm in self.algorytmy:
            if algorytm.nazwa == nazwa:
                return algorytm
        raise ValueError(f"Nie znaleziono algorytmu o nazwie „{nazwa}”.")