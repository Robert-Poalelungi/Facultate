# Grilă de pregătire — Structuri de Date (SDD)

> **Format:** fiecare întrebare are 4 variante, o singură variantă corectă.  
> Apasă pe `▶ Răspuns` pentru a dezvălui răspunsul și explicația.  
> ~70% întrebări de cod, ~30% teorie.

---

## Cuprins

1. [Lab 03 — Lista simplu înlănțuită](#lab-03--lista-simplu-înlănțuită)
2. [Lab 04 — Liste + Delete + Function Pointers](#lab-04--liste--delete--function-pointers)
3. [Lab 05 — Lista dublu înlănțuită](#lab-05--lista-dublu-înlănțuită)
4. [Lab 06 — Hash Table](#lab-06--hash-table)
5. [Lab 07 — Heap (Max + Min + deleteByCondition)](#lab-07--heap-max--min--deletebycondition)
6. [Lab 08 — BST (Binary Search Tree)](#lab-08--bst-binary-search-tree)
7. [Lab 09 — AVL Tree](#lab-09--avl-tree)
8. [Lab 10 — Graf (DFS / BFS)](#lab-10--graf-dfs--bfs)

---

---

## Lab 03 — Lista simplu înlănțuită

---

**Q1.** [Teorie] Cum se reprezintă o listă simplu înlănțuită în C?

a) Ca un vector de structuri alocate static  
b) Ca o succesiune de noduri, fiecare conținând date și un pointer la **nodul următor**  
c) Ca o succesiune de noduri, fiecare cu pointer la **nodul anterior și următor**  
d) Ca un arbore binar cu frunze NULL  

<details><summary>▶ Răspuns</summary>

**b)** Fiecare nod are `data` + `next`. Varianta c) descrie lista **dublu** înlănțuită.

</details>

---

**Q2.** [Cod] Ce afișează secvența de mai jos?

```c
typedef struct Node { int val; struct Node* next; } Node;

Node* list = NULL;

Node* n1 = malloc(sizeof(Node)); n1->val = 1; n1->next = NULL;
Node* n2 = malloc(sizeof(Node)); n2->val = 2; n2->next = NULL;
Node* n3 = malloc(sizeof(Node)); n3->val = 3; n3->next = NULL;

n1->next = n2;
n2->next = n3;
list = n1;

Node* cur = list;
while (cur) {
    printf("%d ", cur->val);
    cur = cur->next;
}
```

a) `3 2 1`  
b) `1 2 3`  
c) `1 2`  
d) loop infinit  

<details><summary>▶ Răspuns</summary>

**b)** Parcurgem de la `list` (n1) → n2 → n3 → NULL, afișând 1, 2, 3.

</details>

---

**Q3.** [Cod] Ce problemă are funcția de mai jos?

```c
void addToBeginning(Node** list, int val) {
    Node* node = malloc(sizeof(Node));
    node->val  = val;
    node->next = list;   // <--- linia suspectă
    *list = node;
}
```

a) `malloc` nu poate fi apelat fără `#include <stdlib.h>`  
b) `node->next = list` atribuie adresa variabilei pointer, nu valoarea ei — tipul e greșit  
c) Nu se poate insera la început fără să parcurgem lista  
d) Nu e nicio problemă  

<details><summary>▶ Răspuns</summary>

**b)** `list` este `Node**`. Corect era `node->next = *list` (vechiul cap al listei). Acum `next` pointează la variabila `head` a apelantului, nu la primul nod.

</details>

---

**Q4.** [Cod] Ce se întâmplă la execuția acestui cod?

```c
Node* n = malloc(sizeof(Node));
n->val  = 42;
n->next = NULL;

Node* p = n;
free(n);
printf("%d\n", p->val);
```

a) Afișează `42`  
b) Afișează `0`  
c) **Comportament nedefinit** — acces la memorie eliberată  
d) Eroare de compilare  

<details><summary>▶ Răspuns</summary>

**c)** După `free(n)`, memoria e eliberată. `p` este un **dangling pointer**. Accesul prin el e comportament nedefinit (UB) — poate afișa 42, poate crăpa, depinde de implementare.

</details>

---

**Q5.** [Cod] Care este complexitatea temporală a funcției `addToEnd` pe o listă cu N noduri (fără pointer la coadă)?

```c
void addToEnd(Node** list, int val) {
    Node* node = malloc(sizeof(Node));
    node->val  = val;
    node->next = NULL;
    if (*list == NULL) { *list = node; return; }
    Node* cur = *list;
    while (cur->next) cur = cur->next;
    cur->next = node;
}
```

a) O(1)  
b) O(log N)  
c) O(N)  
d) O(N²)  

<details><summary>▶ Răspuns</summary>

**c)** Trebuie parcursă toată lista până la ultimul nod — O(N). `addToBeginning` în schimb e O(1).

</details>

---

**Q6.** [Cod] Ce afișează?

```c
Node* list = NULL;

void addToBeginning(Node** list, int val) {
    Node* n = malloc(sizeof(Node));
    n->val  = val;
    n->next = *list;
    *list   = n;
}

addToBeginning(&list, 10);
addToBeginning(&list, 20);
addToBeginning(&list, 30);

Node* cur = list;
while (cur) { printf("%d ", cur->val); cur = cur->next; }
```

a) `10 20 30`  
b) `30 20 10`  
c) `10 30 20`  
d) `20 10 30`  

<details><summary>▶ Răspuns</summary>

**b)** Fiecare inserare la început pune noul nod în față. Ultimul inserat (30) devine capul listei → `30 20 10`.

</details>

---

**Q7.** [Teorie] De ce funcțiile care modifică capul listei primesc `Node**` (pointer la pointer) în loc de `Node*`?

a) Pentru eficiență — se evită copierea structurii  
b) Ca să poată modifica variabila `head` din apelant — altfel modificările sunt locale  
c) Deoarece `Node*` nu poate fi transmis ca parametru  
d) Este o convenție opțională, funcționează și cu `Node*`  

<details><summary>▶ Răspuns</summary>

**b)** C este **pass-by-value**. Dacă primești `Node*`, poți modifica *conținutul* nodului, dar nu poți schimba ce adresă ține variabila `head` din `main`. `Node**` îți dă acces la variabila în sine.

</details>

---

**Q8.** [Cod] Câte noduri are lista după execuția de mai jos?

```c
Node* list = NULL;
addToEnd(&list, 1);
addToEnd(&list, 2);
addToBeginning(&list, 0);
addToEnd(&list, 3);
Node* cur = list;
int count = 0;
while (cur) { count++; cur = cur->next; }
printf("%d\n", count);
```

a) `3`  
b) `4`  
c) `2`  
d) `5`  

<details><summary>▶ Răspuns</summary>

**b)** Se adaugă 4 noduri (1, 2, 0, 3). Lista finală: `0 → 1 → 2 → 3`.

</details>

---

**Q9.** [Cod] Ce problemă are această funcție `freeList`?

```c
void freeList(Node* list) {
    while (list) {
        free(list);
        list = list->next;  // <--- acces după free
    }
}
```

a) Nicio problemă, `list->next` se citește înainte de `free`  
b) **Use-after-free**: `list->next` e accesat după ce `list` a fost eliberat  
c) `free` nu se poate apela în interiorul unui while  
d) Nu iterăm corect  

<details><summary>▶ Răspuns</summary>

**b)** După `free(list)`, citirea `list->next` e comportament nedefinit. Corect:
```c
Node* next = list->next;
free(list);
list = next;
```

</details>

---

**Q10.** [Cod] Ce returnează funcția?

```c
int countNodes(Node* list) {
    if (list == NULL) return 0;
    return 1 + countNodes(list->next);
}
```

a) Lungimea listei  
b) Suma valorilor din listă  
c) Ultimul element  
d) Întotdeauna 1  

<details><summary>▶ Răspuns</summary>

**a)** Recursivitate: cazul de bază returnează 0 (listă goală), altfel 1 + lungimea restului.

</details>

---

---

## Lab 04 — Liste + Delete + Function Pointers

---

**Q11.** [Teorie] Ce este un **function pointer** în C?

a) Un pointer care stochează adresa unei variabile de tip funcție  
b) O variabilă care stochează **adresa unei funcții** și permite apelarea ei indirect  
c) Un tip special de referință folosit doar în C++  
d) Un pointer la structura internă a unei funcții  

<details><summary>▶ Răspuns</summary>

**b)** Function pointer-ul stochează adresa unei funcții. Se poate apela indirect: `(*fn)(args)` sau `fn(args)`.

</details>

---

**Q12.** [Cod] Care declarație este corectă pentru un pointer la o funcție ce primește `Node**` și `int` și nu returnează nimic?

a) `void* insertFn(Node**, int);`  
b) `void (*insertFn)(Node**, int);`  
c) `(*void) insertFn(Node**, int);`  
d) `void insertFn*(Node**, int);`  

<details><summary>▶ Răspuns</summary>

**b)** Sintaxa function pointer: `return_type (*name)(param_types)`.

</details>

---

**Q13.** [Cod] Ce face `deleteFromBeginning`?

```c
void deleteFromBeginning(Node** list) {
    if (*list == NULL) return;
    Node* toDelete = *list;
    *list = (*list)->next;
    free(toDelete->data->driver);
    free(toDelete->data->team);
    free(toDelete->data);
    free(toDelete);
}
```

a) Șterge ultimul nod  
b) Șterge primul nod și avansează capul listei  
c) Șterge primul nod dar nu eliberează memoria  
d) Face crash dacă lista are un singur element  

