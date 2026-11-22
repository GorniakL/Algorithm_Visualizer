# UC-02 — Wizualizacja algorytmu grafowego

## Aktor

Użytkownik

## Cel

Zrozumienie działania algorytmu grafowego poprzez obserwację kolejnych kroków jego wykonywania na grafie.

## Powiązane wymagania

FR-01, FR-02, FR-05, FR-06, FR-07, FR-08, FR-13, FR-16

## Warunek wstępny

System udostępnia algorytm przeszukiwania wszerz oraz co najmniej jeden gotowy graf.

## Scenariusz podstawowy

1. Użytkownik wybiera algorytm grafowy z listy dostępnych algorytmów.
2. System wyświetla krótki opis wybranego algorytmu.
3. Użytkownik wybiera jeden z gotowych grafów oraz wierzchołek początkowy.
4. Użytkownik uruchamia wizualizację.
5. System prezentuje kolejne kroki algorytmu na grafie, wyróżniając odwiedzane wierzchołki i krawędzie, oraz wyświetla liczbę wykonanych operacji. W grafie skierowanym BFS przechodzi od początku krawędzi do jej końca, a w nieskierowanym może przejść w obu kierunkach. Waga krawędzi nie wpływa na wybór sąsiada.
6. System prezentuje graf po zakończeniu działania algorytmu.

## Scenariusze alternatywne

- **4a. Nie wybrano wierzchołka początkowego:** System prosi użytkownika o jego wskazanie przed uruchomieniem wizualizacji. Scenariusz wraca do kroku 3.
