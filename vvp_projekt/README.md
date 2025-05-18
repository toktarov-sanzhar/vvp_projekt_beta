# Vizualizace fraktálů

## Popis

Tento projekt slouží k vizualizaci dvou známých fraktálových množin:

- Mandelbrotova množina
- Juliova množina (závislá na parametru c)

Uživatel může:

- Přepínat mezi Mandelbrot a Julia režimy
- Měnit počet iterací
- Nastavit reálnou a imaginární část parametru c

Program zobrazí výsledek v interaktivním okně s posuvníky a tlačítkem.

## Spuštění

Z hlavní složky spusť:

```
python3 -m fraktaly.main
```

## Ukázka v Jupyteru

Soubor `examples/ukazka.ipynb` můžeš otevřít v Jupyter Notebooku a spustit ručně.

## Struktura projektu

```
vizualizace_fraktalu/
├── fraktaly/
│   ├── main.py
│   ├── mandelbrot.py
│   ├── julia.py
│   ├── visualizer.py
│   └── __init__.py
├── examples/
│   └── ukazka.ipynb
├── tests/
├── README.md
├── setup.py
```

## Autor

Toktarov Sanzhar
TOK0031