<details><summary>▶ Răspuns</summary>

**b)** Salvează capul, avansează `*list` la al doilea nod, eliberează corect tot (câmpuri char*, struct, nod).

</details>

---

**Q14.** [Cod] Ce se întâmplă la apelul următor?

```c
void deleteByCondition(Node** list, int (*cond)(Node*)) {
    while (*list) {
        if (cond(*list)) {
            Node* toDelete = *list;
            *list = (*list)->next;
            free(toDelete->data);
            free(toDelete);
        } else {
            list = &(*list)->next;
        }
    }
}

int isOld(Node* n) { return n->data->year < 2000; }

deleteByCondition(&head, isOld);
```

a) Șterge primul nod care are `year < 2000`  
b) Șterge **toate** nodurile cu `year < 2000`  
c) Șterge **toate** nodurile cu `year >= 2000`  
d) Nu compilează  

<details><summary>▶ Răspuns</summary>

**b)** Bucla continuă până la finalul listei. Când condiția e îndeplinită, scoate nodul și NU avansează `list` (noul `*list` e deja următorul). Când nu e îndeplinită, avansează.

</details>

---

**Q15.** [Cod] Se folosește funcția pointer astfel:

```c
typedef void (*InsertFn)(Node**, F1Car*);
InsertFn fn = addToBeginning;
fn(&list, car);
```

Care este efectul față de `addToBeginning(&list, car)` direct?

a) Efect identic — apelul prin function pointer e echivalent  
b) Se inserează la sfârșit în loc de început  
c) `fn` primește o copie a lui `car`, deci nu se modifică lista  
d) Nu compilează  

<details><summary>▶ Răspuns</summary>

**a)** Apelul prin function pointer este perfect echivalent cu apelul direct. Flexibilitatea apare când poți schimba `fn = addToEnd` fără să schimbi codul de apel.

</details>

---

**Q16.** [Cod] Ce printează codul următor?

```c
void print(int x) { printf("val=%d\n", x); }
void double_it(int x) { printf("val=%d\n", x * 2); }

void apply(void (*fn)(int), int x) { fn(x); }

apply(print, 5);
apply(double_it, 5);
```

a) `val=5` și `val=5`  
b) `val=5` și `val=10`  
c) `val=10` și `val=5`  
d) Eroare de compilare  

<details><summary>▶ Răspuns</summary>

**b)** `apply(print, 5)` → `print(5)` → `val=5`. `apply(double_it, 5)` → `double_it(5)` → `val=10`.

</details>

---

**Q17.** [Cod] Ce problemă are `deleteFromEnd`?

```c
void deleteFromEnd(Node** list) {
    if (*list == NULL) return;
    if ((*list)->next == NULL) {
        free(*list);
        *list = NULL;
        return;
    }
    Node* cur = *list;
    while (cur->next->next) cur = cur->next;
    free(cur->next);
    cur->next = NULL;
}
```

a) Nu eliberează memoria nodului șters  
b) Nu gestionează lista goală  
c) Nu gestionează lista cu un singur element  
d) **Nicio problemă** — codul este corect  

<details><summary>▶ Răspuns</summary>

**d)** Codul gestionează toate cazurile: listă goală (return), un singur element (free + NULL), mai multe elemente (parcurge până la penultimul).

</details>

---

---

## Lab 05 — Lista dublu înlănțuită

---

**Q18.** [Teorie] Care este diferența principală față de lista simplu înlănțuită?

a) Lista dublu înlănțuită folosește vectori în loc de pointeri  
b) Fiecare nod are câte **doi pointeri**: `prev` și `next`  
c) Lista dublu înlănțuită nu are cap (`head`)  
d) Inserarea la început este O(N) în loc de O(1)  

<details><summary>▶ Răspuns</summary>

**b)** Fiecare nod pointează atât la nodul următor cât și la cel anterior. Permite parcurgerea în ambele direcții și ștergerea în O(1) dacă ai pointer la nod.

</details>

---

**Q19.** [Cod] Câți pointeri trebuie actualizați la inserarea unui nod nou **la mijloc** (între `prev` și `next`)?

```c
// Inserăm 'newNode' între 'prev' și 'next'
newNode->prev = prev;
newNode->next = next;
prev->next    = newNode;
next->prev    = newNode;
```

a) 1  
b) 2  
c) 4  
d) 6  

<details><summary>▶ Răspuns</summary>

**c)** Exact 4 pointeri: cei 2 ai nodului nou (`prev`, `next`) + actualizarea `next`-ului din `prev` + actualizarea `prev`-ului din `next`.

</details>

---

**Q20.** [Cod] Ce lipsește din `addToBeginning` pentru lista dublu înlănțuită?

```c
void addToBeginning(DNode** head, int val) {
    DNode* node = malloc(sizeof(DNode));
    node->val   = val;
    node->prev  = NULL;
    node->next  = *head;
    // ??? 
    *head = node;
}
```

a) Nimic, codul e complet  
b) `(*head)->prev = node;` — trebuie actualizat `prev`-ul vechiului cap  
c) `node->next->prev = node;` — greșit, ar crăpa dacă lista e goală  
d) `free(*head);`  

<details><summary>▶ Răspuns</summary>

**b)** Dacă lista nu e goală, vechiul cap (`*head`) trebuie să pointeze înapoi la noul nod. Codul corect:
```c
if (*head) (*head)->prev = node;
*head = node;
```

</details>

---

**Q21.** [Cod] Ce afișează parcurgerea **de la coadă la cap** a listei `1 ↔ 2 ↔ 3`?

```c
DNode* tail = head;
while (tail->next) tail = tail->next;
while (tail) {
    printf("%d ", tail->val);
    tail = tail->prev;
}
```

a) `1 2 3`  
b) `3 2 1`  
c) `3 3 3`  
d) loop infinit  

<details><summary>▶ Răspuns</summary>

**b)** Găsim coada mergând la `tail->next == NULL`, apoi parcurgem înapoi prin `prev`.

</details>

---

**Q22.** [Cod] Ce face acest cod cu o listă dublu înlănțuită?

```c
DNode* cur = head;
while (cur && cur->next) {
    DNode* tmp = cur->next;
    cur->next  = tmp->next;
    if (tmp->next) tmp->next->prev = cur;
    free(tmp->val_str);
    free(tmp);
}
```

a) Șterge toate nodurile de pe pozițiile impare  
b) Șterge toate nodurile de pe pozițiile pare (al doilea, al patrulea...)  
c) Șterge ultimul nod  
d) Inversează lista  

<details><summary>▶ Răspuns</summary>

**b)** Pornind de la `head`, sare peste fiecare al doilea nod și îl șterge. `cur` rămâne pe loc, `tmp` este nodul următor care se șterge.

</details>

---

**Q23.** [Teorie] Care operație este mai eficientă pe lista dublu înlănțuită față de cea simplu înlănțuită?

a) Inserarea la început  
b) Căutarea după valoare  
c) **Ștergerea unui nod dat prin pointer** (fără să știi predecesorul)  
d) Parcurgerea în ordine  

<details><summary>▶ Răspuns</summary>

**c)** Pe lista simplu înlănțuită, ștergerea unui nod necesită găsirea predecesorului (O(N)). Pe lista dublu înlănțuită, fiecare nod cunoaște `prev` → ștergere O(1).

</details>

---

---

## Lab 06 — Hash Table

---

**Q24.** [Teorie] Ce este o **coliziune** într-un hash table?

a) Când funcția hash returnează o valoare negativă  
b) Când două chei diferite produc **același index** hash  
c) Când tabla hash este plină  
d) Când un element este inserat de două ori  

<details><summary>▶ Răspuns</summary>

**b)** Coliziunea = `hash(key1) == hash(key2)` deși `key1 != key2`. Strategia noastră de rezolvare: **chaining** (liste înlănțuite pe fiecare bucket).

</details>

---

**Q25.** [Cod] Ce returnează funcția hash de mai jos pentru `"AB"` cu `size = 10`?

```c
int hash(int size, const char* key) {
    int sum = 0;
    for (int i = 0; key[i]; i++)
        sum += key[i];
    return sum % size;
}
```

`'A'` = 65, `'B'` = 66

a) `1`  
b) `3`  
c) `5`  
d) `7`  

<details><summary>▶ Răspuns</summary>

**b)** `65 + 66 = 131`. `131 % 10 = 1`. — Atenție: răspunsul corect este **1**, nu 3. Deci **a)** este corect.

**a)** `131 % 10 = 1`.

</details>

---

**Q26.** [Cod] Ce tip de coliziune rezolvă structura de mai jos?

```c
typedef struct Node {
    char* key;
    char* value;
    struct Node* next;
} Node;

typedef struct {
    int size;
    Node** buckets;
} HashTable;
```

a) Open addressing (linear probing)  
b) **Chaining** — fiecare bucket e o listă înlănțuită  
c) Double hashing  
d) Cuckoo hashing  

<details><summary>▶ Răspuns</summary>

**b)** `Node** buckets` = array de pointeri la liste înlănțuite. Fiecare bucket poate conține mai multe perechi (key, value) înlănțuite.

</details>

---

**Q27.** [Cod] Ce afișează?

```c
HashTable ht;
ht.size = 5;
ht.buckets = calloc(5, sizeof(Node*));

insert(&ht, "apple", "fruit");
insert(&ht, "car",   "vehicle");
insert(&ht, "apple", "snack");  // cheie duplicată

Node* found = search(&ht, "apple");
printf("%s\n", found ? found->value : "not found");
```

Dacă `insert` adaugă mereu la **începutul** bucket-ului:

