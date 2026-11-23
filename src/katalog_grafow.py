"""Katalog grafów dostępnych w aplikacji."""

from dataclasses import dataclass, field

from graf import Graf


#dataclass automatycznie tworzy konstruktor klasy, skraca kod
@dataclass
class KatalogGrafow:
    grafy: list[Graf] = field(default_factory=list)

    def listaGrafow(self) -> list[Graf]:
        #kopia pozwala zmienic kolejnosc wyniku bez przestawiania wpisow w katalogu
        return self.grafy.copy()

    def znajdz(self, nazwa: str) -> Graf:
        for graf in self.grafy:
            if graf.nazwa == nazwa:
                return graf
        raise ValueError(f"Nie znaleziono grafu o nazwie „{nazwa}”.")