# algorithm_visualizer

**algorithm_visualizer** to aplikacja webowa, która w przystępny i interaktywny
sposób przedstawia działanie wybranych algorytmów. Pozwala obserwować kolejne
etapy ich wykonywania oraz porównywać ich działanie i efektywność.

## Uruchamianie

W katalogu projektu (obok pliku `requirements.txt`) wykonaj kolejno:

```bash
python -m pip install -r requirements.txt
python src/app.py
```

Otwórz [http://localhost:5000/](http://localhost:5000/) w przeglądarce. Aby zatrzymać serwer, naciśnij Ctrl+C w terminalu.

## Dokumentacja

Projekt będzie rozwijany stopniowo wraz z kolejnymi etapami analizy i projektowania.

- [Wizja](docs/vision.md)
- [Słownik domenowy](docs/glossary.md)
- [Wymagania](docs/requirements.md)
- [Przypadki użycia](docs/use_cases/README.md)
- [Diagram klas](docs/class_diagram.md)

## Struktura

```text
algorithm_visualizer/
├── README.md
├── requirements.txt
├── docs/
│   ├── vision.md
│   ├── glossary.md
│   ├── requirements.md
│   ├── use_cases/
│   │   ├── README.md
│   │   ├── UC_01_visualize_sorting.md
│   │   ├── UC_02_visualize_graph_algorithm.md
│   │   ├── UC_03_control_visualization.md
│   │   └── UC_04_compare_sorting.md
│   └── class_diagram.md
└── src/
    ├── app.py
    ├── krok.py
    ├── graf.py
    └── dane.py
```

## Autor

**Łukasz Górniak**