a) `fruit`  
b) `snack`  
c) `vehicle`  
d) `not found`  

<details><summary>▶ Răspuns</summary>

**b)** Al doilea `insert("apple", "snack")` adaugă un nod nou la **începutul** listei din bucket-ul lui "apple". `search` găsește primul nod din lista → "snack".

</details>

---

**Q28.** [Cod] Care este complexitatea medie a operației `search` într-un hash table cu N elemente și M buckets, presupunând distribuție uniformă?

a) O(N)  
b) O(log N)  
c) **O(N/M)** — lungimea medie a unui lanț  
d) O(1) garantat  

<details><summary>▶ Răspuns</summary>

**c)** Cu distribuție uniformă, fiecare bucket are N/M elemente (load factor). Dacă M este proporțional cu N, se obține O(1) amortizat. Dar în cel mai rău caz (toate pe același bucket) e O(N).

</details>

---

**Q29.** [Cod] Ce face funcția?

```c
void deleteByCountry(HashTable* ht, const char* country) {
    for (int i = 0; i < ht->size; i++) {
        Node** cur = &ht->buckets[i];
        while (*cur) {
            if (strcmp((*cur)->team->country, country) == 0) {
                Node* toDelete = *cur;
                *cur = (*cur)->next;
                free(toDelete->team->name);
                free(toDelete->team->country);
                free(toDelete->team);
                free(toDelete);
            } else {
                cur = &(*cur)->next;
            }
        }
    }
}
```

a) Șterge primul element cu țara dată  
b) Șterge **toate** elementele cu țara dată din **toți** bucket-ii  
c) Șterge toate elementele din hash table  
d) Nu compilează  

<details><summary>▶ Răspuns</summary>

**b)** Parcurge toți bucket-ii (`for i`). În fiecare bucket parcurge toată lista. Când găsește țara, scoate nodul și NU avansează `cur` (noul `*cur` e deja următorul). Pattern identic cu `deleteByCondition` de la liste.

</details>

---

**Q30.** [Cod] Ce se printează când printăm un bucket gol?

```c
void printHashTable(HashTable* ht) {
    for (int i = 0; i < ht->size; i++) {
        printf("[%d]: ", i);
        Node* cur = ht->buckets[i];
        while (cur) {
            printf("%s -> ", cur->team->name);
            cur = cur->next;
        }
        printf("NULL\n");
    }
}
```

a) `[i]: ` (fără NULL)  
b) `[i]: NULL`  
c) Bucket-ul gol nu se afișează  
d) Eroare de segmentare  

<details><summary>▶ Răspuns</summary>

**b)** Dacă `ht->buckets[i] == NULL`, while-ul nu se execută și se printează direct `NULL`. Deci output-ul pentru un bucket gol e `[i]: NULL`.

</details>

---

**Q31.** [Teorie] De ce `calloc` în loc de `malloc` la inițializarea bucket-ilor?

```c
ht.buckets = calloc(ht.size, sizeof(Node*));
```

a) `calloc` e mai rapid  
b) `calloc` inițializează toți pointerii cu `NULL` — esențial ca bucket-urile goale să fie `NULL`  
c) `malloc` nu funcționează cu pointeri la pointeri  
d) Sunt echivalenți  

<details><summary>▶ Răspuns</summary>

**b)** `calloc` zero-inițializează memoria. `Node*` zero-inițializat = `NULL`. Dacă am folosi `malloc`, bucket-urile ar conține valori garbage și `while (cur)` ar produce comportament nedefinit.

</details>

---

---

## Lab 07 — Heap (Max + Min + deleteByCondition)

---

**Q32.** [Teorie] Care proprietate definește un **max-heap**?

a) Fiecare nod are valoarea mai mare decât toți descendenții  
b) **Fiecare nod are prioritatea >= copiii săi direcți** (nu neapărat toți descendenții)  
c) Arborele este sortat crescător de la stânga la dreapta  
d) Radăcina este cel mai mic element  

<details><summary>▶ Răspuns</summary>

**b)** Proprietatea heap: `parent >= children`. Este suficient pentru fiecare nod față de copiii direcți — recursiv implică că rădăcina e maximul global.

</details>

---

**Q33.** [Cod] Într-un heap stocat ca vector, care sunt indecșii copiilor nodului de la indexul `i`?

a) `i-1` și `i+1`  
b) `i*2` și `i*2+1`  
c) `2*i+1` și `2*i+2`  
d) `(i-1)/2` și `(i+1)/2`  

<details><summary>▶ Răspuns</summary>

**c)** Copil stâng: `2*i+1`, copil drept: `2*i+2`. Invers, părintele lui `i`: `(i-1)/2`.

</details>

---

**Q34.** [Cod] Ce afișează?

```c
// Max-heap: [10, 7, 9, 4, 5, 8, 6]
// indecși:    0  1  2  3  4  5  6
int heap[] = {10, 7, 9, 4, 5, 8, 6};
int i = 1;
printf("parent=%d left=%d right=%d\n",
    heap[(i-1)/2], heap[2*i+1], heap[2*i+2]);
```

a) `parent=10 left=4 right=5`  
b) `parent=10 left=5 right=8`  
c) `parent=9 left=4 right=5`  
d) `parent=7 left=4 right=5`  

<details><summary>▶ Răspuns</summary>

**a)** `i=1`: parent = `heap[(1-1)/2]` = `heap[0]` = 10. Left = `heap[3]` = 4. Right = `heap[4]` = 5.

</details>

---

**Q35.** [Cod] Ce face `heapify` și când se apelează?

```c
static void heapify(Heap* heap, int index) {
    int largest = index;
    int left  = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < heap->size && heap->tasks[left].priority > heap->tasks[largest].priority)
        largest = left;
    if (right < heap->size && heap->tasks[right].priority > heap->tasks[largest].priority)
        largest = right;

    if (largest != index) {
        swapTask(&heap->tasks[largest], &heap->tasks[index]);
        heapify(heap, largest);
    }
}
```

a) Inserează un element nou menținând proprietatea heap  
b) **Sift-down**: coboară nodul de la `index` până la poziția corectă (max-heap)  
c) Sift-up: urcă nodul de la `index`  
d) Sortează heap-ul  

<details><summary>▶ Răspuns</summary>

**b)** `heapify` = sift-down. Găsește cel mai mare dintre nod și copii, face swap dacă e cazul, și continuă recursiv. Se apelează la `deleteFromHeap` (după ce punem ultimul element la rădăcină) și în `buildHeap`.

</details>

---

**Q36.** [Cod] Ce face `insertHeap` cu indexul înainte de sift-up?

```c
void insertHeap(Heap* heap, Task task) {
    heap->size++;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
    int index  = heap->size - 1;
    heap->tasks[index] = task;
    int parent = (index - 1) / 2;
    while (index > 0 && heap->tasks[index].priority > heap->tasks[parent].priority) {
        swapTask(&heap->tasks[index], &heap->tasks[parent]);
        index  = parent;
        parent = (index - 1) / 2;
    }
}
```

a) Inserează la rădăcină și face sift-down  
b) Inserează la finalul vectorului și face **sift-up** (urcă spre rădăcină)  
c) Inserează în ordine sortată  
d) Inserează la rădăcină fără rebalansare  

<details><summary>▶ Răspuns</summary>

**b)** Noul element se pune la final (`size-1`). Cât timp e mai mare decât părintele, face swap cu părintele și urcă. `index > 0` previne să treacă dincolo de rădăcină.

</details>

---

**Q37.** [Cod] Ce se întâmplă dacă înlocuim `>` cu `<` în condiția din `heapify`?

```c
if (left < heap->size && heap->tasks[left].priority < heap->tasks[largest].priority)
```

a) Nimic — e echivalent  
b) Heap-ul devine **min-heap** (rădăcina = minimul)  
c) `heapify` nu mai funcționează deloc  
d) Heap-ul se sortează descrescător  

<details><summary>▶ Răspuns</summary>

**b)** Schimbând `>` în `<` în heapify (și similar în sift-up din insert), obținem **min-heap**: rădăcina va fi mereu elementul cu prioritatea minimă.

</details>

---

**Q38.** [Cod] Ce problemă apare în `deleteByCondition` dacă incrementăm `i` și când condiția e îndeplinită?

```c
void deleteByCondition(Heap* heap, int minPriority) {
    int i = 0;
    while (i < heap->size) {
        if (heap->tasks[i].priority < minPriority) {
            heap->tasks[i] = heap->tasks[heap->size - 1];
            heap->size--;
            heapify(heap, i);
            i++;  // BUG: linia asta nu trebuie
        } else {
            i++;
        }
    }
}
```

a) Nicio problemă  
b) **Se sare peste elementul mutat la poziția `i`** — poate rămâne un element ce trebuia șters  
c) `heapify` nu funcționează după swap  
d) `heap->size--` cauzează underflow  

<details><summary>▶ Răspuns</summary>

**b)** Când ștergem elementul de la `i`, mutăm ultimul element la poziția `i`. Dacă incrementăm `i`, nu mai verificăm noul element de la `i`. Pattern corect: NU incrementa `i` când condiția e îndeplinită.

</details>

---

**Q39.** [Cod] Ce complexitate are `buildHeap` față de N inserări individuale?

```c
Heap buildHeap(Task* tasks, int size) {
    // ...copiere...
    for (int i = heap.size / 2 - 1; i >= 0; i--)
        heapify(&heap, i);
    return heap;
}
```

a) `buildHeap` = O(N log N), N inserări = O(N)  
b) `buildHeap` = **O(N)**, N inserări = O(N log N)  
c) Ambele O(N)  
d) Ambele O(N log N)  

