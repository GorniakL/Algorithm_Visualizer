# Diagram klas UML (Unified Modeling Language)

Diagram klas przedstawia klasy systemu, ich atrybuty, metody oraz relacje między nimi. Klasy wynikają z pojęć zdefiniowanych w [słowniku domenowym](glossary.md), a metody z [przypadków użycia](use_cases/README.md).

```plantuml
@startuml

abstract class Algorytm {
    +nazwa : str
    +opis : str
}

abstract class AlgorytmSortowania {
    +{abstract} wykonaj(dane : list<int>) : list<Krok>
}

abstract class AlgorytmGrafowy {
    +{abstract} wykonaj(graf : Graf, start : Wierzcholek, cel : Wierzcholek | None = None) : list<Krok>
}

class SortowanieBabelkowe {
    +wykonaj(dane : list<int>) : list<Krok>
}
class SortowaniePrzezWstawianie {
    +wykonaj(dane : list<int>) : list<Krok>
}
class PrzeszukiwanieWszerz {
    +wykonaj(graf : Graf, start : Wierzcholek, cel : Wierzcholek | None = None) : list<Krok>
}

enum RodzajKroku {
    POROWNANIE
    ZAMIANA
    WSTAWIENIE
    ODWIEDZENIE
}

class Krok {
    +rodzaj : RodzajKroku
    +elementy : list<int>
    +stan : list<int>
}

class Wierzcholek {
    +identyfikator : int
    +etykieta : str
}

class Krawedz {
    +poczatek : Wierzcholek
    +koniec : Wierzcholek
    +waga : int = 1
}

class Graf {
    +nazwa : str
    +wierzcholki : list<Wierzcholek>
    +krawedzie : list<Krawedz>
    +skierowany : bool = False
    +znajdzSasiadow(wierzcholek : Wierzcholek) : list<Wierzcholek>
}

class DaneSortowania {
    +{static} MIN_ELEMENTOW : int = 2 {readOnly}
    +{static} MAKS_ELEMENTOW : int = 50 {readOnly}
    +{static} MIN_WARTOSC : int = 1 {readOnly}
    +{static} MAKS_WARTOSC : int = 100 {readOnly}
    +elementy : list<int>
    +{static} zTekstu(tekst : str) : DaneSortowania
    +{static} wygenerujLosowe(liczba : int, minWartosc : int = 1, maxWartosc : int = 100) : DaneSortowania
    +waliduj() : list<str>
}

class Wizualizacja {
    +kroki : list<Krok>
    +stanPoczatkowy : list<int>
    +policzOperacje() : int
    +policzOperacjeRodzaju(rodzaj : RodzajKroku) : int
}

class PorownanieAlgorytmow {
    +algorytm1 : AlgorytmSortowania
    +algorytm2 : AlgorytmSortowania
    +wizualizacja1 : Wizualizacja | None = None
    +wizualizacja2 : Wizualizacja | None = None
    +dane : DaneSortowania
    +uruchom()
    +policzOperacje() : dict<str, int>
}

class KatalogAlgorytmow {
    +algorytmy : list<Algorytm>
    +listaAlgorytmow() : list<Algorytm>
    +znajdz(nazwa : str) : Algorytm
}

class KatalogGrafow {
    +grafy : list<Graf>
    +listaGrafow() : list<Graf>
    +znajdz(nazwa : str) : Graf
}

Algorytm <|-- AlgorytmSortowania
Algorytm <|-- AlgorytmGrafowy
AlgorytmSortowania <|-- SortowanieBabelkowe
AlgorytmSortowania <|-- SortowaniePrzezWstawianie
AlgorytmGrafowy <|-- PrzeszukiwanieWszerz

AlgorytmSortowania ..> Krok : tworzy
AlgorytmGrafowy ..> Krok : tworzy
Krok "*" --> "1" RodzajKroku

Graf "*" o-- "0..*" Wierzcholek
Graf "*" o-- "0..*" Krawedz
Krawedz "*" --> "1" Wierzcholek : poczatek
Krawedz "*" --> "1" Wierzcholek : koniec

Wizualizacja "1" o-- "0..*" Krok
PorownanieAlgorytmow "0..1" *-- "0..2" Wizualizacja
PorownanieAlgorytmow "*" --> "2" AlgorytmSortowania
PorownanieAlgorytmow "*" --> "1" DaneSortowania

KatalogAlgorytmow "1" o-- "1..*" Algorytm
KatalogGrafow "1" o-- "1..*" Graf

@enduml
```

Python zapisuje stan początkowy i kroki algorytmu oraz zlicza operacje. JavaScript będzie odtwarzał animację, obsługiwał pauzę, tempo i wybór kroku. Aby pokazać licznik przy wybranym kroku, interfejs może zliczyć kroki od początku do tego miejsca.

Porównanie korzysta z dwóch różnych algorytmów sortowania i jednego zestawu danych. Przed uruchomieniem obie wizualizacje mogą być puste (`None`). Po zakończeniu `uruchom()` każdy algorytm ma własną wizualizację, a `policzOperacje()` zwraca liczbę operacji dla każdego z nich.

## Skąd wynikają klasy

| Klasa | Pojęcie ze słownika | Przypadki użycia |
|---|---|---|
| Algorytm, AlgorytmSortowania, AlgorytmGrafowy | Algorytm, Algorytm sortowania, Algorytm grafowy | UC-01, UC-02, UC-04 |
| SortowanieBabelkowe, SortowaniePrzezWstawianie, PrzeszukiwanieWszerz | Sortowanie bąbelkowe, Sortowanie przez wstawianie, Przeszukiwanie wszerz | UC-01, UC-02, UC-04 |
| Krok, RodzajKroku | Krok algorytmu, Liczba operacji | UC-01, UC-02, UC-03 |
| Graf, Wierzcholek, Krawedz | Graf, Wierzchołek, Krawędź | UC-02 |
| DaneSortowania | Dane wejściowe | UC-01, UC-04 |
| Wizualizacja | Wizualizacja, Liczba operacji | UC-01, UC-02, UC-03 |
| PorownanieAlgorytmow | Porównanie algorytmów | UC-04 |
| KatalogAlgorytmow, KatalogGrafow | — (lista dostępnych algorytmów i gotowych grafów) | UC-01, UC-02, UC-04 |
