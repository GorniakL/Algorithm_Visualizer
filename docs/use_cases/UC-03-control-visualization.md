# UC-03 — Sterowanie przebiegiem wizualizacji

## Aktor

Użytkownik

## Cel

Obserwowanie działania algorytmu we własnym tempie, z możliwością zatrzymania i powrotu do wcześniejszych kroków.

## Powiązane wymagania

FR-09, FR-10, FR-11, FR-12

## Relacje

Rozszerza UC-01 i UC-02.

## Warunek wstępny

Użytkownik uruchomił wizualizację algorytmu (UC-01 lub UC-02).

## Scenariusz podstawowy

1. Użytkownik wstrzymuje wizualizację.
2. System zatrzymuje prezentację na bieżącym kroku.
3. Użytkownik przechodzi do następnego lub poprzedniego kroku algorytmu.
4. System prezentuje wskazany krok.
5. Użytkownik zmienia tempo wizualizacji.
6. Użytkownik wznawia wizualizację.
7. System kontynuuje prezentację w wybranym tempie.

## Scenariusze alternatywne

- **3a. Brak następnego lub poprzedniego kroku:** System informuje użytkownika, że jest to ostatni lub pierwszy krok algorytmu.
- **\*a. Przywrócenie stanu początkowego:** W dowolnym momencie użytkownik przywraca wizualizację do stanu początkowego, a system prezentuje dane sprzed wykonania algorytmu.