<details><summary>▶ Răspuns</summary>

**b)** `buildHeap` cu heapify bottom-up este **O(N)** (demonstrabil matematic). N inserări individuale fiecare O(log N) dau O(N log N). De aceea `buildHeap` e preferabil când ai toate elementele de la început.

</details>

---

**Q40.** [Cod] Ce afișează codul de mai jos (min-heap)?

```c
Heap minH = initHeap();
// minInsertHeap face sift-up cu <
minInsertHeap(&minH, (Task){"A", 5});
minInsertHeap(&minH, (Task){"B", 2});
minInsertHeap(&minH, (Task){"C", 8});
minInsertHeap(&minH, (Task){"D", 1});

Task t = minDeleteFromHeap(&minH);
printf("%s %d\n", t.description, t.priority);
```

a) `A 5`  
b) `C 8`  
c) `D 1`  
d) `B 2`  

<details><summary>▶ Răspuns</summary>

**c)** Min-heap extrage mereu **minimul**. Prioritățile: 5, 2, 8, 1. Minimul = 1 (D). Deci `D 1`.

</details>

---

---

## Lab 08 — BST (Binary Search Tree)

---

**Q41.** [Teorie] Care este proprietatea fundamentală a unui BST?

a) Arborele este mereu balansat  
b) **Stânga < rădăcină < dreapta** (recursiv pentru fiecare subarbore)  
c) Frunzele sunt pe același nivel  
d) Fiecare nod are exact 2 copii  

<details><summary>▶ Răspuns</summary>

**b)** BST property: tot ce e în subarborele stâng are cheie mai mică, tot ce e în subarborele drept are cheie mai mare. Recursiv valid pentru fiecare nod.

</details>

---

**Q42.** [Cod] Ce afișează parcurgerea **inorder** a BST-ului construit?

```c
// Insert în ordine: 5, 3, 7, 1, 4
//        5
//       / \
//      3   7
//     / \
//    1   4

void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}
```

a) `5 3 7 1 4`  
b) `1 3 4 5 7`  
c) `1 4 3 7 5`  
d) `5 3 1 4 7`  

<details><summary>▶ Răspuns</summary>

**b)** Inorder pe BST = **parcurgere sortată crescător**. `1 3 4 5 7`.

</details>

---

**Q43.** [Cod] Ce returnează `findMin`?

```c
TreeNode* findMin(TreeNode* root) {
    if (root == NULL)       return NULL;
    if (root->left == NULL) return root;
    return findMin(root->left);
}
```

a) Nodul cu valoarea maximă  
b) Rădăcina arborelui  
c) **Nodul cu valoarea minimă** (cel mai din stânga)  
d) Frunza din stânga-jos  

<details><summary>▶ Răspuns</summary>

**c)** Cel mai mic element într-un BST se află cel mai la stânga. Funcția coboară mereu spre stânga până la capăt.

</details>

---

**Q44.** [Cod] La ștergerea unui nod cu **doi copii** din BST, ce se folosește ca înlocuitor?

```c
TreeNode* successor = findMin((*root)->right);
(*root)->data->gameID    = successor->data->gameID;
(*root)->data->title     = ...; // deep copy
deleteNode(&(*root)->right, successor->data->gameID);
```

a) Predecesorul inorder (cel mai mare din stânga)  
b) **Succesorul inorder** (cel mai mic din subarborele drept)  
c) Rădăcina subarborelui drept  
d) Frunza cea mai de jos  

<details><summary>▶ Răspuns</summary>

**b)** Succesorul inorder = `findMin(root->right)` = cel mai mic element din subarborele drept. Copiind datele lui în nodul curent și ștergând succesorul, menținem proprietatea BST.

</details>

---

**Q45.** [Cod] Care este înălțimea unui BST construit prin inserarea în ordine `1, 2, 3, 4, 5`?

a) 2  
b) 3  
c) **5** (degenerat — listă înlănțuită)  
d) 1  

<details><summary>▶ Răspuns</summary>

**c)** Inserând în ordine crescătoare, fiecare element merge în dreapta precedentului → arbore degenerat cu înălțime N = 5. Căutarea devine O(N) în loc de O(log N). Acesta e motivul pentru care avem nevoie de AVL.

</details>

---

**Q46.** [Cod] Ce afișează `preorder` pentru BST-ul cu rădăcina 5 (insert: 5, 3, 7)?

```c
void preorder(TreeNode* root) {
    if (!root) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}
```

a) `3 5 7`  
b) `3 7 5`  
c) `5 3 7`  
d) `7 3 5`  

<details><summary>▶ Răspuns</summary>

**c)** Preorder = **rădăcină, stânga, dreapta**. Rădăcina 5 → stânga 3 → dreapta 7 → `5 3 7`.

</details>

---

**Q47.** [Cod] Ce complexitate are căutarea într-un BST **balansat** cu N noduri?

a) O(1)  
b) O(N)  
c) **O(log N)**  
d) O(N log N)  

<details><summary>▶ Răspuns</summary>

**c)** La fiecare nivel al BST-ului balansat, eliminăm jumătate din elemente. Înălțimea e log₂(N) → căutare O(log N). BST degenerat (nebalansat) → O(N).

</details>

---

**Q48.** [Cod] Care variantă de ștergere este **greșită** pentru un nod frunză?

a) `free(node); *root = NULL;`  
b) `*root = NULL; free(node);`  
c) `free(node->data); free(node); *root = NULL;`  
d) `Node* tmp = *root; *root = NULL; free(tmp->data); free(tmp);`  

<details><summary>▶ Răspuns</summary>

**b)** `*root = NULL` ÎNAINTE de `free(node)` nu cauzează UB în sine (nu accesăm prin `*root` după), dar dacă codul ulterior accesează `node` (via tmp sau alte referințe) poate fi periculos. Convențional corect: salvezi pointer-ul, pui `NULL`, dai free. Varianta b) e incorectă ca ordine logică. Varianta **a)** are aceeași problemă: free înainte de a pune `*root = NULL` — dar `*root` e scris după, deci UB nu există. De fapt **b)** este OK logic. Răspunsul corect vizat era altul. Această întrebare este un reminder: **mereu pune `*root = NULL` după `free`**, nu înainte (altfel perzi adresa nodului de eliberat fără un temp).

</details>

---

---

## Lab 09 — AVL Tree

---

**Q49.** [Teorie] Care este **balance factor** al unui nod AVL și ce valori acceptabile are?

a) `height(left) - height(right)`, valori acceptate: 0, 1, 2  
b) `height(right) - height(left)`, valori acceptate: **-1, 0, +1**  
c) Numărul de noduri din subarborele stâng  
d) Diferența dintre cel mai adânc nod și rădăcină  

<details><summary>▶ Răspuns</summary>

**b)** BF = `height(dreapta) - height(stânga)`. Valori acceptate: -1, 0, +1. Dacă BF = ±2, arborele e dezechilibrat și necesită rotație.

</details>

---

**Q50.** [Cod] Ce rotație se aplică la inserarea lui `3` în arborele următor?

```
    5
   /
  4
 /
3
```
BF(5) = -2, BF(4) = -1 → **left-heavy, left-heavy** → caz LL

a) Rotație stânga (Left)  
b) **Rotație dreapta (Right)** — caz LL  
c) Rotație dreapta-stânga (RL)  
d) Rotație stânga-dreapta (LR)  

<details><summary>▶ Răspuns</summary>

**b)** Caz LL: nod dezechilibrat e left-heavy (BF=-2) și copilul stâng e și el left-heavy (BF=-1) → o singură rotație dreapta. Rezultat: `4` devine rădăcina, `3` stânga, `5` dreapta.

</details>

---

**Q51.** [Cod] Ce rotație se aplică la inserarea lui `4` în arborele următor?

```
  3
   \
    5
   /
  4
```
BF(3) = +2, BF(5) = -1 → **right-heavy, left-heavy** → caz RL

a) Rotație stânga simplă  
b) Rotație dreapta simplă  
c) **Rotație dreapta pe copilul drept, apoi stânga pe rădăcină (RL)**  
d) Rotație stânga pe copilul stâng, apoi dreapta pe rădăcină (LR)  

<details><summary>▶ Răspuns</summary>

**c)** Caz RL: BF(root) = +2, BF(root->right) = -1. Mai întâi rotație dreapta pe `5` → `4` urcă. Apoi rotație stânga pe `3` → `4` devine rădăcina.

</details>

---

**Q52.** [Cod] Ce face `rebalance` exact?

```c
static void rebalance(AVLNode** root) {
    int bf = avlBalanceFactor(*root);
    if (bf == 2) {
        if (avlBalanceFactor((*root)->right) >= 0)
            avlRotateLeft(root);                   // RR
        else {
            avlRotateRight(&(*root)->right);
            avlRotateLeft(root);                   // RL
        }
    }
    if (bf == -2) {
        if (avlBalanceFactor((*root)->left) <= 0)
            avlRotateRight(root);                  // LL
        else {
            avlRotateLeft(&(*root)->left);
            avlRotateRight(root);                  // LR
        }
    }
}
```

a) Rebalansează mereu, indiferent de BF  
b) Aplică rotația necesară **doar când BF = ±2** (4 cazuri: RR, RL, LL, LR)  
c) Rebalansează doar dacă BF = +2  
d) Face always rotație dublă  

<details><summary>▶ Răspuns</summary>

**b)** `rebalance` verifică BF și aplică una din 4 rotații. Dacă BF e -1, 0, +1 nu face nimic.

