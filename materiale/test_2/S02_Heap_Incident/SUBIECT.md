# S02 - Max-Heap | Incident Response System

Implement a C application for managing a cybersecurity incident response system using a max-heap.

---

## Data Structure

Define the `Incident` structure containing:

| Field | Type | Description |
|---|---|---|
| id | int | Unique incident identifier |
| title | char* | Short description of the incident |
| affectedSystem | char* | e.g. "Database", "API Gateway", "Auth Service" |
| severity | int | Priority key for the heap (1–10) |
| responseTime | int | Expected response time in minutes |

---

## Requirements

**1. (2p)** Load at least 8 incidents from a .csv file and insert them one by one into a max-heap keyed by `severity`. Print the heap array after loading.

**2. (1p)** Define a hardcoded array of at least 5 incidents, build a max-heap from it using `buildHeap`, and print the resulting heap array.

**3. (2p)** Extract incidents from the heap one by one (highest severity first) until only incidents with severity below a threshold remain. Print each extracted incident and the heap state after each extraction.

**4. (4p)** Implement a function `exportIncidents` that scans the heap array and exports all incidents matching a condition into a dynamically allocated array of `Incident*` pointers, using a **function pointer** as the filter. Test with two filters:
- one that filters by severity above a threshold
- one that filters by affectedSystem equal to a specific name

Display the exported array after each call.

> If the function pointer is not used and the condition is hardcoded, a maximum of 2p will be awarded for this step.

---

## Rezolvare

- `S02.c` — cod complet one-file
- `incidents.csv` — date de test (10 incidente)

### Puncte cheie de retinut

**Heap stocheaza Incident by VALUE (nu pointer):**
```c
typedef struct {
    Incident* incidents;
    int size;
} Heap;
```

**Function pointer (cerinta 4):**
```c
typedef int (*IncidentFilter)(Incident*);

Incident** exportIncidents(Heap* heap, IncidentFilter filter, int* count);
```

**Export = scanare liniara a vectorului (nu recursiv, e heap nu BST):**
```c
for (int i = 0; i < heap->size; i++) {
    if (filter(&heap->incidents[i])) { ... }
}
```

**Threshold global pentru function pointer:**
```c
static int severityThreshold = 7;
static char* systemFilter = "Database";
```
