# Wymagania

Wymagania (Requirements) określają, co system powinien robić oraz jakie właściwości i ograniczenia powinien spełniać.

## Oznaczenia

- **FR** (Functional Requirement) — wymaganie funkcjonalne, określające, co system powinien robić.

- **NFR** (Non-Functional Requirement) — wymaganie niefunkcjonalne, określające, jakie właściwości lub ograniczenia powinien spełniać system.

Każde wymaganie posiada unikalny identyfikator, np. `FR-01` lub `NFR-01`.

## Wymagania funkcjonalne

| ID | Wymaganie |
|---|---|
| FR-01 | System umożliwia użytkownikowi wybór algorytmu z listy dostępnych algorytmów. |
| FR-02 | System wyświetla użytkownikowi krótki opis wybranego algorytmu. |
| FR-03 | System umożliwia użytkownikowi podanie danych wejściowych dla algorytmu sortowania. |
| FR-04 | System umożliwia użytkownikowi wygenerowanie od 2 do 50 losowych liczb całkowitych. Generator domyślnie losuje z zakresu 1–100 i może użyć węższego przedziału. |
| FR-05 | System umożliwia użytkownikowi wybór grafu oraz wierzchołka początkowego oraz końcowego dla algorytmu grafowego. |
| FR-06 | System umożliwia użytkownikowi uruchomienie wizualizacji wybranego algorytmu. |
| FR-07 | System prezentuje kolejne kroki algorytmu w sposób graficzny. |
| FR-08 | System wyróżnia w wizualizacji elementy, na których algorytm aktualnie wykonuje krok. |
| FR-09 | System umożliwia użytkownikowi wstrzymanie i wznowienie wizualizacji. |
| FR-10 | System umożliwia użytkownikowi przejście do następnego i do poprzedniego kroku algorytmu. |
| FR-11 | System umożliwia użytkownikowi zmianę tempa wizualizacji. |
| FR-12 | System umożliwia użytkownikowi przywrócenie wizualizacji do stanu początkowego. |
| FR-13 | System wyświetla liczbę operacji wykonanych przez algorytm do bieżącego kroku. |
| FR-14 | System umożliwia użytkownikowi porównanie dwóch algorytmów sortowania na tych samych danych wejściowych. |
| FR-15 | System prezentuje użytkownikowi zestawienie liczby operacji wykonanych przez porównywane algorytmy. |
| FR-16 | System sprawdza poprawność danych wejściowych i informuje użytkownika o błędach, umożliwiając ich poprawienie przed uruchomieniem wizualizacji. Dla sortowania dopuszcza 2–50 liczb całkowitych o wartościach 1–100. Przy losowaniu obie granice muszą należeć do tego zakresu, a dolna granica może być co najwyżej równa górnej. |

## Wymagania niefunkcjonalne

| ID | Wymaganie |
|---|---|
| NFR-01 | Aplikacja jest dostępna i poprawnie wyświetla się w przeglądarce internetowej. |
| NFR-02 | System reaguje na polecenia użytkownika (uruchomienie, wstrzymanie, zmiana kroku) w czasie nieprzekraczającym 1 sekundy dla 95% poleceń. |
| NFR-03 | System opisuje legendą znaczenie wyróżnień stosowanych w wizualizacji. |


## Pytania otwarte

- W jaki sposób użytkownik definiuje graf: wybiera gotowy, czy tworzy własny?
- Czy porównanie algorytmów ma opierać się na liczbie operacji, czy na czasie wykonania?
- Czy porównywać można także algorytmy grafowe?
- Czy system ma wyświetlać kod lub pseudokod algorytmu i wyróżniać aktualnie wykonywany wiersz?
- Jaki jest maksymalny rozmiar grafu?
- Jaki rozmiar danych wejściowych powinien być obsługiwany, aby wizualizacja pozostała czytelna i płynna?
- Czy użytkownik musi mieć konto, aby korzystać z aplikacji?


## Założenia pierwszej wersji

- System udostępnia algorytmy sortowania: sortowanie bąbelkowe i sortowanie przez wstawianie, oraz jeden algorytm grafowy: przeszukiwanie wszerz.
- Użytkownik wybiera graf spośród gotowych grafów. Graf może być skierowany lub nieskierowany (domyślnie nieskierowany). Krawędź ma wagę całkowitą, domyślnie 1. BFS uwzględnia kierunek krawędzi i pomija jej wagę.
- Porównanie algorytmów opiera się na liczbie operacji i dotyczy algorytmów sortowania.
- Korzystanie z aplikacji nie wymaga konta użytkownika.