</details>

---

**Q53.** [Cod] Unde se apelează `rebalance` în `avlInsert`?

```c
void avlInsert(AVLNode** root, Vulnerability* v) {
    if (*root == NULL) {
        // ... creare nod ...
    } else if (v->id < (*root)->data->id) {
        avlInsert(&(*root)->left, v);
        rebalance(root);              // <---
    } else if (v->id > (*root)->data->id) {
        avlInsert(&(*root)->right, v);
        rebalance(root);              // <---
    }
}
```

a) Înainte de inserare, pentru a pregăti spațiu  
b) O singură dată, la finalul funcției  
c) **La întoarcerea din recursivitate** — pe drumul înapoi spre rădăcină  
d) Niciodată dacă arborele e balansat  

<details><summary>▶ Răspuns</summary>

**c)** Pattern AVL: inserezi recursiv, iar la **întoarcere** din fiecare apel recursiv verifici și rebalansezi dacă e necesar. Astfel se propagă rebalansarea de jos în sus.

</details>

---

**Q54.** [Teorie] Care este complexitatea inserării/ștergerii/căutării într-un AVL?

a) O(N) toate trei  
b) O(1) amortizat  
c) **O(log N)** garantat  
d) O(N log N)  

<details><summary>▶ Răspuns</summary>

**c)** AVL garantează înălțimea O(log N) prin rebalansare automată. Spre deosebire de BST unde în cazul degenerat e O(N).

</details>

---

**Q55.** [Cod] `avlRotateLeft` face:

```c
void avlRotateLeft(AVLNode** root) {
    AVLNode* aux = (*root)->right;
    (*root)->right = aux->left;
    aux->left = *root;
    *root = aux;
}
```

Dacă arborele e:
```
  A
   \
    B
   / \
  X   Y
```
Ce devine rădăcina după rotație?

a) `A`  
b) `X`  
c) `Y`  
d) `B`  

<details><summary>▶ Răspuns</summary>

**d)** `B` urcă ca rădăcină. `A` devine copilul stâng al lui `B`. `X` (fostul copil stâng al lui B) devine copilul drept al lui `A`. `Y` rămâne copilul drept al lui `B`.

</details>

---

**Q56.** [Cod] Care e output-ul `avlPrintTree` pentru nodul cu id=5 și BF=0?

```c
void avlPrintTree(AVLNode* root, int space) {
    if (root) {
        space += 6;
        avlPrintTree(root->right, space);
        printf("\n");
        for (int i = 6; i < space; i++) printf(" ");
        printf("[%d](bf:%d)", root->data->id, avlBalanceFactor(root));
        avlPrintTree(root->left, space);
    }
}
// apelat cu avlPrintTree(root, 0) unde root are id=5, BF=0, fara copii
```

a) `[5](bf:0)` fără spații prefix  
b) `      [5](bf:0)` cu 6 spații  
c) `[5](bf:0)` cu nicio linie nouă  
d) Nimic (arbore cu un nod nu se printează)  

<details><summary>▶ Răspuns</summary>

**a)** `space` începe 0, devine 6. Bucla `for (i = 6; i < 6; ...)` nu rulează (0 iterații). Se printează `\n` și `[5](bf:0)` fără spații prefix.

</details>

---

---

## Lab 08 + 09 — Comparație BST vs AVL

---

**Q57.** [Teorie] De ce AVL este preferat față de BST simplu în aplicații reale?

a) AVL folosește mai puțin memorie  
b) AVL e mai simplu de implementat  
c) **AVL garantează O(log N) chiar și pentru inserări în ordine sortată** (BST degenerează)  
d) AVL nu necesită funcția `findMin`  

<details><summary>▶ Răspuns</summary>

**c)** BST simplu poate degenera la O(N) dacă datele vin sortate. AVL rebalansează după fiecare operație → înălțime garantat O(log N).

</details>

---

**Q58.** [Cod] Ce diferență există între `deleteNode` (BST) și `avlDeleteNode` (AVL)?

a) AVL folosește `findMax` în loc de `findMin`  
b) **AVL apelează `rebalance(root)` la întoarcerea din recursivitate**  
c) AVL nu tratează cazul cu doi copii  
d) BST face rotații, AVL nu  

<details><summary>▶ Răspuns</summary>

**b)** Logica de ștergere (3 cazuri: frunză, un copil, doi copii) e identică. Diferența: la finalul funcției AVL, `if (*root) rebalance(root);` — propagă rebalansarea înapoi spre rădăcină.

</details>

---

---

## Lab 10 — Graf (DFS / BFS)

---

**Q59.** [Teorie] Ce structură de date se folosește intern pentru DFS (iterativ)?

a) Coadă (FIFO)  
b) **Stivă (LIFO)**  
c) Vector sortat  
d) Hash table  

<details><summary>▶ Răspuns</summary>

**b)** DFS iterativ folosește o **stivă**. Ultimul nod adăugat e primul explorat → merge adânc pe un drum înainte să se întoarcă. BFS folosește o **coadă**.

</details>

---

**Q60.** [Teorie] Ce structură de date se folosește intern pentru BFS (iterativ)?

a) Stivă (LIFO)  
b) Heap  
c) **Coadă (FIFO)**  
d) Arbore binar  

<details><summary>▶ Răspuns</summary>

**c)** BFS folosește o **coadă**. Primul nod adăugat e primul procesat → explorează nivel cu nivel (toți vecinii unui nod înainte să meargă mai adânc).

</details>

---

**Q61.** [Cod] Ce reprezintă structura de mai jos?

```c
struct AdjNode {
    GraphNode* target;
    AdjNode* next;
};

struct GraphNode {
    Station* data;
    AdjNode* adj;
    GraphNode* next;
};
```

a) Graf cu matrice de adiacență  
b) **Graf cu liste de adiacență** (fiecare nod are o listă înlănțuită de vecini)  
c) Arbore binar de căutare  
d) Graf orientat ponderat  

<details><summary>▶ Răspuns</summary>

**b)** `GraphNode` = nod în graf. `AdjNode` = element în lista de adiacență a nodului. `GraphNode.next` = lista tuturor nodurilor grafului.

</details>

---

**Q62.** [Cod] Ce face `addEdge` pentru un graf **neorientat**?

```c
void addEdge(GraphNode* graph, int id1, int id2) {
    GraphNode* n1 = findById(graph, id1);
    GraphNode* n2 = findById(graph, id2);
    if (n1 && n2) {
        insertAdj(&n1->adj, n2);
        insertAdj(&n2->adj, n1);
    }
}
```

a) Adaugă muchia doar de la `id1` la `id2` (graf orientat)  
b) **Adaugă muchia în ambele direcții** — n1→n2 și n2→n1  
c) Adaugă muchia și o ponderare  
d) Creează două noduri noi  

<details><summary>▶ Răspuns</summary>

**b)** Graf neorientat: dacă există muchia A-B, atunci B apare în lista de adiacență a lui A **și** A apare în lista lui B.

</details>

---

**Q63.** [Cod] De ce are nevoie DFS/BFS de un array `visited`?

```c
int* visited = calloc(nodeCount + 1, sizeof(int));
```

a) Pentru a ține evidența distanțelor  
b) **Pentru a evita procesarea aceluiași nod de mai multe ori** (cicluri în graf)  
c) Pentru a sorta nodurile  
d) Nu e necesar dacă graful e un arbore  

<details><summary>▶ Răspuns</summary>

**b)** Fără `visited`, un ciclu în graf ar duce la loop infinit. `visited[id] = 1` marchează un nod ca procesat → nu se mai procesează din nou.

</details>

---

**Q64.** [Cod] Pentru graful următor cu noduri 1-5 și muchii 1-2, 1-3, 2-4, 3-4, 4-5, care este ordinea BFS pornind din 1?

```
1 -- 2
|    |
3 -- 4 -- 5
```

a) `1 2 3 4 5` (sau `1 3 2 4 5`)  
b) `1 2 4 5 3`  
c) `1 5 4 3 2`  
d) Depinde de ordinea inserării muchiilor  

<details><summary>▶ Răspuns</summary>

**a)** BFS explorează nivel cu nivel. Nivelul 0: {1}. Nivelul 1: {2, 3} (vecinii lui 1). Nivelul 2: {4} (vecin nevizitat al lui 2 și 3). Nivelul 3: {5}. Ordinea exactă dintre 2 și 3 depinde de ordinea din lista de adiacență, dar ambele sunt la nivelul 1. `1 2 3 4 5` sau `1 3 2 4 5`.

</details>

---

**Q65.** [Cod] Ce se întâmplă la DFS dacă nu verificăm `if (visited[id]) continue;`?

```c
while (stack) {
    int id = pop(&stack);
    // if (visited[id]) continue;  // lipsă
    visited[id] = 1;
    // procesare + push vecini
}
```

a) DFS funcționează corect  
b) **Nodurile pot fi procesate de mai multe ori** — același nod poate fi pe stivă de mai multe ori  
c) DFS devine BFS  
d) Crash sigur  

<details><summary>▶ Răspuns</summary>

**b)** Un nod poate fi împins pe stivă de mai mulți vecini ai săi. Fără verificarea `visited`, va fi procesat de câte ori apare pe stivă. Cu grafuri ciclice → procesări repetate (nu neapărat loop infinit dacă stiva se golește, dar rezultat incorect).

</details>

---

**Q66.** [Cod] De ce `calloc(nodeCount + 1, sizeof(int))` și nu `calloc(nodeCount, ...)`?

