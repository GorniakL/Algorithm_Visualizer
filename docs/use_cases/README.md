# Przypadki użycia


## Wersja Mermaid

### 1. Aktor i przypadek użycia

```mermaid
flowchart LR
    Uzytkownik["Użytkownik"]
    UC01([Wizualizacja algorytmu sortowania])

    Uzytkownik --- UC01
```

### 2. Granice systemu i relacja rozszerzenia

```mermaid
flowchart LR
    Uzytkownik["Użytkownik"]

    subgraph System["algorithm-visualizer"]
        UC01([UC-01<br/>Wizualizacja algorytmu sortowania])
        UC02([UC-02<br/>Wizualizacja algorytmu grafowego])
        UC03([UC-03<br/>Sterowanie przebiegiem wizualizacji])
        UC04([UC-04<br/>Porównanie algorytmów sortowania])
    end

    Uzytkownik --- UC01
    Uzytkownik --- UC02
    Uzytkownik --- UC03
    Uzytkownik --- UC04

    UC03 -.->|rozszerza| UC01
    UC03 -.->|rozszerza| UC02
```

## Wersja PlantUML — zgodna z notacją UML

### 1. Aktor i przypadek użycia

```plantuml
@startuml
actor Użytkownik
usecase "Wizualizacja algorytmu sortowania" as UC01
Użytkownik --> UC01
@enduml
```

### 2. Granice systemu i relacja rozszerzenia

```plantuml
@startuml
left to right direction

actor Użytkownik

rectangle "algorithm-visualizer" {
    usecase "UC-01\nWizualizacja algorytmu sortowania" as UC01
    usecase "UC-02\nWizualizacja algorytmu grafowego" as UC02
    usecase "UC-03\nSterowanie przebiegiem wizualizacji" as UC03
    usecase "UC-04\nPorównanie algorytmów sortowania" as UC04
}

Użytkownik -- UC01
Użytkownik -- UC02
Użytkownik -- UC03
Użytkownik -- UC04

UC03 ..> UC01 : <<extend>>
UC03 ..> UC02 : <<extend>>
@enduml
```


## Katalog przypadków użycia

| ID | Przypadek użycia | Aktor | Wymagania |
|----|------------------|-------|-----------|
| [UC-01](UC-01-visualize-sorting.md) | Wizualizacja algorytmu sortowania | Użytkownik | FR-01, FR-02, FR-03, FR-04, FR-06, FR-07, FR-08, FR-13, FR-16 |
| [UC-02](UC-02-visualize-graph-algorithm.md) | Wizualizacja algorytmu grafowego | Użytkownik | FR-01, FR-02, FR-05, FR-06, FR-07, FR-08, FR-13 |
| [UC-03](UC-03-control-visualization.md) | Sterowanie przebiegiem wizualizacji | Użytkownik | FR-09, FR-10, FR-11, FR-12 |
| [UC-04](UC-04-compare-sorting.md) | Porównanie algorytmów sortowania | Użytkownik | FR-01, FR-03, FR-04, FR-14, FR-15, FR-16 |