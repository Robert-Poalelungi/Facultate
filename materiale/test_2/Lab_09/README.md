# Lab 09 — AVL Tree (BST auto-balansat) — walkthrough complet

**Pre-requisites:** Lab 08 (BST) — AVL = BST + rotații. Dacă n-ai Lab 08 clar, oprește-te acolo mai întâi.

---

## Concept central in 30 secunde

**Problema BST:** dacă inserezi chei în ordine (101, 102, 103...) arborele devine o **listă înlănțuită** → search O(n).

**Soluția AVL:** după fiecare insert/delete, verificăm **balance factor** la fiecare nod de pe drumul înapoi spre rădăcină. Dacă e ±2, aplicăm o **rotație** care reechilibrează.

**Balance factor = height(dreapta) - height(stânga)**
- `-1, 0, +1` → valid (arbore balansat)
- `-2` → left-heavy → rotație dreapta
- `+2` → right-heavy → rotație stânga

**Rezultat:** height garantat O(log n) → search/insert/delete toate O(log n).

---

## Diferențe față de BST (Lab 08)

| | BST | AVL |
|---|---|---|
| Struct nod | `TreeNode` | `AVLNode` |
| Insert | recursiv simplu | recursiv + `rebalance()` la întoarcere |
| Delete | recursiv simplu | recursiv + `rebalance()` la întoarcere |
| Funcții extra | — | `avlHeight`, `avlBalanceFactor`, `avlRotateLeft`, `avlRotateRight`, `rebalance` |
| Prefix funcții | fără prefix | `avl` prefix |

---

# Cod + walkthrough

## 1. Structuri

```c
typedef struct {
    unsigned int gameID;
    char* title;
    char* studio;
    int releaseYear;
} VideoGame;

typedef struct AVLNode {
    VideoGame* data;
    struct AVLNode* left;
    struct AVLNode* right;
} AVLNode;
```

Identic cu BST dar nodul se numește `AVLNode`. Nu are câmp `height` stocat — îl calculăm la cerere cu `avlHeight()`.

---

## 2. `avlHeight` și `avlBalanceFactor`

```c
int avlHeight(AVLNode* root) {
    if (root == NULL) return 0;
    int leftHeight  = avlHeight(root->left);
    int rightHeight = avlHeight(root->right);
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

int avlBalanceFactor(AVLNode* root) {
    if (root == NULL) return 0;
    return avlHeight(root->right) - avlHeight(root->left);
}
```

**`avlHeight`:** recursiv, returnează `1 + max(stânga, dreapta)`. NULL → 0.

**`avlBalanceFactor`:** `height(dreapta) - height(stânga)`.
- Pozitiv → right-heavy
- Negativ → left-heavy
- `avlPrintTree` afișează bf-ul fiecărui nod pentru debugging

---

## 3. Rotații — singura idee nouă față de BST

### `avlRotateRight` — când stânga e prea înaltă (bf = -2)

```
    (*root)               aux
    /     \              /   \
  aux      C    ->      A   (*root)
  / \                       /    \
 A   B                     B      C
```

```c
void avlRotateRight(AVLNode** root) {
    AVLNode* aux = (*root)->left;
    (*root)->left = aux->right;   // B devine copil stâng al lui root
    aux->right = *root;           // root coboară, devine copil drept al lui aux
    *root = aux;                  // aux devine noua rădăcină
}
```

### `avlRotateLeft` — când dreapta e prea înaltă (bf = +2)

```
  (*root)                   aux
  /     \                  /   \
 A       aux    ->    (*root)   C
         / \           /   \
        B   C         A     B
```

```c
void avlRotateLeft(AVLNode** root) {
    AVLNode* aux = (*root)->right;
    (*root)->right = aux->left;   // B devine copil drept al lui root
    aux->left = *root;            // root coboară, devine copil stâng al lui aux
    *root = aux;
}
```

---

## 4. `rebalance` — cele 4 cazuri

```c
static void rebalance(AVLNode** root) {
    int balance = avlBalanceFactor(*root);

    if (balance == 2) {
        if (avlBalanceFactor((*root)->right) >= 0)
            avlRotateLeft(root);                        // RR — rotație stânga simplă
        else {
            avlRotateRight(&(*root)->right);
            avlRotateLeft(root);                        // RL — rotație dublă
        }
    }

    if (balance == -2) {
        if (avlBalanceFactor((*root)->left) <= 0)
            avlRotateRight(root);                       // LL — rotație dreapta simplă
        else {
            avlRotateLeft(&(*root)->left);
            avlRotateRight(root);                       // LR — rotație dublă
        }
    }
}
```

**Cele 4 cazuri:**

| Caz | bf root | bf copil | Fix |
|-----|---------|----------|-----|
| RR | +2 | copil drept >= 0 | o rotație stânga pe root |
| RL | +2 | copil drept < 0 | rotație dreapta pe copil drept, apoi stânga pe root |
| LL | -2 | copil stâng <= 0 | o rotație dreapta pe root |
| LR | -2 | copil stâng > 0 | rotație stânga pe copil stâng, apoi dreapta pe root |

**Mnemonic:** numele cazului (RR, RL, LL, LR) descrie **forma dezechilibrului**, nu rotația care îl fixează.