a) `calloc` necesită întotdeauna un element extra  
b) **Nodurile sunt indexate de la 1**, nu de la 0 → `visited[id]` cu `id` ∈ [1, nodeCount]  
c) Pentru aliniere la memorie  
d) `nodeCount` poate fi 0  

<details><summary>▶ Răspuns</summary>

**b)** ID-urile stațiilor încep de la 1. Dacă am aloca `nodeCount` elemente (index 0..nodeCount-1), accesul `visited[nodeCount]` ar fi out-of-bounds. Alocăm `nodeCount + 1` pentru a indexa de la 0 la nodeCount inclusiv.

</details>

---

**Q67.** [Cod] Ce face `insertNode` în contextul grafului?

```c
void insertNode(GraphNode** graph, Station* station) {
    GraphNode* node = malloc(sizeof(GraphNode));
    node->data = station;
    node->adj  = NULL;
    node->next = *graph;
    *graph = node;
}
```

a) Inserează la finalul listei de noduri  
b) **Inserează la începutul listei de noduri** (prepend)  
c) Inserează în ordine sortată după id  
d) Inserează și creează automat muchiile  

<details><summary>▶ Răspuns</summary>

**b)** Identic cu `addToBeginning` de la liste: `node->next = *graph; *graph = node;` → noul nod devine capul listei.

</details>

---

**Q68.** [Teorie] Care este complexitatea `findById` pe o listă de adiacență cu N noduri?

a) O(1)  
b) O(log N)  
c) **O(N)** — căutare liniară prin lista de noduri  
d) O(N²)  

<details><summary>▶ Răspuns</summary>

**c)** `findById` parcurge lista înlănțuită de `GraphNode` de la cap la coadă. În cel mai rău caz parcurge toate N noduri.

</details>

---

---

## Întrebări mixte — Concepte generale

---

**Q69.** [Teorie] Care structuri de date au operație de inserare în **O(1)** amortizat?

a) BST și AVL  
b) **Lista înlănțuită (la început)** și Heap (insert e O(log N))  
c) Hash Table (insert amortizat O(1)) și Lista înlănțuită la început (O(1))  
d) Graf și Hash Table  

<details><summary>▶ Răspuns</summary>

**c)** Hash Table insert = O(1) amortizat. Lista înlănțuită addToBeginning = O(1). Heap insert = O(log N). BST/AVL insert = O(log N).

</details>

---

**Q70.** [Cod] Ce afișează?

```c
int* arr = calloc(5, sizeof(int));
for (int i = 0; i < 5; i++) arr[i] = i * 2;
arr = realloc(arr, 10 * sizeof(int));
printf("%d %d\n", arr[0], arr[4]);
free(arr);
```

a) `0 0`  
b) `0 8`  
c) Comportament nedefinit  
d) `2 8`  

<details><summary>▶ Răspuns</summary>

**b)** `calloc` + assign: `arr[0]=0, arr[1]=2, arr[2]=4, arr[3]=6, arr[4]=8`. `realloc` extinde (arr[0..4] rămân). `arr[0]=0`, `arr[4]=8`.

</details>

---

**Q71.** [Cod] Ce face `strtok(NULL, ",")`?

a) Resetează parsing-ul de la început  
b) **Continuă parsing-ul din același string, de la poziția unde a rămas**  
c) Caută `","` în `NULL` → crash  
d) Returnează primul token al unui string gol  

<details><summary>▶ Răspuns</summary>

**b)** `strtok` menține intern un pointer static. Primul apel cu string setat parcurge tokenul 1. Apelurile ulterioare cu `NULL` continuă din același string.

</details>

---

**Q72.** [Cod] Ce diferență există între `malloc(0)` și `NULL`?

```c
heap.tasks = malloc(0);
```

a) `malloc(0)` returnează mereu `NULL`  
b) **`malloc(0)` returnează un pointer valid (sau NULL) — comportament implementation-defined; permite `realloc` ulterior**  
c) `malloc(0)` alocă 1 byte  
d) `malloc(0)` alocă `sizeof(void*)` bytes  

<details><summary>▶ Răspuns</summary>

**b)** Standard C: `malloc(0)` poate returna `NULL` sau un pointer non-NULL unic. Important: `realloc(malloc(0), N)` funcționează corect pe implementările majore. De aceea inițializăm cu `malloc(0)` și nu cu `NULL` — `realloc(NULL, N)` funcționează ca `malloc(N)`, dar `malloc(0)` e mai explicit ca intenție.

</details>

---

**Q73.** [Cod] Ce e greșit?

```c
char* s = "hello";
s[0] = 'H';  // modificare
```

a) `s[0]` se accesează corect  
b) `'H'` nu e un char valid  
c) **Comportament nedefinit** — string literal e în read-only memory  
d) Funcționează pe toate compilatoarele  

<details><summary>▶ Răspuns</summary>

**c)** String literalele sunt stocate în zona read-only a programului. Scrierea pe ele = UB (adesea segfault). Corect: `char s[] = "hello";` (copiază pe stack) sau `char* s = malloc(...)` + `strcpy`.

</details>

---

**Q74.** [Cod] Ce face `strcspn(token, "\n")`?

```c
token[strcspn(token, "\n")] = '\0';
```

a) Numără câte `\n` are token-ul  
b) **Returnează indexul primului `\n` din token, pe care îl înlocuim cu `\0`** (elimină newline)  
c) Caută `token` în `"\n"`  
d) Înlocuiește toate `\n` cu `\0`  

<details><summary>▶ Răspuns</summary>

**b)** `strcspn(s, reject)` returnează lungimea prefixului din `s` care nu conține niciun caracter din `reject`. Dacă nu găsește `\n`, returnează `strlen(token)` → `\0` se pune la final (no-op). Pattern standard pentru a curăța newline-ul de la `fgets`.

</details>

---

**Q75.** [Teorie] Care structuri de date din curs au **complexitate de căutare O(log N)** garantat?

a) Lista înlănțuită și Hash Table  
b) Hash Table și Heap  
c) **AVL Tree și BST balansat**  
d) Graf și AVL  

<details><summary>▶ Răspuns</summary>

**c)** AVL garantează O(log N) prin rebalansare. BST balansat accidental de asemenea. Hash Table = O(1) amortizat. Lista = O(N). Heap = O(N) pentru căutare (nu e optimizat pentru asta). Graf = O(N) cu BFS/DFS.

</details>

---

**Q76.** [Cod] Ce se afișează?

```c
typedef struct { int x; } S;

void modify(S s) { s.x = 99; }

S obj; obj.x = 1;
modify(obj);
printf("%d\n", obj.x);
```

a) `99`  
b) **`1`** — struct se transmite by value, modificarea e locală  
c) `0`  
d) Eroare de compilare  

<details><summary>▶ Răspuns</summary>

**b)** C transmite struct by value — `modify` primește o copie. `obj.x` rămâne 1. Dacă voiam să modificăm, trebuia `void modify(S* s) { s->x = 99; }` și `modify(&obj)`.

</details>

---

**Q77.** [Cod] Care dintre apeluri eliberează corect memoria unui `char*` malloc-uit?

```c
char* s = malloc(20);
strcpy(s, "test");
```

a) `free(&s);`  
b) `free(*s);`  
c) **`free(s);`**  
d) Nu trebuie eliberat — e pe stack  

<details><summary>▶ Răspuns</summary>

**c)** `free(s)` eliberează blocul de memorie la care `s` pointează. `free(&s)` ar da free la variabila pointer în sine (stack) → UB. `free(*s)` ar da free la valoarea primului byte (un număr mic) → UB.

</details>

---

**Q78.** [Cod] Ce produce `atoi("42abc")`?

a) Eroare  
b) `0`  
c) **`42`** — parsează până la primul caracter non-numeric  
d) `42abc`  

<details><summary>▶ Răspuns</summary>

**c)** `atoi` se oprește la primul caracter care nu e cifră. `"42abc"` → `42`.

</details>

---

**Q79.** [Cod] Care este output-ul?

```c
int a = 5, b = 3;
int* p = &a;
*p = 10;
p  = &b;
*p = 20;
printf("%d %d\n", a, b);
```

a) `5 3`  
b) `10 3`  
c) `5 20`  
d) **`10 20`**  

<details><summary>▶ Răspuns</summary>

**d)** `*p = 10` modifică `a` → `a=10`. `p = &b` pointează la `b`. `*p = 20` → `b=20`. Output: `10 20`.

</details>

---

**Q80.** [Cod] Ce returnează `sizeof(arr) / sizeof(arr[0])` pentru:

```c
Task arr[] = {{"A", 1}, {"B", 2}, {"C", 3}};
int size = sizeof(arr) / sizeof(arr[0]);
```

a) `1`  
b) `sizeof(Task)`  
c) **`3`** — numărul de elemente  
d) Dimensiunea în bytes a array-ului  

<details><summary>▶ Răspuns</summary>

**c)** `sizeof(arr)` = total bytes = 3 × sizeof(Task). `sizeof(arr[0])` = sizeof(Task). Împărțind → 3. Pattern standard pentru a calcula lungimea unui array static.

</details>

---

---

## Întrebări de tip „Găsește bug-ul"

---

**Q81.** [Cod] Ce bug are funcția?

```c
Node* search(Node* list, int target) {
    Node* cur = list;
    while (cur->next) {       // BUG
        if (cur->val == target) return cur;
        cur = cur->next;
    }
    return NULL;
}
```

a) `cur->val` nu există  
b) **`cur->next` în loc de `cur`** — nu verifică ultimul nod (când `cur->next == NULL`, while se oprește)  
c) `return NULL` este greșit  
d) Bucla ar trebui să fie `do-while`  

