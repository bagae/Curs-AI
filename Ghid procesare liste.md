# Ghid Liste Python

---

## 1. `range()`

- Creează un interval de numere.  
- Sintaxe:
  - `range(stop)`
  - `range(start, stop)`
  - `range(start, stop, pas)`

Exemplu:

```python
for i in range(1, 6):
    print(i, end=" ")
```

Output:  
```
1 2 3 4 5
```

---

## 2. `len()`

- Returnează numărul de elemente.

```python
lista = [10, 20, 30, 40]
print(len(lista))
```

Output:  
```
4
```

---

## 3. `append()`

- Adaugă un element la sfârșit.

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)
```

Output:  
```
[1, 2, 3, 4]
```

---

## 4. `insert()`

- Adaugă un element pe o poziție specifică.

```python
lista = [1, 2, 3]
lista.insert(1, 10)
print(lista)
```

Output:  
```
[1, 10, 2, 3]
```

---

## 5. `pop()`

- Scoate și returnează elementul de la sfârșit sau de la o poziție.

```python
lista = [1, 2, 3]
x = lista.pop()
print(x, lista)
```

Output:  
```
3 [1, 2]
```

```python
y = lista.pop(0)
print(y, lista)
```

Output:  
```
1 [2]
```

---

## 6. `remove()`

- Șterge prima apariție a unui element.

```python
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)
```

Output:  
```
[1, 3, 2]
```

---

## 7. `sort()` și `sorted()`

- `sort()` sortează lista în loc.  
- `sorted()` returnează o listă nouă sortată.

```python
lista = [3, 1, 4, 2]
lista.sort()
print(lista)  # [1, 2, 3, 4]

lista2 = sorted([3, 1, 4, 2])
print(lista2) # [1, 2, 3, 4]
```

---

## 8. `reverse()`

- Inversează lista în loc.

```python
lista = [1, 2, 3]
lista.reverse()
print(lista)
```

Output:  
```
[3, 2, 1]
```

---

## 9. `count()`

- Numără câte apariții are un element.

```python
lista = [1, 2, 2, 3]
print(lista.count(2))
```

Output:  
```
2
```

---

## 10. `index()`

- Returnează prima poziție a unui element.

```python
lista = [1, 2, 3, 2]
print(lista.index(2))
```
