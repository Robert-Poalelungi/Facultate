# Lab 08 — Binary Search Tree (BST) — walkthrough complet

**Pre-requisites:** Lab 3 (recursivitate pe pointeri), `Node**` pattern.

---

## Concept central in 30 secunde

**BST** = arbore binar in care:
- **Stanga** are doar chei **mai mici** ca radacina
- **Dreapta** are doar chei **mai mari** (sau egale)
- **Recursiv** — fiecare subarbore e si el un BST

**De ce inveti BST inainte de AVL:** AVL = BST + rotatii. Daca nu intelegi recursivitatea pe arbore aici, AVL e magie neagra.

---

# Cod + walkthrough

## 1. Headere si structuri

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    unsigned int gameID;
    char* title;
    char* studio;
    int releaseYear;
} VideoGame;

typedef struct TreeNode {
    VideoGame* data;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;
```

**Pas cu pas:**
- `VideoGame` = datele utile: un ID (unsigned int), titlu, studio, an.
- `TreeNode` = nodul din arbore: pointer la datele unui joc + 2 pointeri (`left`, `right`).
- `data` e `VideoGame*` (pointer) — nodul nu contine struct-ul inline, ci un pointer la el.

**Cheie de sortare in BST:** `gameID`. Stanga → ID mai mic, dreapta → ID mai mare.

**Diferenta vs lista:** in loc de un singur pointer `next`, ai 2 pointeri (`left` si `right`).

---

## 2. `printGame` — afisare

```c
void printGame(const VideoGame* game) {
    printf("[%u] %s - %s (%d)\n", game->gameID, game->title, game->studio, game->releaseYear);
}
```

Format: `[105] Elden Ring - FromSoftware (2022)`.

---

## 3. `insert` — inserare recursiva

```c
void insert(TreeNode** root, VideoGame* game) {
    if (*root == NULL) {
        TreeNode* newNode = malloc(sizeof(TreeNode));
        newNode->data = game;
        newNode->left = NULL;
        newNode->right = NULL;
        *root = newNode;
    }
    else if (game->gameID < (*root)->data->gameID) {
        insert(&(*root)->left, game);
    }
    else {
        insert(&(*root)->right, game);
    }
}
```

**Pas cu pas:**

**Caz de baza — loc liber, creezi nodul:**
```c
if (*root == NULL) {
    TreeNode* newNode = malloc(sizeof(TreeNode));
    newNode->data = game;
    newNode->left = NULL;
    newNode->right = NULL;
    *root = newNode;
}
```
Aloci nodul, ii dai pointerul la `game` si setezi copiii la NULL.
`*root = newNode` — atribui in pointerul parintelui (sau radacina daca e primul nod).

**Recurgie pe stanga sau dreapta:**
```c
else if (game->gameID < (*root)->data->gameID) {
    insert(&(*root)->left, game);
}
else {
    insert(&(*root)->right, game);
}
```

**De ce `TreeNode**`?** Trebuie sa modifici `parent->left` sau `parent->right`. Cu `TreeNode*` copia locala s-ar pierde la return.

---

## 4. `search` — cautare recursiva

```c
TreeNode* search(TreeNode* root, unsigned int gameID) {
    if (root == NULL) return NULL;

    if (gameID == root->data->gameID) return root;
    else if (gameID < root->data->gameID) return search(root->left, gameID);
    else return search(root->right, gameID);
}
```

**Pas cu pas:**
1. Caz de baza: NULL → nu s-a gasit, returneaza NULL.
2. Egalitate → gasit, returneaza nodul.
3. Mai mic → cauta in stanga, mai mare → cauta in dreapta.

**Complexitate:** O(log n) pe un arbore balansat, O(n) in cel mai rau caz (arbore degenerat).

---

## 5. `findMin` / `findMax`

```c
TreeNode* findMin(TreeNode* root) {
    if (root == NULL) return NULL;
    if (root->left == NULL) return root;
    return findMin(root->left);
}

TreeNode* findMax(TreeNode* root) {
    if (root == NULL) return NULL;
    if (root->right == NULL) return root;
    return findMax(root->right);
}
```

**Idee:** minimul e mereu cel mai din stanga (continua pe `left` pana nu mai poti). Maximul — cel mai din dreapta.

**Folosit in `deleteNode`** pentru a gasi in-order successorul.

---

## 6. `height` si `countNodes`

```c
int height(TreeNode* root) {
    if (root == NULL) return 0;
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

int countNodes(TreeNode* root) {
    if (root == NULL) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}
```

**`height`:** recursiv, returnezi `1 + max(inaltime_stanga, inaltime_dreapta)`. Identic cu `treeHeight` din AVL.

**`countNodes`:** parcurgi tot arborele, numeri fiecare nod = 1 + stanga + dreapta.

---

## 7. `deleteNode` — stergere cu 3 cazuri

```c
void deleteNode(TreeNode** root, unsigned int gameID) {
    if (*root == NULL) { printf("Game with ID %u not found.\n", gameID); return; }

    if (gameID < (*root)->data->gameID)      deleteNode(&(*root)->left, gameID);
    else if (gameID > (*root)->data->gameID) deleteNode(&(*root)->right, gameID);
    else {
        // Caz 1: frunza
        // Caz 2a: doar copil drept
        // Caz 2b: doar copil stang
        // Caz 3: 2 copii — inlocuieste cu in-order successor
    }
}
```

**Cele 3 cazuri:**

**Caz 1 — frunza (fara copii):**
```c
if ((*root)->left == NULL && (*root)->right == NULL) {
    free((*root)->data->title);
    free((*root)->data->studio);
    free((*root)->data);
    free(*root);
    *root = NULL;
}
```
Eliberezi tot (string-uri → struct → nod) si setezi pointerul la NULL.

**Caz 2 — un singur copil:**
```c
TreeNode* toDelete = *root;
*root = (*root)->right;  // sau ->left
free(toDelete->data->title); free(toDelete->data->studio);
free(toDelete->data); free(toDelete);
```
Parintele "sare" peste nodul sters, pointand direct la copilul ramas.

**Caz 3 — doi copii:**
```c
TreeNode* successor = findMin((*root)->right);
// Deep copy din successor in nodul curent
free((*root)->data->title); free((*root)->data->studio);
(*root)->data->gameID = successor->data->gameID;
(*root)->data->releaseYear = successor->data->releaseYear;
(*root)->data->title = malloc(...); strcpy(...);
(*root)->data->studio = malloc(...); strcpy(...);
// Sterge succesorul (are cel mult 1 copil)
deleteNode(&(*root)->right, successor->data->gameID);
```
In-order successorul = cel mai mic din sub-arborele drept. Il copiezi in locul nodului de sters, apoi stergi succesorul (care are cel mult un copil drept).

---

## 8. Cele 3 parcurgeri (in cod)

```c
void inorder(TreeNode* root) {
    if (root) { inorder(root->left); printGame(root->data); inorder(root->right); }
}
void preorder(TreeNode* root) {
    if (root) { printGame(root->data); preorder(root->left); preorder(root->right); }
}
void postorder(TreeNode* root) {
    if (root) { postorder(root->left); postorder(root->right); printGame(root->data); }
}
```

| Parcurgere | Ordine | Rezultat |
|-----------|--------|---------|
| inorder | stanga → radacina → dreapta | **sortat crescator dupa ID** |
| preorder | radacina → stanga → dreapta | util pentru clonare |
| postorder | stanga → dreapta → radacina | util pentru free (copii inainte de parinte) |

**Mnemonic:** "Pozitia lui R (radacina) in nume iti spune cand proceseaza."

---

## 9. `printTree` — vizualizare arbore rotit

```c
void printTree(TreeNode* root, int space) {
    if (root) {
        space += 6;
        printTree(root->right, space);
        printf("\n");
        for (int i = 6; i < space; i++) printf(" ");
        printf("[%u]", root->data->gameID);
        printTree(root->left, space);
    }
}
```

**Pas cu pas:**
- `space += 6` — indentare cu 6 spatii per nivel.
- **Dreapta prima** — arborele e afisat rotit cu 90 grade (radacina la stanga, copii la dreapta pe ecran).
- Afiseaza `[gameID]` cu indentare proportionala cu adancimea.

**Apel din main:** `printTree(root, 0)`.

---

## 10. `freeTree` — eliberare recursiva (post-order)

```c
void freeTree(TreeNode* root) {
    if (root) {
        freeTree(root->left);
        freeTree(root->right);
        free(root->data->title);
        free(root->data->studio);
        free(root->data);
        free(root);
    }
}
```

**De ce post-order?** Trebuie sa eliberezi copiii **inainte** de parinte, altfel pierzi accesul la ei.

Eliberezi: string-urile → struct-ul VideoGame → nodul TreeNode.

---

## 11. `loadGames` — citire CSV

```c
int loadGames(const char* filename, TreeNode** root) {
    FILE* f = fopen(filename, "r");
    if (f == NULL) { printf("Error: ..."); return -1; }

    char line[256];
    int count = 0;

    while (fgets(line, sizeof(line), f) != NULL) {
        VideoGame* game = malloc(sizeof(VideoGame));

        char* token = strtok(line, ",");
        game->gameID = (unsigned int)atoi(token);

        token = strtok(NULL, ",");
        game->title = malloc(strlen(token) + 1);
        strcpy(game->title, token);

        token = strtok(NULL, ",");
        game->studio = malloc(strlen(token) + 1);
        strcpy(game->studio, token);

        token = strtok(NULL, ",");
        token[strcspn(token, "\n")] = '\0';
        game->releaseYear = atoi(token);

        insert(root, game);
        count++;
    }

    fclose(f);
    return count;
}
```

**Format games.csv:** `gameID,titlu,studio,an` — ex. `105,Elden Ring,FromSoftware,2022`

**Pas cu pas:**
1. `fopen` + check NULL → return `-1`.
2. `fgets` loop (NU `feof`).
3. 4 campuri: `strtok` de 4 ori. `strcspn` scoate `\n` de pe ultimul camp.
4. `malloc` pentru fiecare string — deep copy.
5. Returneaza numarul de jocuri citite.

---

## 12. `main`

```c
int main() {
    TreeNode* root = NULL;
    int count = loadGames("games.csv", &root);
    // printTree, inorder, preorder, postorder
    // height, countNodes, findMin, findMax
    // search(root, 105)
    // deleteNode(&root, 108)
    freeTree(root);
    return 0;
}
```

Demo-uri in main:
1. **printTree** — vizualizare grafica (rotita cu 90 grade).
2. **Cele 3 parcurgeri** — verifica ca inorder da sortat.
3. **height + countNodes** — info despre structura arborelui.
4. **findMin + findMax** — jocul cu ID-ul cel mai mic/mare.
5. **search** — gaseste jocul cu ID 105.
6. **deleteNode** — sterge radacina (ID 108) si afiseaza arborele dupa.

---

# Functii pentru testul 2

## A. Numarare cu conditie

```c
int countByCondition(TreeNode* root, /* parametri */) {
    if (!root) return 0;
    int count = (/* CONDITIA TA — ex. root->data->releaseYear > 2019 */) ? 1 : 0;
    count += countByCondition(root->left, /* parametri */);
    count += countByCondition(root->right, /* parametri */);
    return count;
}
```

Parcurgi recursiv TOT arborele (nu poti optimiza pe BST ca la search).

## B. Cautare cu conditie pe string

```c
TreeNode* findByTitle(TreeNode* root, const char* title) {
    if (!root) return NULL;
    if (strcmp(root->data->title, title) == 0) return root;
    TreeNode* found = findByTitle(root->left, title);
    if (found) return found;
    return findByTitle(root->right, title);
}
```

Cand conditia NU e pe cheie (nu e pe `gameID`), trebuie sa parcurgi **ambele sub-arbori**.

---

# Capcane

| Capcana | Antidot |
|---------|---------|
| Confuzia `TreeNode*` vs `TreeNode**` | Modifici radacina/copilul → `**`. Doar citesti → `*`. |
| Crezi ca `freeTree` ia `TreeNode**` | NU in acest cod. Ia `TreeNode*` (nu seteaza pointerul la NULL dupa free). |
| Recursivitate pe NULL fara guard | Mereu `if (!root) return ...` la inceputul functiei. |
| Crezi ca BST e mereu balansat | NU. Daca inserezi 101,102,...,115 in ordine → lista inlantuita. AVL fixeaza asta. |
| `feof` anti-pattern | Foloseste `while (fgets(...) != NULL)`. |
| Free in ordine gresita | Post-order: copii intai, parinte la final. |
| search si findMin/findMax iau `TreeNode*`, nu `**` | Returneaza pointer, nu modifica structura → `*` e suficient. |

---

# Self-test (fara cod deschis)

- [ ] Pot desena BST-ul din inserarea: 108, 104, 112, 102, 106, 110, 114.
- [ ] Pot scrie `insert` recursiv in 4 min.
- [ ] Pot scrie `search` in 2 min.
- [ ] Pot scrie `findMin` si `findMax` in 2 min.
- [ ] Pot scrie cele 3 parcurgeri (in/pre/post) in 5 min.
- [ ] Pot scrie `deleteNode` cu cele 3 cazuri in 10 min.
- [ ] Pot scrie `freeTree` post-order in 2 min.
- [ ] Pot explica de ce in-order da elementele sortate.

Daca bifezi 7/8 → esti gata pentru AVL.