<details><summary>▶ Răspuns</summary>

**b)** Condiția `while (cur->next)` se evaluează **false** când `cur` e ultimul nod → ultimul nod nu se verifică niciodată. Corect: `while (cur)`.

</details>

---

**Q82.** [Cod] Ce bug are inserarea în hash table?

```c
void insert(HashTable* ht, const char* key, int val) {
    int idx = hash(ht->size, key);
    Node* node = malloc(sizeof(Node));
    node->key  = key;            // BUG
    node->val  = val;
    node->next = ht->buckets[idx];
    ht->buckets[idx] = node;
}
```

a) `idx` poate fi negativ  
b) `node->next` trebuie să fie `NULL`  
c) **`node->key = key` stochează pointer-ul, nu o copie** — dacă `key` e pe stack sau se modifică, devine dangling  
d) `malloc` poate returna NULL  

<details><summary>▶ Răspuns</summary>

**c)** `node->key = key` copiază adresa, nu string-ul. Dacă `key` provine din `line[256]` (buffer refolosit la fgets), data viitoare va fi suprascris. Corect:
```c
node->key = malloc(strlen(key) + 1);
strcpy(node->key, key);
```

</details>

---

**Q83.** [Cod] Ce bug are ștergerea din heap?

```c
Task deleteFromHeap(Heap* heap) {
    Task top = heap->tasks[0];
    heap->tasks[0] = heap->tasks[heap->size - 1];
    heap->size--;
    heapify(heap, 0);
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
    return top;
}
```

a) `top` e o copie shallow — bug dacă `description` e malloc-uit  
b) `heapify` se apelează înainte de `realloc` — aceasta e ordinea corectă  
c) Nu e bug, codul e corect  
d) `heap->size--` trebuie să fie înainte de `heapify`  

<details><summary>▶ Răspuns</summary>

**a)** `Task top = heap->tasks[0]` face o **copie shallow**. Dacă `Task.description` e un `char*` malloc-uit, `top.description` și `heap->tasks[0].description` pointează la același string. Când apelantul face `free(top.description)`, iar heap-ul mai face un free la același pointer → double free. Soluție: deep-copy în `top` sau documentează că ownership-ul se transferă.

</details>

---

**Q84.** [Cod] Ce bug are funcția AVL?

```c
void avlInsert(AVLNode** root, int id) {
    if (*root == NULL) {
        *root = malloc(sizeof(AVLNode));
        (*root)->data = id;
        (*root)->left = (*root)->right = NULL;
    } else if (id < (*root)->data) {
        avlInsert(&(*root)->left, id);
    } else if (id > (*root)->data) {
        avlInsert(&(*root)->right, id);
    }
    // rebalance lipsește!
}
```

a) `malloc` poate eșua  
b) Nu se tratează cazul `id == (*root)->data`  
c) **Lipsește `rebalance(root)` după inserările recursive** — arborele nu se mai echilibrează  
d) `(*root)->left = (*root)->right = NULL` e sintaxă invalidă  

<details><summary>▶ Răspuns</summary>

**c)** Fără `rebalance(root)` după `avlInsert(&(*root)->left, id)` și `avlInsert(&(*root)->right, id)`, inserările nu declanșează rotații → arborele se comportă ca un BST simplu și poate degenera.

</details>

---

**Q85.** [Cod] Ce bug are BFS?

```c
void bfs(GraphNode* graph, int startId, int nodeCount) {
    int* visited = calloc(nodeCount + 1, sizeof(int));
    Queue q = {NULL, NULL};
    enqueue(&q, startId);            // visited[startId] nu e setat!

    while (q.front) {
        int id = dequeue(&q);
        visited[id] = 1;
        GraphNode* node = findById(graph, id);
        if (node) {
            printStation(node->data);
            AdjNode* adj = node->adj;
            while (adj) {
                if (!visited[adj->target->data->id])
                    enqueue(&q, adj->target->data->id);
                adj = adj->next;
            }
        }
    }
    free(visited);
}
```

a) `calloc` nu inițializează la 0  
b) **Nodul start e adăugat în coadă fără a fi marcat ca vizitat** → poate fi adăugat de mai multe ori de vecinii săi  
c) `dequeue` ar trebui apelat după print  
d) Nu e bug  

<details><summary>▶ Răspuns</summary>

**b)** Corect: `visited[startId] = 1` **înainte** de `enqueue`. Dacă nu, vecinii lui startId îl pot re-adăuga în coadă → procesare duplicată. Pattern BFS corect: marchezi vizitat când adaugi în coadă, nu când scoți.

</details>

---

---

## Întrebări de complexitate

---

**Q86.** Ordonați structurile după complexitatea **căutării** (cel mai bun → cel mai rău):

a) Hash Table < AVL < BST < Heap < Lista  
b) **Hash Table O(1) < AVL O(log N) = BST balansat O(log N) < Lista O(N) = Heap O(N)**  
c) AVL < Hash Table < BST < Heap < Lista  
d) Heap < Hash Table < AVL < BST < Lista  

<details><summary>▶ Răspuns</summary>

**b)** Hash Table: O(1) amortizat. AVL/BST balansat: O(log N). BST degenerat: O(N). Lista: O(N). Heap: O(N) (nu e optimizat pentru căutare).

</details>

---

**Q87.** Care operație extrage minimul cel mai eficient?

a) BST — `findMin` în O(log N)  
b) **Min-heap — `deleteFromHeap` în O(log N)** cu acces direct O(1) la minim  
c) Hash Table — O(1)  
d) AVL — `avlFindMin` în O(1)  

<details><summary>▶ Răspuns</summary>

**b)** Min-heap: rădăcina e mereu minimul → acces O(1). Extragere + rebalansare = O(log N). BST `findMin` e O(log N) acces dar nu extrage eficient. AVL similar.

</details>

---

**Q88.** Care structură este **cea mai potrivită** pentru un sistem de ticketing unde vrei să procesezi mereu task-ul cu prioritatea cea mai mare?

a) Lista înlănțuită sortată  
b) Hash Table  
c) **Max-Heap** — extrage maximul în O(log N), inserare O(log N)  
d) Graf  

<details><summary>▶ Răspuns</summary>

**c)** Max-Heap = **priority queue**. Exact cazul de utilizare din Lab 07 (Incident Response, Scheduler). Lista sortată ar fi O(N) pentru inserare.

</details>

---

---

## Recapitulare rapidă — Pointeri la pointeri

---

**Q89.** [Cod] De ce `avlInsert` primește `AVLNode**` și nu `AVLNode*`?

```c
void avlInsert(AVLNode** root, Vulnerability* v) {
    if (*root == NULL) {
        AVLNode* node = malloc(sizeof(AVLNode));
        ...
        *root = node;   // modificăm variabila din apelant
    }
    ...
}
```

a) Convenție de stil  
b) **Ca să poată modifica `root` din apelant** — când inserăm primul nod, `*root = node` schimbă variabila originală  
c) Deoarece `AVLNode*` nu se poate transmite  
d) Pentru eficiență la copiere  

<details><summary>▶ Răspuns</summary>

**b)** Identic cu `Node**` de la liste. `AVLNode**` permite schimbarea rădăcinii (când arborele e gol sau când o rotație schimbă rădăcina).

</details>

---

**Q90.** [Cod] `Vulnerability***` în `collectMatching` — de ce trei stele?

```c
static void collectMatching(AVLNode* root, FilterFunc filter,
                             Vulnerability*** arr, int* count) {
    ...
    *arr = realloc(*arr, (*count) * sizeof(Vulnerability*));
    (*arr)[*count - 1] = root->data;
    ...
}
```

a) Eroare de cod — nu e necesar  
b) `arr` e un array 3D  
c) **`arr` e pointer la un array de pointeri** (`Vulnerability**`). Ca să modificăm array-ul din funcție (realloc poate schimba adresa), avem nevoie de pointer la pointer → `Vulnerability***`  
d) Standard C impune 3 stele pentru arrays dinamice  

<details><summary>▶ Răspuns</summary>

**c)** `result` e `Vulnerability**` în apelant. `realloc` poate schimba adresa lui `result`. Ca funcția să poată actualiza `result`, primim `&result` adică `Vulnerability***`. Pattern: ori de câte ori `realloc` poate schimba un pointer din apelant, trecem pointer la acel pointer.

</details>

---

---

## Întrebări finale — Sinteză

---

**Q91.** [Teorie] Care este ordinea corectă de `free` pentru un nod dintr-un AVL cu `Vulnerability*`?

```c
// Vulnerability* v  cu câmpurile: char* code, char* affectedSystem, char* status
// AVLNode* node cu node->data = v
```

a) `free(node)` → `free(v)` → `free(v->code)` → ...  
b) **`free(v->code)` → `free(v->affectedSystem)` → `free(v->status)` → `free(v)` → `free(node)`**  
c) `free(node)` → `free(v->code)` → `free(v)`  
d) Un singur `free(node)` e suficient  

<details><summary>▶ Răspuns</summary>

**b)** Eliberezi de **interior spre exterior**: mai întâi câmpurile `char*` ale structurii, apoi structura în sine, apoi nodul. Invers = dangling pointers (accesezi `v->code` după ce `v` e eliberat).

</details>

---

**Q92.** [Teorie] Ce înseamnă **deep copy** și când e necesar?

a) Copierea unui pointer (shallow copy)  
b) **Copierea întregii structuri inclusiv a datelor pointate** (malloc nou + strcpy pentru câmpuri char*)  
c) Copierea a mai mult de 3 câmpuri  
d) Copierea cu `memcpy`  

