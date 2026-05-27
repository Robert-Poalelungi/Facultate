# Rezumat teoretic — Structuri de Date (SDD)

> Acoperă toată materia de seminar: Lab 03 → Lab 10.  
> Fiecare secțiune: concept, structuri, operații, complexitate, capcane.

---

## Cuprins

1. [Fundamente C](#1-fundamente-c)
2. [Lab 03 — Lista simplu înlănțuită](#2-lab-03--lista-simplu-înlănțuită)
3. [Lab 04 — Delete + Function Pointers](#3-lab-04--delete--function-pointers)
4. [Lab 05 — Lista dublu înlănțuită](#4-lab-05--lista-dublu-înlănțuită)
5. [Lab 06 — Hash Table](#5-lab-06--hash-table)
6. [Lab 07 — Heap](#6-lab-07--heap)
7. [Lab 08 — BST (Binary Search Tree)](#7-lab-08--bst-binary-search-tree)
8. [Lab 09 — AVL Tree](#8-lab-09--avl-tree)
9. [Lab 10 — Graf (DFS / BFS)](#9-lab-10--graf-dfs--bfs)
10. [Tabel comparativ final](#10-tabel-comparativ-final)

---

---

# 1. Fundamente C

## Pointeri și indirectare

Un **pointer** stochează o adresă de memorie.

```
int x = 42;
int* p = &x;   // p = adresa lui x

*p             // valoarea de la adresa p  → 42
&x             // adresa variabilei x      → ex. 0x7ffd...
p              // adresa stocată în p      → ex. 0x7ffd...
```

| Expresie | Semnificație |
|---|---|
| `int* p` | pointer la int |
| `&x` | adresa lui x |
| `*p` | valoarea pointată de p (dereferențiere) |
| `p->field` | echivalent cu `(*p).field` |

## Pointer la pointer (`**`)

Necesar când o funcție trebuie să **modifice un pointer din apelant**.

```c
void f(int** pp) {
    *pp = malloc(sizeof(int));
    **pp = 99;
}

int* p = NULL;
f(&p);          // acum p pointează la un int cu valoarea 99
```

**Regula:** dacă funcția poate schimba capul unei liste / rădăcina unui arbore → primește `Node**` / `TreeNode**`.

## malloc / realloc / free

```c
void* malloc(size_t size)           // aloca size bytes, neinitialized
void* calloc(size_t n, size_t size) // aloca n*size bytes, initializat cu 0
void* realloc(void* ptr, size_t sz) // redimensionează blocul
void  free(void* ptr)               // eliberează blocul
```

**Reguli esențiale:**
- Fiecare `malloc`/`calloc` → exact un `free`
- Nu accesa memoria după `free` (dangling pointer)
- Nu da `free` de două ori aceluiași pointer (double free)
- `realloc` poate muta blocul → **nu mai folosi pointer-ul vechi**

## Deep copy vs. shallow copy

```c
// Shallow copy — ambii pointeri pointează la același string
Task t2 = t1;                     // t2.description == t1.description (aceeași adresă)

// Deep copy — copie independentă
t2.description = malloc(strlen(t1.description) + 1);
strcpy(t2.description, t1.description);
```

**Când e necesar deep copy:** ori de câte ori inserezi date din un buffer temporar (ex. `line[256]` din `fgets`) sau când două structuri trebuie să aibă viețile independente.

## Pattern fgets + strtok (citire CSV)

```c
char line[256];
while (fgets(line, sizeof(line), f)) {
    char* token = strtok(line, ",");   // primul câmp
    int id = atoi(token);

    token = strtok(NULL, ",");         // al doilea câmp (NULL = continuă)
    char* name = malloc(strlen(token) + 1);
    strcpy(name, token);

    token = strtok(NULL, ",");
    token[strcspn(token, "\n")] = '\0'; // elimină newline
    // ...
}
```

---

---

# 2. Lab 03 — Lista simplu înlănțuită

## Concept

O **listă simplu înlănțuită** este o colecție de noduri unde fiecare nod pointează la **nodul următor**. Ultimul nod pointează la `NULL`.

```
head → [data|next] → [data|next] → [data|next] → NULL
```

## Structuri

```c
typedef struct Node {
    DataType* data;
    struct Node* next;
} Node;
```

`head` este un `Node*` inițializat cu `NULL` (lista goală).

## Operații și complexitate

| Operație | Complexitate | Notă |
|---|---|---|
| `addToBeginning` | **O(1)** | Nodul nou devine capul |
| `addToEnd` | **O(N)** | Trebuie parcursă lista |
| `search` | **O(N)** | Căutare liniară |
| `deleteFromBeginning` | **O(1)** | Avansează capul |
| `deleteFromEnd` | **O(N)** | Trebuie găsit penultimul |
| `freeList` | **O(N)** | Fiecare nod se eliberează |

## Implementare — operații esențiale

### addToBeginning
```c
void addToBeginning(Node** list, DataType* data) {
    Node* node  = malloc(sizeof(Node));
    node->data  = data;
    node->next  = *list;   // noul nod pointează la vechiul cap
    *list       = node;    // capul listei devine noul nod
}
```

### addToEnd
```c
void addToEnd(Node** list, DataType* data) {
    Node* node  = malloc(sizeof(Node));
    node->data  = data;
    node->next  = NULL;
    if (*list == NULL) { *list = node; return; }
    Node* cur = *list;
    while (cur->next) cur = cur->next;
    cur->next = node;
}
```

### freeList (corect)
```c
void freeList(Node* list) {
    while (list) {
        Node* next = list->next;  // salvezi ÎNAINTE de free
        free(list->data->name);   // câmpuri char* din struct
        free(list->data);         // struct-ul
        free(list);               // nodul
        list = next;
    }
}
```

## Capcane frecvente

| Greșeală | Corect |
|---|---|
| `node->next = list` (în loc de `*list`) | `node->next = *list` |
| `free(list); list = list->next;` | Salvezi `next` înainte de `free` |
| `while (cur->next)` la search | `while (cur)` — altfel nu verifici ultimul nod |
| Funcție primește `Node*` când modifică capul | Trebuie `Node**` |

---

---

# 3. Lab 04 — Delete + Function Pointers

## Delete by condition — pattern

```c
void deleteByCondition(Node** list, int (*cond)(Node*)) {
    while (*list) {
        if (cond(*list)) {
            Node* toDelete = *list;
            *list = (*list)->next;    // scoatem nodul din lanț
            free(toDelete->data);
            free(toDelete);
            // NU avansăm list — noul *list trebuie și el verificat
        } else {
            list = &(*list)->next;    // avansăm la următorul
        }
    }
}
```

**Vizual:**
```
list → [A] → [B] → [C] → NULL
       ↑
       *list

Dacă B trebuie șters:
  Când list = &A->next, *list = B
  *list = B->next = C    → A->next pointează direct la C
  free(B)
```

## Function pointers

### Declarație
```c
// Pointer la funcție care primește Node* și returnează int
typedef int (*CondFn)(Node*);

// Fără typedef
int (*cond)(Node*);
```

### Utilizare
```c
int isExpensive(Node* n) { return n->data->price > 100; }

deleteByCondition(&list, isExpensive);
// sau
CondFn fn = isExpensive;
deleteByCondition(&list, fn);
```

### De ce e util
Poți schimba comportamentul funcției **fără să schimbi codul ei** — trimiți o altă funcție ca argument. Pattern folosit extensiv în Lab 09 (AVL export cu FilterFunc) și Lab 04 (deleteByCondition, insertByChoice).

### Threshold global (limitare C)
Function pointer-ul nu poate lua parametri extra. Soluție standard: variabilă globală statică.

```c
static float threshold = 7.0f;

int filterBySeverity(const Vulnerability* v) {
    return v->severity > threshold;   // citește variabila globală
}

threshold = 9.0f;
exportByCondition(root, filterBySeverity, &count);
```

---

---

# 4. Lab 05 — Lista dublu înlănțuită

## Concept

Fiecare nod are **doi pointeri**: `prev` (spre nodul anterior) și `next` (spre nodul următor).

```
NULL ← [prev|data|next] ↔ [prev|data|next] ↔ [prev|data|next] → NULL
        ↑ head                                         ↑ tail (opțional)
```

## Structură

```c
typedef struct DNode {
    DataType* data;
    struct DNode* prev;
    struct DNode* next;
} DNode;
```

## Inserare la început

```c
void addToBeginning(DNode** head, DataType* data) {
    DNode* node = malloc(sizeof(DNode));
    node->data  = data;
    node->prev  = NULL;
    node->next  = *head;
    if (*head) (*head)->prev = node;   // vechiul cap pointează înapoi
    *head = node;
}
```

**Pointeri modificați:** 4 total (cei 2 ai nodului nou + `prev`-ul vechiului cap + `next`-ul nodului precedent la inserare la mijloc).

## Avantaj față de lista simplă

| Operație | Lista simplă | Lista dublă |
|---|---|---|
| Ștergere nod (ai pointer la el) | O(N) — găsești predecesorul | **O(1)** — cunoști `prev` |
| Parcurgere inversă | Imposibil direct | O(N) prin `prev` |
| Inserare înainte de nod dat | O(N) | **O(1)** |

## Capcane

- La inserare/ștergere actualizezi **ambii** pointeri ai tuturor nodurilor afectate
- La inserare la început: dacă lista era goală, `(*head)->prev` ar crăpa → verifici `if (*head)`
- La ștergere: dacă nodul e capul, `node->prev == NULL` → tratezi separat

---

---

# 5. Lab 06 — Hash Table

## Concept

Un **hash table** mapează chei la valori folosind o **funcție hash** care transformă cheia într-un index de bucket.

```
key → hash(key) % size → index → bucket[index]
```

## Funcția hash (suma ASCII)

```c
int hash(int size, const char* key) {
    int sum = 0;
    for (int i = 0; key[i]; i++)
        sum += (int)key[i];
    return sum % size;
}
```

**Proprietăți dorite:** distribuție uniformă (evită coliziuni), eficiență O(1).

## Coliziuni — rezolvare prin chaining

Când `hash(key1) == hash(key2)` (chei diferite, același index), se formează o **listă înlănțuită** în acel bucket.

```
buckets:
[0]: NULL
[1]: [Team A] → [Team B] → NULL   ← coliziune între A și B
[2]: [Team C] → NULL
[3]: NULL
```

## Structuri

```c
typedef struct Node {
    TeamType* data;
    struct Node* next;
} Node;

typedef struct {
    int size;
    Node** buckets;   // array de pointeri la liste
} HashTable;
```

## Inițializare

```c
HashTable ht;
ht.size    = 10;
ht.buckets = calloc(ht.size, sizeof(Node*));
// calloc → toți pointerii inițializați cu NULL
```

## Operații

### Insert (prepend în bucket)
```c
void insert(HashTable* ht, TeamType* data) {
    int idx   = hash(ht->size, data->name);
    Node* node = malloc(sizeof(Node));
    node->data = data;
    node->next = ht->buckets[idx];
    ht->buckets[idx] = node;
}
```

### Search
```c
Node* search(HashTable* ht, const char* name) {
    int idx  = hash(ht->size, name);
    Node* cur = ht->buckets[idx];
    while (cur) {
        if (strcmp(cur->data->name, name) == 0) return cur;
        cur = cur->next;
    }
    return NULL;
}
```

### Delete by condition (toate bucket-urile)
```c
void deleteByCountry(HashTable* ht, const char* country) {
    for (int i = 0; i < ht->size; i++) {
        Node** cur = &ht->buckets[i];
        while (*cur) {
            if (strcmp((*cur)->data->country, country) == 0) {
                Node* del = *cur;
                *cur = (*cur)->next;
                free(del->data->name);
                free(del->data);
                free(del);
                // NU avansăm cur
            } else {
                cur = &(*cur)->next;
            }
        }
    }
}
```

## Complexitate

| Operație | Caz mediu | Caz rău (toți în același bucket) |
|---|---|---|
| Insert | **O(1)** | O(1) — prepend |
| Search | **O(1)** amortizat | O(N) |
| Delete | **O(1)** amortizat | O(N) |

> **Load factor** = N/M (N elemente, M bucket-uri). Performanță bună când load factor ≈ 1.

## Capcane

- `malloc` în loc de `calloc` la inițializare → bucket-urile conțin garbage, nu NULL
- Shallow copy la `data->name = key` → dangling pointer dacă sursa e un buffer refolosit
- `printHashTable` afișează și bucket-urile goale (cu `NULL`)

---

---

# 6. Lab 07 — Heap

## Concept

Un **heap** este un **arbore binar complet** (toate nivelurile pline, ultimul completat de la stânga) stocat ca **vector**.

- **Max-heap:** `parent.priority >= children.priority` → rădăcina = maximul
- **Min-heap:** `parent.priority <= children.priority` → rădăcina = minimul

```
Max-heap ca arbore:          Ca vector:
        [10]                 idx: 0  1  2  3  4  5  6
       /    \                val:[10, 7, 9, 4, 5, 8, 6]
     [7]    [9]
    /   \  /   \
  [4] [5][8]  [6]
```

## Formula de indexare

```
Nod la index i:
  ├── Părinte:      (i - 1) / 2
  ├── Copil stâng:  2*i + 1
  └── Copil drept:  2*i + 2
```

## Structuri

```c
typedef struct {
    char* description;
    int priority;
} Task;

typedef struct {
    Task* tasks;
    int size;
} Heap;
```

## Operații fundamentale

### heapify (sift-down) — O(log N)
Coboară un element la locul lui corect. Se aplică **top-down** (de la rădăcină spre frunze).

```c
static void heapify(Heap* heap, int index) {
    int largest = index;
    int left    = 2 * index + 1;
    int right   = 2 * index + 2;

    if (left  < heap->size && heap->tasks[left].priority  > heap->tasks[largest].priority)
        largest = left;
    if (right < heap->size && heap->tasks[right].priority > heap->tasks[largest].priority)
        largest = right;

    if (largest != index) {
        swapTask(&heap->tasks[largest], &heap->tasks[index]);
        heapify(heap, largest);   // recursiv în jos
    }
}
```

### insertHeap — O(log N)
Adaugă la final + **sift-up** (urcă spre rădăcină).

```c
void insertHeap(Heap* heap, Task task) {
    heap->size++;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
    int index  = heap->size - 1;
    heap->tasks[index] = task;
    // deep copy description dacă e necesar
    int parent = (index - 1) / 2;
    while (index > 0 && heap->tasks[index].priority > heap->tasks[parent].priority) {
        swapTask(&heap->tasks[index], &heap->tasks[parent]);
        index  = parent;
        parent = (index - 1) / 2;
    }
}
```

### deleteFromHeap — O(log N)
Extrage rădăcina (max), pune ultimul element la rădăcină, aplică `heapify`.

```c
Task deleteFromHeap(Heap* heap) {
    Task top = heap->tasks[0];              // salvezi maximul
    heap->tasks[0] = heap->tasks[heap->size - 1];  // ultimul → rădăcină
    heap->size--;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
    heapify(heap, 0);                       // restabilești proprietatea
    return top;
}
```

### buildHeap — O(N)
Construiește heap din array neordonat prin `heapify` bottom-up (mai eficient decât N inserări individuale = O(N log N)).

```c
Heap buildHeap(Task* tasks, int size) {
    Heap heap;
    heap.size   = size;
    heap.tasks  = malloc(size * sizeof(Task));
    for (int i = 0; i < size; i++) {
        heap.tasks[i] = tasks[i];
        // deep copy description dacă e necesar
    }
    for (int i = heap.size / 2 - 1; i >= 0; i--)
        heapify(&heap, i);
    return heap;
}
```

> **De ce `size/2 - 1`?** Jumătatea din dreapta a vectorului sunt **frunze** — nu au copii, heapify pe ele nu face nimic. Pornești de la ultimul nod **non-frunză**.

### deleteByCondition — O(N log N)

```c
void deleteByCondition(Heap* heap, int minPriority) {
    int i = 0;
    while (i < heap->size) {
        if (heap->tasks[i].priority < minPriority) {
            free(heap->tasks[i].description);
            heap->tasks[i] = heap->tasks[heap->size - 1]; // swap cu ultimul
            heap->size--;
            heapify(heap, i);
            // NU i++ — elementul mutat la i trebuie și el verificat
        } else {
            i++;
        }
    }
}
```

## Min-heap

Identic cu max-heap, singurele diferențe:

| Funcție | Max-heap | Min-heap |
|---|---|---|
| `heapify` | caută **LARGEST** cu `>` | caută **SMALLEST** cu `<` |
| `insert` sift-up | `tasks[i] > tasks[parent]` | `tasks[i] < tasks[parent]` |

## Complexitate

| Operație | Complexitate |
|---|---|
| insert | O(log N) |
| deleteFromHeap (extrage max/min) | O(log N) |
| buildHeap | **O(N)** |
| peek (citește max/min) | O(1) |
| deleteByCondition | O(N log N) |
| search arbitrary | O(N) |

## Heap sort

Extrage elementele unul câte unul din max-heap → obții **ordine crescătoare**. Extrage din min-heap → ordine crescătoare direct. Complexitate totală: O(N log N).

---

---

# 7. Lab 08 — BST (Binary Search Tree)

## Concept

Un **BST** este un arbore binar unde:
- tot subarborele **stâng** conține chei **mai mici** decât rădăcina
- tot subarborele **drept** conține chei **mai mari**
- fiecare subarbore este și el un BST (recursiv)

```
BST cu chei: 5, 3, 7, 1, 4, 6, 9

        5
       / \
      3   7
     / \ / \
    1  4 6  9
```

## Structuri

```c
typedef struct TreeNode {
    VideoGame* data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;
```

## Operații

### Insert — O(log N) mediu, O(N) degenerat
```c
void bstInsert(TreeNode** root, VideoGame* game) {
    if (*root == NULL) {
        *root = malloc(sizeof(TreeNode));
        (*root)->data  = game;
        (*root)->left  = (*root)->right = NULL;
        return;
    }
    if (game->gameID < (*root)->data->gameID)
        bstInsert(&(*root)->left, game);
    else if (game->gameID > (*root)->data->gameID)
        bstInsert(&(*root)->right, game);
    // dacă egal: duplicat, nu inserăm
}
```

### Search — O(log N) mediu
```c
TreeNode* bstSearch(TreeNode* root, unsigned int id) {
    if (!root)                   return NULL;
    if (id == root->data->gameID) return root;
    if (id  < root->data->gameID) return bstSearch(root->left, id);
    return                               bstSearch(root->right, id);
}
```

### findMin / findMax
```c
TreeNode* findMin(TreeNode* root) {
    if (!root || !root->left) return root;
    return findMin(root->left);   // tot la stânga = minimul
}
TreeNode* findMax(TreeNode* root) {
    if (!root || !root->right) return root;
    return findMax(root->right);  // tot la dreapta = maximul
}
```

### Delete — 3 cazuri
```c
void deleteNode(TreeNode** root, unsigned int id) {
    if (!*root) return;
    if (id < (*root)->data->gameID) {
        deleteNode(&(*root)->left, id);
    } else if (id > (*root)->data->gameID) {
        deleteNode(&(*root)->right, id);
    } else {
        // Caz 1: frunză
        if (!(*root)->left && !(*root)->right) {
            free((*root)->data); free(*root); *root = NULL;
        }
        // Caz 2a: doar copil drept
        else if (!(*root)->left) {
            TreeNode* del = *root; *root = (*root)->right;
            free(del->data); free(del);
        }
        // Caz 2b: doar copil stâng
        else if (!(*root)->right) {
            TreeNode* del = *root; *root = (*root)->left;
            free(del->data); free(del);
        }
        // Caz 3: doi copii → in-order successor
        else {
            TreeNode* succ = findMin((*root)->right);
            // copiezi datele succesorului în nodul curent
            (*root)->data->gameID = succ->data->gameID;
            // ... deep copy câmpuri char* ...
            // ștergi succesorul din subarborele drept
            deleteNode(&(*root)->right, succ->data->gameID);
        }
    }
}
```

**Vizual ștergere cu doi copii:**
```
Sterg 5:          Succesorul inorder al lui 5 = findMin(dreapta) = 6
        5               6
       / \    →        / \
      3   7           3   7
         /               \
        6                 9
         \
          9
```

## Traversări

```
Inorder   (stânga → rădăcină → dreapta): produce cheile SORTATE CRESCĂTOR
Preorder  (rădăcină → stânga → dreapta): util pentru copiere / serializare arbore
Postorder (stânga → dreapta → rădăcină): util pentru ștergere (eliberezi de jos în sus)
```

## Afișare vizuală (rotit 90°)

```c
void printTree(TreeNode* root, int space) {
    if (root) {
        space += 6;
        printTree(root->right, space);         // dreapta sus
        printf("\n");
        for (int i = 6; i < space; i++) printf(" ");
        printf("[%u]", root->data->gameID);
        printTree(root->left, space);          // stânga jos
    }
}
```

## Complexitate

| Operație | Caz mediu (balansat) | Caz rău (degenerat) |
|---|---|---|
| Search | O(log N) | O(N) |
| Insert | O(log N) | O(N) |
| Delete | O(log N) | O(N) |
| findMin/Max | O(log N) | O(N) |

> BST degenerat: inserezi în ordine sortată → arborele devine o **listă înlănțuită** → toate operațiile O(N). Soluție: AVL.

---

---

# 8. Lab 09 — AVL Tree

## Concept

AVL = BST **auto-balansat**. După fiecare insert/delete, verifică **balance factor** și aplică **rotații** pentru a menține înălțimea O(log N).

## Balance factor (BF)

```
BF(nod) = height(subarbore_drept) - height(subarbore_stâng)

BF valid: -1, 0, +1
BF = -2 → left-heavy  → rotație spre dreapta
BF = +2 → right-heavy → rotație spre stânga
```

```c
int avlHeight(AVLNode* root) {
    if (!root) return 0;
    int l = avlHeight(root->left);
    int r = avlHeight(root->right);
    return 1 + (l > r ? l : r);
}

int avlBalanceFactor(AVLNode* root) {
    if (!root) return 0;
    return avlHeight(root->right) - avlHeight(root->left);
}
```

## Cele 4 cazuri de dezechilibru și rotațiile lor

### Caz LL (BF = -2, BF(stânga) ≤ 0) → Rotație dreapta

```
    z(-2)                y(0)
   /                    / \
  y(-1)      →         x   z
 /
x
```

```c
void avlRotateRight(AVLNode** root) {
    AVLNode* aux   = (*root)->left;
    (*root)->left  = aux->right;
    aux->right     = *root;
    *root          = aux;
}
```

### Caz RR (BF = +2, BF(dreapta) ≥ 0) → Rotație stânga

```
  z(+2)                y(0)
     \                / \
      y(+1)   →      z   x
         \
          x
```

```c
void avlRotateLeft(AVLNode** root) {
    AVLNode* aux   = (*root)->right;
    (*root)->right = aux->left;
    aux->left      = *root;
    *root          = aux;
}
```

### Caz LR (BF = -2, BF(stânga) > 0) → Rotație stânga pe copil + dreapta pe rădăcină

```
  z(-2)        z(-2)         x
 /            /             / \
y(+1)   →   x(-1)   →     y   z
  \         /
   x       y
```

```c
avlRotateLeft(&(*root)->left);
avlRotateRight(root);
```

### Caz RL (BF = +2, BF(dreapta) < 0) → Rotație dreapta pe copil + stânga pe rădăcină

```
z(+2)       z(+2)          x
    \            \         / \
    y(-1)   →    x(+1) → z   y
   /                \
  x                  y
```

```c
avlRotateRight(&(*root)->right);
avlRotateLeft(root);
```

## rebalance — unificată

```c
static void rebalance(AVLNode** root) {
    int bf = avlBalanceFactor(*root);

    if (bf == 2) {                              // right-heavy
        if (avlBalanceFactor((*root)->right) >= 0)
            avlRotateLeft(root);                // RR
        else {
            avlRotateRight(&(*root)->right);
            avlRotateLeft(root);                // RL
        }
    }
    if (bf == -2) {                             // left-heavy
        if (avlBalanceFactor((*root)->left) <= 0)
            avlRotateRight(root);               // LL
        else {
            avlRotateLeft(&(*root)->left);
            avlRotateRight(root);               // LR
        }
    }
}
```

## Insert și Delete

**Diferența față de BST:** un singur apel `rebalance(root)` adăugat la întoarcerea din recursivitate.

```c
void avlInsert(AVLNode** root, Vulnerability* v) {
    if (*root == NULL) {
        // creare nod nou
    } else if (v->id < (*root)->data->id) {
        avlInsert(&(*root)->left, v);
        rebalance(root);              // ← ADĂUGAT față de BST
    } else if (v->id > (*root)->data->id) {
        avlInsert(&(*root)->right, v);
        rebalance(root);              // ← ADĂUGAT față de BST
    }
}

void avlDeleteNode(AVLNode** root, int id) {
    // ... exact ca BST (3 cazuri) ...
    if (*root) rebalance(root);       // ← ADĂUGAT la finalul funcției
}
```

## Export cu function pointer

```c
typedef int (*FilterFunc)(const Vulnerability*);

// Helper recursiv inorder
static void collectMatching(AVLNode* root, FilterFunc filter,
                             Vulnerability*** arr, int* count) {
    if (!root) return;
    collectMatching(root->left, filter, arr, count);
    if (filter(root->data)) {
        (*count)++;
        *arr = realloc(*arr, (*count) * sizeof(Vulnerability*));
        (*arr)[*count - 1] = root->data;
    }
    collectMatching(root->right, filter, arr, count);
}

Vulnerability** exportByCondition(AVLNode* root, FilterFunc filter, int* outCount) {
    *outCount = 0;
    Vulnerability** result = NULL;
    collectMatching(root, filter, &result, outCount);
    return result;                    // apelantul face free(result)
}
```

## Complexitate garantată

| Operație | Complexitate |
|---|---|
| Search | **O(log N)** garantat |
| Insert | **O(log N)** garantat |
| Delete | **O(log N)** garantat |
| Rotație | O(1) |

> **AVL vs BST:** BST poate degenera la O(N). AVL garantează O(log N) prin costul extra al rotațiilor. Rotațiile sunt O(1) — overhead mic.

## BST vs AVL — tabel comparativ

| | BST | AVL |
|---|---|---|
| Struct nod | `TreeNode` | `AVLNode` |
| Prefix funcții | fără prefix | `avl` prefix |
| Insert | recursiv | recursiv + `rebalance` |
| Delete | recursiv | recursiv + `rebalance` |
| Funcții extra | — | `avlHeight`, `avlBalanceFactor`, `avlRotateLeft`, `avlRotateRight`, `rebalance` |
| Complexitate garantată | NU (degenerat = O(N)) | **DA** — O(log N) |

---

---

# 9. Lab 10 — Graf (DFS / BFS)

## Concept

Un **graf** este o mulțime de **noduri** (vârfuri) conectate prin **muchii** (arce).

- **Neorientat:** muchia A-B există în ambele direcții
- **Orientat:** muchia A→B există doar dintr-o direcție

```
Graf neorientat:          Lista de adiacență:
1 -- 2                    1: [2, 3]
|    |         →          2: [1, 4]
3 -- 4 -- 5               3: [1, 4]
                          4: [2, 3, 5]
                          5: [4]
```

## Reprezentare — lista de adiacență

```c
typedef struct AdjNode AdjNode;
typedef struct GraphNode GraphNode;

struct AdjNode {
    GraphNode* target;   // pointer la nodul vecin
    AdjNode*   next;     // următorul vecin
};

struct GraphNode {
    Station*   data;     // datele nodului
    AdjNode*   adj;      // capul listei de adiacență
    GraphNode* next;     // următorul nod din graf (lista de noduri)
};
```

**Vizual:**

```
graph → [GraphNode(1)] → [GraphNode(2)] → [GraphNode(3)] → NULL
              |                 |
         [AdjNode→2]      [AdjNode→1]
              |                 |
         [AdjNode→3]      [AdjNode→4]
              |                 |
             NULL              NULL
```

## Operații de construcție

```c
void insertNode(GraphNode** graph, Station* s) {
    GraphNode* node = malloc(sizeof(GraphNode));
    node->data = s; node->adj = NULL;
    node->next = *graph; *graph = node;   // prepend
}

static void insertAdj(AdjNode** list, GraphNode* target) {
    AdjNode* adj = malloc(sizeof(AdjNode));
    adj->target = target;
    adj->next   = *list; *list = adj;     // prepend
}

void addEdge(GraphNode* graph, int id1, int id2) {
    GraphNode* n1 = findById(graph, id1);
    GraphNode* n2 = findById(graph, id2);
    if (n1 && n2) {
        insertAdj(&n1->adj, n2);   // graf neorientat → ambele direcții
        insertAdj(&n2->adj, n1);
    }
}
```

## DFS — Depth-First Search (parcurgere în adâncime)

**Principiu:** merge cât mai adânc pe un drum înainte să se întoarcă.  
**Structura de date:** **stivă (LIFO)**

```
Graf:  1-2, 1-3, 2-4, 3-4, 4-5
DFS din 1 (cu stiva): 1 → push(2,3) → pop(3) → push(4) → pop(4) → push(5) → ...
Ordine vizitare: 1, 3, 4, 2, 5  (sau 1, 2, 4, 5, 3 — depinde de ordinea din lista adj)
```

```c
void dfs(GraphNode* graph, int startId, int nodeCount) {
    int* visited     = calloc(nodeCount + 1, sizeof(int));
    StackNode* stack = NULL;
    push(&stack, startId);

    while (stack) {
        int id = pop(&stack);
        if (visited[id]) continue;         // nod deja procesat
        visited[id] = 1;
        // procesare nod
        GraphNode* node = findById(graph, id);
        if (node) {
            printStation(node->data);
            AdjNode* adj = node->adj;
            while (adj) {
                if (!visited[adj->target->data->id])
                    push(&stack, adj->target->data->id);
                adj = adj->next;
            }
        }
    }
    free(visited);
}
```

## BFS — Breadth-First Search (parcurgere în lățime)

**Principiu:** explorează toți vecinii unui nod înainte să meargă mai adânc.  
**Structura de date:** **coadă (FIFO)**

```
BFS din 1:
  Nivel 0: {1}
  Nivel 1: {2, 3}   ← toți vecinii lui 1
  Nivel 2: {4}      ← vecini nevizitați ai lui 2 și 3
  Nivel 3: {5}
Ordine: 1, 2, 3, 4, 5
```

```c
void bfs(GraphNode* graph, int startId, int nodeCount) {
    int* visited = calloc(nodeCount + 1, sizeof(int));
    Queue q      = {NULL, NULL};
    visited[startId] = 1;    // marchezi la ENQUEUE, nu la dequeue
    enqueue(&q, startId);

    while (q.front) {
        int id = dequeue(&q);
        GraphNode* node = findById(graph, id);
        if (node) {
            printStation(node->data);
            AdjNode* adj = node->adj;
            while (adj) {
                int adjId = adj->target->data->id;
                if (!visited[adjId]) {
                    visited[adjId] = 1;   // marchezi la enqueue
                    enqueue(&q, adjId);
                }
                adj = adj->next;
            }
        }
    }
    free(visited);
}
```

> **Diferența crucială BFS vs DFS:**
> - BFS marchează `visited` când **adaugă în coadă** → evită duplicatele în coadă
> - DFS marchează `visited` când **scoate din stivă** (cu `if (visited[id]) continue`) → un nod poate fi pe stivă de mai multe ori, dar e procesat o singură dată

## Stivă și Coadă implementate cu liste înlănțuite

```c
// Stivă (LIFO)
typedef struct StackNode { int id; struct StackNode* next; } StackNode;

void push(StackNode** top, int id) {
    StackNode* n = malloc(sizeof(StackNode));
    n->id = id; n->next = *top; *top = n;
}
int pop(StackNode** top) {
    StackNode* n = *top; int id = n->id;
    *top = n->next; free(n); return id;
}

// Coadă (FIFO)
typedef struct QueueNode { int id; struct QueueNode* next; } QueueNode;
typedef struct { QueueNode* front; QueueNode* back; } Queue;

void enqueue(Queue* q, int id) {
    QueueNode* n = malloc(sizeof(QueueNode));
    n->id = id; n->next = NULL;
    if (q->back) q->back->next = n; else q->front = n;
    q->back = n;
}
int dequeue(Queue* q) {
    QueueNode* n = q->front; int id = n->id;
    q->front = n->next; if (!q->front) q->back = NULL;
    free(n); return id;
}
```

## DFS vs BFS — comparație

| | DFS | BFS |
|---|---|---|
| Structura internă | Stivă (LIFO) | Coadă (FIFO) |
| Ordine explorare | Adâncime (merge cât mai departe) | Lățime (nivel cu nivel) |
| Cel mai scurt drum | NU garantat | **DA** (grafuri neponderate) |
| Memorie | O(adâncime) | O(lățime nivel maxim) |
| Utilitate | Detectare cicluri, componente conexe | Cel mai scurt drum, nivel BFS |

## Complexitate

| Operație | Complexitate |
|---|---|
| DFS / BFS | **O(V + E)** — V noduri + E muchii |
| `insertNode` | O(1) |
| `addEdge` | O(V) — `findById` e O(V) |
| `findById` | O(V) |

## Free graf

```c
void freeGraph(GraphNode* graph) {
    while (graph) {
        AdjNode* adj = graph->adj;
        while (adj) {
            AdjNode* nextAdj = adj->next;
            free(adj);               // doar AdjNode, nu data (pointează la alt GraphNode)
            adj = nextAdj;
        }
        free(graph->data->name);     // câmpurile char* ale Station
        free(graph->data->line);
        free(graph->data);           // Station struct
        GraphNode* next = graph->next;
        free(graph);                 // GraphNode
        graph = next;
    }
}
```

---

---

# 10. Tabel comparativ final

| Structură | Insert | Search | Delete | Ordonat? | Cazul de utilizare |
|---|---|---|---|---|---|
| **Lista simplă** | O(1) cap / O(N) coadă | O(N) | O(N) | Nu | Inserări/ștergeri frecvente la capete |
| **Lista dublă** | O(1) cap/coadă | O(N) | O(1) cu pointer | Nu | Ștergere eficientă cu pointer la nod |
| **Hash Table** | O(1) amortizat | O(1) amortizat | O(1) amortizat | Nu | Lookup rapid după cheie |
| **Heap (max/min)** | O(log N) | O(N) | O(log N) max/min | Parțial | Priority queue — extrage max/min eficient |
| **BST** | O(log N) mediu | O(log N) mediu | O(log N) mediu | **Da** (inorder) | Date sortate + căutare eficientă |
| **AVL** | O(log N) garantat | O(log N) garantat | O(log N) garantat | **Da** (inorder) | BST garantat balansat |
| **Graf** | O(1) nod | O(V) | O(V+E) | Nu | Relații, rețele, hărți |

---

## Rezumat — Ce structură pentru ce problemă?

```
Vrei să extragi mereu maximul/minimul?
    → Max-heap / Min-heap (priority queue)

Vrei să cauți rapid după o cheie (nu te interesează ordinea)?
    → Hash Table

Vrei elemente sortate + căutare/insert/delete eficiente?
    → AVL (garantat) sau BST (dacă datele nu vin sortate)

Vrei inserări/ștergeri frecvente la capete?
    → Lista înlănțuită

Vrei să modelezi relații între entități (rețele, dependențe)?
    → Graf + DFS/BFS

Vrei cel mai scurt drum (muchii neponderate)?
    → BFS
```

---

## Pattern-uri de cod de memorat

### 1. Node** pattern
```c
// Orice funcție care poate schimba capul/rădăcina → primește **
void insert(Node** list, ...) { *list = newNode; }
insert(&head, ...);
```

### 2. Delete din listă cu pointer la pointer
```c
Node** cur = &head;
while (*cur) {
    if (condition(*cur)) {
        Node* del = *cur; *cur = (*cur)->next; free(del);
    } else { cur = &(*cur)->next; }
}
```

### 3. Deep copy string
```c
dest->name = malloc(strlen(src->name) + 1);
strcpy(dest->name, src->name);
```

### 4. Free în ordine corectă
```c
// De la interior spre exterior
free(node->data->name);       // câmpuri char*
free(node->data);             // struct-ul
free(node);                   // nodul
```

### 5. Heap index formulas
```c
parent(i)      = (i - 1) / 2
left_child(i)  = 2*i + 1
right_child(i) = 2*i + 2
```

### 6. AVL rebalance — când se apelează
```c
avlInsert(&(*root)->left, v);
rebalance(root);              // la întoarcerea din FIECARE apel recursiv
```

### 7. BFS — marchezi visited la enqueue
```c
visited[start] = 1; enqueue(&q, start);
while (q.front) {
    int id = dequeue(&q);
    // procesezi id
    // pentru fiecare vecin nevizitat: visited[vecin]=1; enqueue
}
```
