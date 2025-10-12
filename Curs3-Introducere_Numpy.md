# Introducere în NumPy 

## Ce este NumPy?

**NumPy (Numerical Python)** este o bibliotecă open-source pentru Python utilizată pentru **procesare numerică**, **operații vectoriale** și **calcul științific**.  
Permite manipularea eficientă a datelor sub formă de array-uri multidimensionale.

---

## Avantajele utilizării NumPy

-  Rapid, scris în C pentru performanță ridicată  
- Ușor de folosit pentru calcule matematice complexe  
-  Se integrează perfect cu alte biblioteci științifice Python  

---

##  Instalare

```bash
pip install numpy
```
Instalează biblioteca folosind `pip`, managerul de pachete Python.

---

##  Import și creare de array-uri

```python
import numpy as np

a = np.array([1, 2, 3, 4])          # creează un array 1D dintr-o listă Python
b = np.array([[1, 2, 3], [4, 5, 6]]) # creează un array 2D
zeros = np.zeros((3, 3))             # creează o matrice 3x3 plină cu zerouri
rand = np.random.rand(2, 3)          # generează o matrice 2x3 cu valori aleatorii
```
Fiecare metodă creează tipuri diferite de array-uri în funcție de necesitate.

---

## Proprietăți importante ale unui array

```python
print(a.ndim)   # număr de dimensiuni (1D, 2D etc.)
print(a.shape)  # dimensiunea pe fiecare axă
print(a.size)   # numărul total de elemente
print(a.dtype)  # tipul de date al elementelor
```
Aceste proprietăți oferă informații despre structura și conținutul array-ului.

---

## Operații între elementele vectorilor

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)   # adună elementele corespunzătoare
print(x - y)   # scade elementele corespunzătoare
print(x * y)   # înmulțire element cu element
print(x / y)   # împărțire element cu element
print(np.sqrt(x))  # calculează rădăcina pătrată pentru fiecare element
```
Operațiile sunt efectuate rapid pe toate elementele din array simultan.

---

## Indexare

```python
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0, 2])     # accesează elementul din prima linie, a treia coloană

```
Permite selectarea și modificarea precisă a sub-secțiunilor dintr-un array.

---

##  Funcții utile pentru calculul statistic

| Funcție | Descriere |
|----------|------------|
| `np.mean(arr)` | Calculează media aritmetică a elementelor |
| `np.median(arr)` | Returnează mediana valorilor |
| `np.std(arr)` | Calculează deviația standard |
| `np.sum(arr)` | Returnează suma tuturor elementelor |
| `np.max(arr)` | Returnează valoarea maximă |
| `np.min(arr)` | Returnează valoarea minimă |
| `np.var(arr)` | Calculează varianța |
| `np.unique(arr)` | Returnează elementele unice din array |

---

## Algebră liniară

```python
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

C = np.dot(A, B)        # produs matricial (A × B)
detA = np.linalg.det(A) # calculează determinantul matricei
invA = np.linalg.inv(A) # calculează inversa matricei
```
Funcțiile din `np.linalg` oferă instrumente pentru calcule matriciale avansate.

---

## Generarea de date numerice

```python
v = np.arange(0, 10, 2)   # vector de la 0 la 10 cu pas 2
lin = np.linspace(0, 1, 5) # 5 valori egal distanțate între 0 și 1
```
Folosite pentru a genera secvențe numerice .

---

## Aplicații practice
1. Calculul sumei și produsului elementelor dintr-un vector
2. Eliminarea valorilor duplicate dintr-un vector
3. Înlocuirea valorilor NaN cu media numerelor diferite de Nan