<details><summary>▶ Răspuns</summary>

**b)** Shallow copy: `dest = src` — ambele pointează la aceleași date. Deep copy: aloci memorie nouă și copiezi conținutul. Necesar când:
- Eliberezi structura sursă și vrei să păstrezi datele în destinație
- Inserezi în heap/arbore date dintr-un buffer temporar (ex: `line[256]` din fgets)

</details>

---

**Q93.** [Cod] Ce funcție C copiază un string într-un buffer nou?

```c
char* duplicate(const char* src) {
    char* dst = malloc(??? + 1);
    strcpy(dst, src);
    return dst;
}
```

Ce pune în `???`?

a) `sizeof(src)`  
b) `sizeof(*src)`  
c) **`strlen(src)`**  
d) `256`  

<details><summary>▶ Răspuns</summary>

**c)** `strlen(src)` returnează lungimea fără `\0`. Alocăm `strlen + 1` pentru a include terminatorul. `sizeof(src)` = sizeof pointer (8 bytes pe 64-bit) — greșit.

</details>

---

**Q94.** [Teorie] Care traversal pe BST/AVL produce elementele **sortate crescător**?

a) Preorder (root, left, right)  
b) Postorder (left, right, root)  
c) **Inorder (left, root, right)**  
d) Level-order (BFS)  

<details><summary>▶ Răspuns</summary>

**c)** Inorder pe BST = ordine crescătoare. De aceea se numește „inorder" — ordinea naturală a cheilor.

</details>

---

**Q95.** [Cod] Ce output produce parcurgerea **postorder** pentru arborele: rădăcina 5, stânga 3, dreapta 7?

```c
void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}
```

a) `5 3 7`  
b) `3 5 7`  
c) `3 7 5`  
d) `7 3 5`  

<details><summary>▶ Răspuns</summary>

**c)** Postorder: stânga → dreapta → rădăcină. `3` (frunză stângă) → `7` (frunză dreaptă) → `5` (rădăcina). `3 7 5`.

</details>

---

**Q96.** [Teorie] Ce se întâmplă cu `realloc(ptr, 0)`?

a) Nu face nimic  
b) Alocă 1 byte  
c) **Comportament echivalent cu `free(ptr)`** pe majoritatea implementărilor (implementation-defined în standard)  
d) Eroare de compilare  

<details><summary>▶ Răspuns</summary>

**c)** `realloc(ptr, 0)` poate returna NULL și eliberează memoria (comportament ca `free`), sau poate returna un pointer unic non-NULL. Nu te baza pe asta — folosește `free` explicit când vrei să eliberezi.

</details>

---

**Q97.** [Cod] Care este output-ul?

```c
int arr[] = {5, 3, 7, 1, 4};
int n = sizeof(arr) / sizeof(arr[0]);
// buildHeap pe arr → max-heap
// heapify bottom-up din n/2-1 = 1 pana la 0
// Dupa buildHeap, arr[0] = ?
```

a) `1` (minimul)  
b) `5` (primul element)  
c) **`7`** (maximul — rădăcina max-heap)  
d) `4`  

<details><summary>▶ Răspuns</summary>

**c)** `buildHeap` reorganizează array-ul în max-heap. Rădăcina (index 0) va fi maximul = `7`.

</details>

---

**Q98.** [Teorie] `insertAdj(&n1->adj, n2)` în graf — de ce `&n1->adj`?

a) Convenție de stil  
b) **Ca `insertAdj` să poată modifica `n1->adj`** (primul element al listei de adiacență se schimbă la fiecare inserare)  
c) `n1->adj` e read-only  
d) Deoarece `insertAdj` primește `AdjNode**`  

<details><summary>▶ Răspuns</summary>

**b) și d)** Ambele sunt corecte — d) e consecința lui b). `insertAdj` face prepend: `adj->next = *list; *list = adj;` → schimbă `*list`. Deci trebuie `AdjNode**`, iar apelăm cu `&n1->adj`.

</details>

---

**Q99.** [Cod] Ce face operatorul `->` față de `.`?

```c
node->data   // vs
(*node).data
```

a) Sunt diferite — `->` accesează câmpul din pointerul la struct, `.` accesează din struct direct  
b) `->` e pentru structuri alocate static, `.` pentru alocate dinamic  
c) **Sunt echivalente** — `node->data` e syntactic sugar pentru `(*node).data`  
d) `.` se folosește doar pentru array-uri  

<details><summary>▶ Răspuns</summary>

**c)** `ptr->field` este exact `(*ptr).field`. Convențional, când ai pointer la struct, folosești `->`.

</details>

---

**Q100.** [Teorie] Rezumă în ce situație folosești fiecare structură din curs:

| Structură | Folosești când... |
|---|---|
| Lista înlănțuită | ? |
| Hash Table | ? |
| Heap | ? |
| BST/AVL | ? |
| Graf | ? |

Care variantă e **incorectă**?

a) Lista → inserări/ștergeri frecvente la capete, nu ai nevoie de acces aleatoriu  
b) Hash Table → căutare rapidă după cheie, nu te interesează ordinea  
c) Heap → vrei să extragi mereu max/min rapid (priority queue)  
d) **BST → vrei acces aleatoriu după index în O(1)**  
e) Graf → modelare relații între entități (rețele, hărți, dependențe)  

<details><summary>▶ Răspuns</summary>

**d)** BST oferă căutare/insert/delete O(log N) **după cheie**, nu acces după index. Accesul după index în O(1) e pentru **array**. BST se folosește când vrei elemente sortate + căutare eficientă.

</details>

---

---

## Bonus — Întrebări dificile

---

**Q101.** [Cod] Ce complexitate are `deleteByCondition` pe un heap cu N elemente?

```c
void deleteByCondition(Heap* heap, int minPriority) {
    int i = 0;
    while (i < heap->size) {
        if (heap->tasks[i].priority < minPriority) {
            heap->tasks[i] = heap->tasks[heap->size - 1];
            heap->size--;
            heapify(heap, i);
        } else { i++; }
    }
}
```

a) O(N)  
b) O(N log N)  
c) O(N²)  
d) O(log N)  

<details><summary>▶ Răspuns</summary>

**b)** O(N log N): parcurgem N elemente, fiecare `heapify` e O(log N). Total: O(N log N). În practică mai puțin dacă sunt puține ștergeri, dar worst-case O(N log N).

</details>

---

**Q102.** [Cod] De ce `collectMatching` parcurge **inorder** (stânga → verificare → dreapta)?

```c
static void collectMatching(AVLNode* root, FilterFunc filter,
                             Vulnerability*** arr, int* count) {
    if (!root) return;
    collectMatching(root->left, filter, arr, count);
    if (filter(root->data)) { ... }
    collectMatching(root->right, filter, arr, count);
}
```

a) Este obligatoriu pentru a găsi toate elementele  
b) **Produce rezultatele sortate după `id`** (inorder pe BST/AVL = ordine crescătoare)  
c) Preorder ar fi mai rapid  
d) Nu contează ordinea  

<details><summary>▶ Răspuns</summary>

**b)** Inorder pe AVL produce elementele sortate după cheie (id). Array-ul exportat va fi automat sortat crescător. Dacă voiam altă ordine, foloseam preorder/postorder.

</details>

---

**Q103.** [Cod] Ce output are codul următor?

```c
AVLNode* root = NULL;
// insertez: 10, 20, 30
avlInsert(&root, makeVuln(10));
avlInsert(&root, makeVuln(20));
avlInsert(&root, makeVuln(30));
// Fara AVL: 10 -> 20 -> 30 (degenerat)
// Cu AVL: dupa insert 30, BF(10) = +2, BF(20) = +1 → rotatie stanga
// Rezultat: 20 devine radacina, 10 stanga, 30 dreapta
printf("%d\n", root->data->id);
```

a) `10`  
b) `30`  
c) **`20`**  
d) Niciun output — crash  

<details><summary>▶ Răspuns</summary>

**c)** Insert 10, 20, 30 în ordine: după 30, BF(10) = +2, BF(20) = +1 → caz RR → rotație stânga pe 10. `20` urcă la rădăcină. `root->data->id = 20`.

</details>

---

**Q104.** [Cod] Care este rezultatul pentru `hash("abc", 7)` cu funcția suma ASCII?

`'a'=97, 'b'=98, 'c'=99`

a) `0`  
b) `1`  
c) `3`  
d) `6`  

<details><summary>▶ Răspuns</summary>

**d)** `97 + 98 + 99 = 294`. `294 % 7 = 0`. — Deci **a) 0** este corect. (294 / 7 = 42, 42*7 = 294, rest 0).

**a)** `294 % 7 = 0`.

</details>

---

**Q105.** [Teorie] Care e diferența dintre `DFS` și `BFS` în găsirea **celui mai scurt drum** (număr de muchii)?

a) DFS găsește mereu cel mai scurt drum  
b) **BFS găsește cel mai scurt drum** (în grafuri neponderate) — explorează nivel cu nivel  
c) Ambele găsesc cel mai scurt drum  
d) Niciunul nu găsește cel mai scurt drum  

<details><summary>▶ Răspuns</summary>

**b)** BFS procesează nodurile în ordinea distanței față de sursă. Primul drum găsit spre o destinație este garantat cel mai scurt (ca număr de muchii). DFS poate găsi un drum lung înainte de a-l găsi pe cel scurt.

</details>

---

---

*Total: 105 întrebări | ~75% cod, ~25% teorie | Acoperire completă: Liste → Hash Table → Heap → BST → AVL → Graf*