---

## 5. `avlInsert` — BST insert + rebalance la întoarcere

```c
void avlInsert(AVLNode** root, VideoGame* game) {
    if (*root == NULL) {
        AVLNode* newNode = malloc(sizeof(AVLNode));
        newNode->data  = game;
        newNode->left  = NULL;
        newNode->right = NULL;
        *root = newNode;
    } else if (game->gameID < (*root)->data->gameID) {
        avlInsert(&(*root)->left, game);
        rebalance(root);
    } else if (game->gameID > (*root)->data->gameID) {
        avlInsert(&(*root)->right, game);
        rebalance(root);
    }
}
```

**Diferența față de BST:** după fiecare apel recursiv, `rebalance(root)` verifică și corectează eventualul dezechilibru **pe drumul înapoi spre rădăcină**.

Duplicate (gameID egal) → ignorate.

---

## 6. `avlDeleteNode` — BST delete + rebalance la întoarcere

Identic cu `deleteNode` din BST (aceleași 3 cazuri: frunză, un copil, doi copii cu in-order successor), cu un singur adaos la final:

```c
if (*root) rebalance(root);
```

Același principiu: după ce am șters recursiv, rebalansăm pe drumul înapoi. Guard-ul `if (*root)` previne apelul pe NULL (cazul frunzei care setează `*root = NULL` și face `return` imediat).

---

## 7. `avlPrintTree` — vizualizare cu balance factor

```c
void avlPrintTree(AVLNode* root, int space) {
    if (root) {
        space += 6;
        avlPrintTree(root->right, space);
        printf("\n");
        for (int i = 6; i < space; i++) printf(" ");
        printf("[%u] (bf:%d)", root->data->gameID, avlBalanceFactor(root));
        avlPrintTree(root->left, space);
    }
}
```

Față de BST, afișează și `(bf:X)` lângă fiecare nod. Util pentru a verifica vizual că arborele e balansat (toți bf în {-1, 0, 1}).

---

## 8. `avlLoadGames` — citire CSV

Identic cu `loadGames` din BST, doar că apelează `avlInsert` în loc de `insert`.

**Format games.csv:** `gameID,titlu,studio,an`

---

## 9. `main`

```c
AVLNode* root = NULL;
int count = avlLoadGames("games.csv", &root);

avlPrintTree(root, 0);          // vizualizare cu bf la fiecare nod
avlInorder(root);               // sortat dupa ID
avlHeight(root);                // inaltime garantata O(log n)
avlCountNodes(root);
avlBalanceFactor(root);         // bf al radacinii (ar trebui sa fie 0 sau +-1)
avlFindMin(root); avlFindMax(root);
avlSearch(root, 105);
avlDeleteNode(&root, 108);
avlFreeTree(root);
```

---

# Functii pentru testul 2

Patternurile sunt identice cu BST — doar schimbi `TreeNode` cu `AVLNode` și prefixezi cu `avl`.

## A. Numarare cu conditie

```c
int avlCountByCondition(AVLNode* root, /* parametri */) {
    if (!root) return 0;
    int count = (/* CONDITIA TA */) ? 1 : 0;
    count += avlCountByCondition(root->left, /* parametri */);
    count += avlCountByCondition(root->right, /* parametri */);
    return count;
}
```

## B. Cautare dupa alt camp (nu cheie)

```c
AVLNode* avlFindByTitle(AVLNode* root, const char* title) {
    if (!root) return NULL;
    if (strcmp(root->data->title, title) == 0) return root;
    AVLNode* found = avlFindByTitle(root->left, title);
    if (found) return found;
    return avlFindByTitle(root->right, title);
}
```

Cand conditia nu e pe `gameID`, parcurgi **ambii sub-arbori**.

---

# Capcane

| Capcana | Antidot |
|---------|---------|
| Uiti `rebalance(root)` dupa recursie | E singura diferenta fata de BST la insert/delete. |
| Confunzi cazul cu rotatia care il fixeaza | RR → rotateLeft. LL → rotateRight. RL/LR → rotatii duble. |
| bf = height(dreapta) - height(stanga) vs invers | Pozitiv = right-heavy = rotateLeft. |
| `avlHeight(NULL)` da 0 | Corect — caz de baza, nu crash. |
| `rebalance` dupa delete cand `*root == NULL` | Guard: `if (*root) rebalance(root)` — nu apelezi pe NULL. |

---

# Self-test (fara cod deschis)

- [ ] Pot explica de ce BST degenerat → O(n) si cum AVL fixeaza asta.
- [ ] Pot desena rotatia dreapta (LL) pe un exemplu simplu in 2 min.
- [ ] Pot desena rotatia dubla LR in 3 min.
- [ ] Pot scrie `avlHeight` si `avlBalanceFactor` in 2 min.
- [ ] Pot scrie `avlRotateLeft` si `avlRotateRight` in 3 min.
- [ ] Pot scrie `rebalance` cu cele 4 cazuri in 5 min.
- [ ] Pot scrie `avlInsert` (= BST insert + rebalance) in 4 min.
- [ ] Pot scrie `avlDeleteNode` cu cele 3 cazuri + rebalance in 10 min.

Daca bifezi 7/8 → stapanesti AVL.
