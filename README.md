# Traveling Salesman Problem - Genetski Algoritam

## Opis projekta

Ovaj projekt implementira rješenje za Problem trgovačkog putnika (TSP) koristeći genetski algoritam. Problem trgovačkog putnika je jedan od najpoznatijih problema u kombinatornoj optimizaciji gdje je cilj pronaći najkraću rutu koja prolazi kroz sve gradove točno jednom i vraća se u početni grad.

## Autori

- **Matej Muller**
- **Gabriel Beronja**

**Fakultet:** Fakultet informatike u Puli  
**Kolegij:** Robotika  
**Mentor:** doc. dr. sc. Ivan Lorencin

## Sadržaj

- [Pregled algoritma](#pregled-algoritma)
- [Instalacija](#instalacija)
- [Korištenje](#korištenje)
- [Parametri algoritma](#parametri-algoritma)
- [Struktura koda](#struktura-koda)
- [Rezultati](#rezultati)
- [Zavisnosti](#zavisnosti)

## Pregled algoritma

Genetski algoritam koristi principe evolucije za rješavanje optimizacijskih problema. Ovaj projekt implementira:

- **PMX (Partially Mapped Crossover)** - specijalizirani operator ukrštanja za TSP
- **Inverzijska mutacija** - obrće redoslijed gradova u nasumičnom segmentu
- **Turnirska selekcija** - bira najbolju jedinku iz nasumičnog skupa
- **Elitizam** - čuva najbolje rute između generacija

## Instalacija

1. Klonirajte repozitorij:

```bash
git clone [URL_REPOZITORIJA]
cd traveling-salesman-genetic-algorithm
```

2. Instalirajte potrebne Python pakete:

```bash
pip install numpy matplotlib
```

## Korištenje

Za pokretanje osnovne simulacije:

```python
python TravelingSalesmanProblem.ipynb
```

Ili otvorite Jupyter notebook i pokrenite sve ćelije.

## Parametri algoritma

Glavni parametri koji se mogu podesiti:

```python
NUM_CITIES = 30          # Broj gradova
COORDINATE_RANGE = 100   # Opseg koordinata
POPULATION_SIZE = 100    # Veličina populacije
GENERATIONS = 500        # Broj generacija
MUTATION_RATE = 0.2      # Stopa mutacije
ELITE_SIZE = 1           # Broj elitnih jedinki
TOURNAMENT_SIZE = 3      # Veličina turnira za selekciju
```

## Struktura koda

### Glavni moduli:

- **Generiranje podataka:** Kreiranje nasumičnih koordinata gradova
- **Fitness funkcija:** Računanje ukupne udaljenosti rute
- **Genetski operatori:**
  - Selekcija (turnirska)
  - Ukrštanje (PMX)
  - Mutacija (inverzijska)
- **Vizualizacija:** Prikaz najbolje rute i konvergencije algoritma

### Ključne funkcije:

- `euclidean_distance()` - Računa euklidsku udaljenost između gradova
- `genetic_algorithm()` - Glavni algoritam optimizacije
- `pmx_crossover()` - PMX operator ukrštanja
- `inversion_mutation()` - Inverzijska mutacija
- `tournament_selection()` - Turnirska selekcija

## Rezultati

Algoritam generira dva glavna prikaza:

1. **Vizualizacija rute:** Grafički prikaz najbolje pronađene rute
2. **Konvergencijski graf:** Praćenje poboljšanja kroz generacije

Tipični rezultati pokazuju:

- Značajno poboljšanje u prvim generacijama
- Postupnu konvergenciju prema optimalnom rješenju
- Finalno poboljšanje od 40-60% u odnosu na početnu rutu

## Zavisnosti

- Python 3.7+
- NumPy (za numeričke operacije)
- Matplotlib (za vizualizaciju)
- Jupyter Notebook (za pokretanje)

## Značajke implementacije

- **Reproducibilnost:** Postavljen seed za konzistentne rezultate
- **Elitizam:** Osigurava zadržavanje najboljih rješenja
- **Modularan kod:** Jasno odvojene funkcionalnosti
- **Vizualno praćenje:** Grafovi rute i konvergencije
- **Performanse:** Optimizirane operacije s NumPy

## Licenca

Ovaj projekt je razvijen u obrazovne svrhe na Fakultetu informatike u Puli.

---

_Napomena: Ovaj projekt je dio kolegija Robotika pod mentorstvom doc. dr. sc. Ivana Lorencina._
