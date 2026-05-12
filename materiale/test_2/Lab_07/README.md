# Lab 07 — Heap (max-heap pe vector) — walkthrough complet

**Pre-requisites:** vectori, malloc/realloc, recursivitate.

---

## Concept central in 30 secunde

**Heap = arbore binar complet, stocat ca vector.** Aici e **max-heap**: parintele are mereu prioritate >= ambele copii.

**Mapping vector <-> arbore:**
```
index 0       -> radacina
index i:        parintele e la (i-1)/2
                copil stang la 2*i+1
                copil drept la 2*i+2
```

```
            [10]                  vector: [10, 7, 9, 4, 5, 8, 6]
           /     \                index:   0  1  2  3  4  5  6
        [7]       [9]
       /   \     /   \
     [4]   [5] [8]   [6]
```

**2 operatii fundamentale:**
- **Sift-up** (urcare) — folosit la `insertHeap`
- **Sift-down** (coborare) — folosit la `heapify`

---

# Cod + walkthrough

## 1. Headere si structuri

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* description;
    int priority;
} Task;

typedef struct {
    Task* tasks;
    int size;
} Heap;
```

**Pas cu pas:**
- `Task` are 2 campuri: string-ul cu descrierea (alocat dinamic) si prioritatea.
- `Heap` are vectorul `tasks` (alocat dinamic) si `size` (cate elemente sunt efectiv in heap).

**Atentie:** `size` e numarul EFECTIV de elemente, nu capacitatea. Folosim `realloc` la fiecare insert.

---

## 2. `printTask` — afisare task

```c
void printTask(Task task) {
    printf("[Priority %d] %s\n", task.priority, task.description);
}
```

Format: `[Priority 15] Restart hung service`. Primeste task by value (copie).

---

## 3. `swapTask` — schimba doua taskuri (static)

```c
static void swapTask(Task* t1, Task* t2) {
    Task aux = *t1;
    *t1 = *t2;
    *t2 = aux;
}
```

**Pas cu pas:**
1. `Task aux = *t1;` — salveaza continutul primului task
2. `*t1 = *t2;` — suprascrie primul cu al doilea
3. `*t2 = aux;` — pune in al doilea ce era salvat

**De ce `static`:** vizibilitate doar in fisierul curent — functie de uz intern, nu e parte din interfata publica.

---

## 4. `heapify` — sift-down (static)

```c
static void heapify(Heap* heap, int index) {
    int largest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < heap->size && heap->tasks[left].priority > heap->tasks[largest].priority) {
        largest = left;
    }

    if (right < heap->size && heap->tasks[right].priority > heap->tasks[largest].priority) {
        largest = right;
    }

    if (largest != index) {
        swapTask(&heap->tasks[largest], &heap->tasks[index]);
        heapify(heap, largest);
    }
}
```

**Pas cu pas:**

**Bloc 1 — gaseste cel mai mare dintre `index`, `stang`, `drept`:**
```c
int largest = index;
int left = 2 * index + 1;
int right = 2 * index + 2;
```

**Bloc 2 — verifica stangul:**
```c
if (left < heap->size && ...) largest = left;
```
`left < heap->size` — copilul exista? Daca da si e mai mare, updateaza `largest`.

**Bloc 3 — verifica dreptul:**
Identic, dar compara cu `largest` (care poate fi acum stangul).

**Bloc 4 — daca exista un copil mai mare:**
```c
if (largest != index) {
    swapTask(...);
    heapify(heap, largest);
}
```
Swap + recursiv mai jos — s-ar putea ca acolo regula sa fie din nou incalcata.

**Diferenta fata de versiunea veche:** ia `Heap*` (pointer), nu by value. Modificarile sunt vizibile in apelant.

**Mnemonic:** "gaseste cel mai mare dintre eu+copii, daca nu sunt eu → swap si continua de acolo".

**Complexitate:** O(log n).

---

## 5. `initHeap` — heap gol

```c
Heap initHeap() {
    Heap heap;
    heap.size = 0;
    heap.tasks = malloc(0);
    return heap;
}
```

`malloc(0)` — returneaza un pointer valid (comportament standard C), suficient pentru primul `realloc` din `insertHeap`.

---

## 6. `insertHeap` — inserezi cu **sift-up**

```c
void insertHeap(Heap* heap, Task task) {
    heap->size++;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));

    int index = heap->size - 1;
    heap->tasks[index] = task;

    int parent = (index - 1) / 2;

    while (index > 0 && heap->tasks[index].priority > heap->tasks[parent].priority) {
        swapTask(&heap->tasks[index], &heap->tasks[parent]);
        index = parent;
        parent = (index - 1) / 2;
    }
}
```

**Pas cu pas:**

**Bloc 1 — alocare loc:**
```c
heap->size++;
heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
```
Marim cu 1. `realloc` extinde (sau muta) vectorul.

**Bloc 2 — pune task-ul la final:**
```c
int index = heap->size - 1;
heap->tasks[index] = task;
```

**Bloc 3 — sift-up:**
```c
int parent = (index - 1) / 2;
while (index > 0 && heap->tasks[index].priority > heap->tasks[parent].priority) {
    swapTask(...);
    index = parent;
    parent = (index - 1) / 2;
}
```
- `index > 0` — conditie de stop la radacina (evita swap cu el insusi la index 0).
- Cat timp prioritatea copilului > parintelui: swap si urca.

**Mnemonic:** "urca pana esti sef sau atingi varful".

**Complexitate:** O(log n).

---

## 7. `deleteFromHeap` — extrage maximul

```c
Task deleteFromHeap(Heap* heap) {
    Task top = heap->tasks[0];

    heap->tasks[0] = heap->tasks[heap->size - 1];
    heap->size--;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));

    heapify(heap, 0);

    return top;
}
```

**Pas cu pas:**

1. Salveaza maximul (radacina, index 0).
2. Pune ultimul element pe locul radacinii.
3. Scade size-ul si realloc.
4. `heapify(heap, 0)` — coboara noul element de la radacina pana isi gaseste locul.

**Diferenta fata de versiunea veche:** un singur apel `heapify(heap, 0)` in loc de un loop de la `size/2`. E corect si eficient — iti trebuie doar sa repari radacina.

---

## 8. `printHeap` — afisare heap

```c
void printHeap(Heap* heap) {
    for (int i = 0; i < heap->size; i++) {
        printTask(heap->tasks[i]);
    }
}
```

Afiseaza fiecare task complet (prioritate + descriere) in ordinea din vector. **NU e ordine sortata** — heap-ul respecta doar `parinte >= copii`.

---

## 9. `buildHeap` — din array la heap valid

```c
Heap buildHeap(Task* tasks, int size) {
    Heap heap;
    heap.size = size;
    heap.tasks = malloc(size * sizeof(Task));

    for (int i = 0; i < size; i++) {
        heap.tasks[i] = tasks[i];
    }

    for (int i = heap.size / 2 - 1; i >= 0; i--) {
        heapify(&heap, i);
    }

    return heap;
}
```

**Pas cu pas:**

**Bloc 1 — copiaza array-ul:**
```c
for (int i = 0; i < size; i++) {
    heap.tasks[i] = tasks[i];
}
```
Copie shallow (struct assignment) — string-urile `description` raman pointeri la datele originale.

**Bloc 2 — heapify de la mijloc spre inceput:**
```c
for (int i = heap.size / 2 - 1; i >= 0; i--) {
    heapify(&heap, i);
}
```
- Indexii > `size/2` sunt **frunze** — n-au copii, skip.
- Mergand invers, cand ajungi la `i`, sub-arborii lui sunt deja heapified.

**Complexitate:** O(n) (nu O(n log n)).

---

## 10. `freeHeap` — eliberare memorie

```c
void freeHeap(Heap* heap) {
    for (int i = 0; i < heap->size; i++) {
        free(heap->tasks[i].description);
    }
    free(heap->tasks);
    heap->tasks = NULL;
    heap->size = 0;
}
```

Elibereaza fiecare `description` (string alocat dinamic), apoi vectorul `tasks`. Seteaza pointerii la NULL si size la 0 ca "sentinel".

**Atentie:** apelezi `freeHeap` doar pe un heap incarcat din fisier (unde descripțiile sunt `malloc`-uite). Pe un heap construit din `buildHeap` cu string literals, `free` pe literale e UB.

---

## 11. `loadTasks` — citire CSV

```c
int loadTasks(const char* filename, Heap* heap) {
    FILE* f = fopen(filename, "r");
    if (f == NULL) {
        printf("Error: could not open file '%s'\n", filename);
        return -1;
    }

    char line[128];
    int count = 0;

    while (fgets(line, sizeof(line), f) != NULL) {
        Task task;

        char* token = strtok(line, ",");
        task.priority = atoi(token);

        token = strtok(NULL, ",");
        token[strcspn(token, "\n")] = '\0';
        task.description = malloc(strlen(token) + 1);
        strcpy(task.description, token);

        insertHeap(heap, task);
        count++;
    }

    fclose(f);
    return count;
}
```

**Format scheduler.txt:** `prioritate,descriere` — ex. `15,Restart hung service`

**Pas cu pas:**
1. `fopen` + check NULL → returneaza `-1` la eroare.
2. `while (fgets(...) != NULL)` — pattern corect (NU `feof`).
3. `strtok(line, ",")` → prioritatea, `atoi`.
4. `strtok(NULL, ",")` → descrierea, `strcspn` scoate `\n`, `malloc + strcpy`.
5. Returneaza numarul de taskuri citite.

---

## 12. `main`

```c
int main() {
    Heap heap = initHeap();
    int count = loadTasks("scheduler.txt", &heap);
    // ... check count < 0 ...

    printf("Loaded %d tasks:\n", count);
    printHeap(&heap);

    printf("\n--- Processing tasks by priority ---\n\n");
    while (heap.size > 0) {
        Task task = deleteFromHeap(&heap);
        printf("Processing: ");
        printTask(task);
        free(task.description);
    }
    freeHeap(&heap);

    printf("\n--- Build heap from unordered array ---\n\n");
    Task unordered[] = {
        {"Fix typo in docs", 3}, {"Patch SQL injection", 28}, ...
    };
    int size = sizeof(unordered) / sizeof(Task);
    Heap heap2 = buildHeap(unordered, size);
    printHeap(&heap2);
    freeHeap(&heap2);

    return 0;
}
```

3 demo-uri:
1. **Citire din fisier + printHeap** — verifici ordinea din vector (parinte >= copii, NU sortat).
2. **Processing loop** — extrage taskurile unul cate unul in ordine descrescatoare a prioritatii (heap sort).
3. **buildHeap** dintr-un array neordonat — verifici ca heapify de la mijloc construieste un max-heap valid.

---

# Functii pentru testul 2

Acestea NU sunt in cod — le scrii TU. Patternuri:

## A. Numarare cu conditie

```c
int countByCondition(Heap* heap, /* parametri pentru conditie */) {
    int count = 0;
    for (int i = 0; i < heap->size; i++) {
        if (/* CONDITIA TA — ex. heap->tasks[i].priority > 20 */) {
            count++;
        }
    }
    return count;
}
```

**Idee:** parcurgere LINIARA a vectorului (nu recursivitate).

## B. Stergere cu criteriu

```c
void deleteByCondition(Heap* heap, /* parametri */) {
    int i = 0;
    while (i < heap->size) {
        if (/* CONDITIA TA */) {
            swapTask(&heap->tasks[i], &heap->tasks[heap->size - 1]);
            free(heap->tasks[heap->size - 1].description);
            heap->size--;
            heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
            heapify(heap, i);
            // NU incrementa i — noul element de pe pozitia i poate indeplini si el conditia
        } else {
            i++;
        }
    }
}
```

**Atentie:** `if-else` cu `i++` doar pe ramura de "nu sterge".

## C. Salvare cu filtru

```c
Task* saveMatching(Heap* heap, /* parametri */, int* outSize) {
    Task* result = NULL;
    *outSize = 0;
    for (int i = 0; i < heap->size; i++) {
        if (/* CONDITIA TA */) {
            (*outSize)++;
            result = realloc(result, (*outSize) * sizeof(Task));
            result[*outSize - 1].priority = heap->tasks[i].priority;
            result[*outSize - 1].description = malloc(strlen(heap->tasks[i].description) + 1);
            strcpy(result[*outSize - 1].description, heap->tasks[i].description);
        }
    }
    return result;
}
```

---

# Capcane

| Capcana | Antidot |
|---------|---------|
| `(i-1)/2` cand i=0 da 0 (parinte = el insusi) | Conditia `index > 0` in while opreste loop-ul inainte de swap. |
| `heapify` ia `Heap*`, nu `Heap` | Pasezi `&heap`, nu `heap`. |
| Crezi ca `printHeap` afiseaza sortat | NU. Afiseaza ordinea din vector — heap-ul nu e sortat. |
| Confuzii intre sift-up si sift-down | `insertHeap` urca (sift-up). `heapify` coboara (sift-down). |
| `deleteFromHeap` mai apeleaza `heapify` in loop | NU. Un singur `heapify(heap, 0)` e suficient. |
| `feof` in loc de `fgets != NULL` | Anti-pattern. Foloseste mereu `while (fgets(...) != NULL)`. |

---

# Self-test (fara cod deschis)

- [ ] Pot desena vectorul `[10, 5, 8, 3, 4, 7, 2]` ca arbore in 1 min.
- [ ] Pot scrie `swapTask` in 1 min.
- [ ] Pot scrie `insertHeap` cu sift-up in 5 min (cu conditia `index > 0`).
- [ ] Pot scrie `heapify` recursiv cu `Heap*` in 5 min.
- [ ] Pot scrie `deleteFromHeap` cu un singur `heapify(heap, 0)` in 4 min.
- [ ] Pot scrie `buildHeap` cu `size/2 - 1` corect.
- [ ] Pot scrie cele 3 functii pentru testul 2 (count, delete, save) in 15 min.
- [ ] Pot explica de ce `buildHeap` e O(n), nu O(n log n).

Daca bifezi 7/8 -> stapanesti Heap.
