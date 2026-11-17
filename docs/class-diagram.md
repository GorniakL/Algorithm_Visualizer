# Diagram klas UML (Unified Modeling Language)

Diagram klas przedstawia klasy systemu, ich atrybuty, metody oraz relacje między nimi. Klasy wynikają z pojęć zdefiniowanych w [słowniku domenowym](glossary.md), a metody z [przypadków użycia](use-cases/README.md).

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
    +{abstract} wykonaj(graf : Graf, start : Wierzcholek) : list<Krok>
}

class SortowanieBabelkowe
class SortowaniePrzezWstawianie
class PrzeszukiwanieWszerz

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
}

class Graf {
    +nazwa : str
    +wierzcholki : list<Wierzcholek>
    +krawedzie : list<Krawedz>
    +pobierzSasiadow(wierzcholek : Wierzcholek) : list<Wierzcholek>
}

class DaneSortowania {
    +elementy : list<int>
    +{static} zTekstu(tekst : str) : DaneSortowania
    +{static} wygenerujLosowe(liczba : int) : DaneSortowania
    +waliduj() : list<str>
}

class Wizualizacja {
    +kroki : list<Krok>
    +stanPoczatkowy : list<int>
    +numerKroku : int
    +tempo : int
    +wstrzymana : bool
    +uruchom()
    +wstrzymaj()
    +wznow()
    +nastepny() : bool
    +poprzedni() : bool
    +ustawTempo(tempo : int)
    +resetuj()
    +pobierzBiezacyKrok() : Krok
    +pobierzStan() : list<int>
    +liczbaOperacji() : int
    +liczbaOperacjiRodzaju(rodzaj : RodzajKroku) : int
}

class Porownanie {
    +dane : DaneSortowania
    +uruchom()
    +pobierzZestawienie() : dict<str, int>
}

class KatalogAlgorytmow {
    +pobierzWszystkie() : list<Algorytm>
    +pobierz(nazwa : str) : Algorytm
}

class KatalogGrafow {
    +pobierzWszystkie() : list<Graf>
    +pobierz(nazwa : str) : Graf
}

Algorytm <|-- AlgorytmSortowania
Algorytm <|-- AlgorytmGrafowy
AlgorytmSortowania <|-- SortowanieBabelkowe
AlgorytmSortowania <|-- SortowaniePrzezWstawianie
AlgorytmGrafowy <|-- PrzeszukiwanieWszerz

Algorytm ..> Krok : tworzy
Krok --> RodzajKroku

Graf "1" *-- "1..*" Wierzcholek
Graf "1" *-- "0..*" Krawedz
Krawedz "*" --> "2" Wierzcholek

Wizualizacja "1" o-- "0..*" Krok
Porownanie "1" *-- "2" Wizualizacja
Porownanie --> DaneSortowania

KatalogAlgorytmow "1" o-- "1..*" Algorytm
KatalogGrafow "1" o-- "1..*" Graf

@enduml
```

## Skąd wynikają klasy

| Klasa | Pojęcie ze słownika | Przypadki użycia |
|---|---|---|
| Algorytm, AlgorytmSortowania, AlgorytmGrafowy | Algorytm, Algorytm sortowania, Algorytm grafowy | UC-01, UC-02, UC-04 |
| SortowanieBabelkowe, SortowaniePrzezWstawianie, PrzeszukiwanieWszerz | Sortowanie bąbelkowe, Sortowanie przez wstawianie, Przeszukiwanie wszerz | UC-01, UC-02, UC-04 |
| Krok, RodzajKroku | Krok algorytmu, Liczba operacji | UC-01, UC-02, UC-03 |
| Graf, Wierzcholek, Krawedz | Graf, Wierzchołek, Krawędź | UC-02 |
| DaneSortowania | Dane wejściowe | UC-01, UC-04 |
| Wizualizacja | Wizualizacja, Tempo wizualizacji, Wyróżnienie | UC-01, UC-02, UC-03 |
| Porownanie | Porównanie algorytmów | UC-04 |
| KatalogAlgorytmow, KatalogGrafow | — (lista dostępnych algorytmów i gotowych grafów) | UC-01, UC-02, UC-04 |
