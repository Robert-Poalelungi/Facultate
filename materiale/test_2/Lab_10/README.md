# Lab 10 — Graph (lista de adiacenta, DFS, BFS)

## Structuri de date

```c
typedef struct {
    int id;
    char* name;
    char* line;
} Station;

struct AdjNode {
    GraphNode* target;   // pointer la nodul vecin
    AdjNode* next;
};

struct GraphNode {
    Station* data;
    AdjNode* adj;        // lista de adiacenta
    GraphNode* next;     // urmatorul nod din graf
};
```

Graf neorientat reprezentat ca **lista inlantuita de noduri**, fiecare nod avand o **lista inlantuita de adiacenta**.

---

## Operatii

| Functie | Descriere |
|---|---|
| `insertNode(graph, station)` | adauga nod nou la inceputul listei |
| `addEdge(graph, id1, id2)` | adauga muchie neorientata (ambele directii) |
| `findById(graph, id)` | cauta nod dupa id |
| `printGraph(graph)` | afiseaza lista de adiacenta |
| `dfs(graph, startId, nodeCount)` | parcurgere in adancime (stiva) |
| `bfs(graph, startId, nodeCount)` | parcurgere in latime (coada) |
| `loadGraph(graph, nodesFile, edgesFile)` | incarca din CSV + edges file |
| `freeGraph(graph)` | elibereaza toata memoria |

---

## DFS vs BFS

```
Graf:
  1 - 2
  |   |
  3 - 4 - 5

DFS din 1: 1 → 2 → 4 → 3 → 5   (merge adanc)
BFS din 1: 1 → 2 → 3 → 4 → 5   (nivel cu nivel)
```

**DFS** — foloseste **stiva** (LIFO):
```
push(start)
while stack not empty:
    id = pop()
    if not visited: mark, print, push vecini
```

**BFS** — foloseste **coada** (FIFO):
```
enqueue(start), mark visited
while queue not empty:
    id = dequeue()
    print
    for fiecare vecin nevizitat: mark, enqueue
```

---

## Pattern visited array

```c
int* visited = calloc(nodeCount + 1, sizeof(int));
// visited[id] = 0 → nevizitat
// visited[id] = 1 → vizitat
// index de la 1, deci size = nodeCount + 1
```

---

## Fisiere de intrare

**stations.csv** — `id,name,line`
```
1,Unirii,M1
2,Romana,M1
...
```

**connections.txt** — `id1,id2` (o muchie per linie)
```
1,2
1,4
...
```
