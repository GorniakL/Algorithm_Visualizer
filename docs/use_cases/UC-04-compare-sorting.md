# UC-04 — Porównanie algorytmów sortowania

## Aktor

Użytkownik

## Cel

Zobaczenie, czym różnią się dwa algorytmy sortowania i który z nich wykonuje mniej operacji na tych samych danych.

## Powiązane wymagania

FR-01, FR-03, FR-04, FR-14, FR-15, FR-16

## Warunek wstępny

System udostępnia algorytmy sortowania: sortowanie bąbelkowe i sortowanie przez wstawianie.

## Scenariusz podstawowy

1. Użytkownik wybiera dwa algorytmy sortowania do porównania.
2. Użytkownik podaje dane wejściowe lub prosi o wygenerowanie losowych danych.
3. System sprawdza poprawność danych wejściowych.
4. Użytkownik uruchamia porównanie.
5. System prezentuje działanie obu algorytmów na tych samych danych.
6. System prezentuje zestawienie liczby operacji wykonanych przez oba algorytmy.

## Scenariusze alternatywne

- **1a. Wybrano ten sam algorytm dwukrotnie:** System prosi użytkownika o wybór dwóch różnych algorytmów.
- **3a. Niepoprawne dane wejściowe:** System informuje użytkownika o błędach i umożliwia ich poprawienie. Scenariusz wraca do kroku 2.
