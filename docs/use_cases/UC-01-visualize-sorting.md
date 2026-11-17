# UC-01 — Wizualizacja algorytmu sortowania

## Aktor

Użytkownik

## Cel

Zrozumienie działania wybranego algorytmu sortowania poprzez obserwację kolejnych kroków jego wykonywania.

## Powiązane wymagania

FR-01, FR-02, FR-03, FR-04, FR-06, FR-07, FR-08, FR-13, FR-16

## Warunek wstępny

System udostępnia algorytmy sortowania: sortowanie bąbelkowe i sortowanie przez wstawianie.

## Scenariusz podstawowy

1. Użytkownik wybiera algorytm sortowania z listy dostępnych algorytmów.
2. System wyświetla krótki opis wybranego algorytmu.
3. Użytkownik podaje dane wejściowe lub prosi o wygenerowanie losowych danych.
4. System sprawdza poprawność danych wejściowych.
5. Użytkownik uruchamia wizualizację.
6. System prezentuje kolejne kroki algorytmu, wyróżniając elementy, na których wykonywany jest krok, oraz wyświetla liczbę wykonanych operacji.
7. System prezentuje dane po zakończeniu sortowania.

## Scenariusze alternatywne

- **4a. Niepoprawne dane wejściowe:** System informuje użytkownika o błędach i umożliwia ich poprawienie. Scenariusz wraca do kroku 3.
