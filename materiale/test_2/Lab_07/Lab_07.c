// Lab 07 — Heap (max-heap pe vector)
// Compilare: gcc Lab_07.c -o Lab_07
// Rulare:   pune scheduler.txt langa executabil, apoi ./Lab_07

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================================
// 1. DATA — Task
// ============================================================

typedef struct {
    char* description;
    int priority;
} Task;

void printTask(Task task) {
    printf("[Priority %d] %s\n", task.priority, task.description);
}

// ============================================================
// 2. HEAP — max-heap pe vector dinamic
// ============================================================

typedef struct {
    Task* tasks;
    int size;
} Heap;

static void swapTask(Task* t1, Task* t2) {
    Task aux = *t1;
    *t1 = *t2;
    *t2 = aux;
}

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

Heap initHeap() {
    Heap heap;
    heap.size = 0;
    heap.tasks = malloc(0);
    return heap;
}

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

Task deleteFromHeap(Heap* heap) {
    Task top = heap->tasks[0];

    heap->tasks[0] = heap->tasks[heap->size - 1];
    heap->size--;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));

    heapify(heap, 0);

    return top;
}

void printHeap(Heap* heap) {
    for (int i = 0; i < heap->size; i++) {
        printTask(heap->tasks[i]);
    }
}

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

void freeHeap(Heap* heap) {
    for (int i = 0; i < heap->size; i++) {
        free(heap->tasks[i].description);
    }
    free(heap->tasks);
    heap->tasks = NULL;
    heap->size = 0;
}

// ============================================================
// 3. DELETE BY CONDITION
// ============================================================
//
// Pattern: parcurge vectorul, cand conditia e indeplinita
//   → swap cu ultimul, scade size, heapify pe pozitia curenta
//   → NU incrementa i (noul element de pe pozitia i poate si el sa indeplineasca conditia)
// Cand conditia NU e indeplinita → i++

void deleteByCondition(Heap* heap, int minPriority) {
    int i = 0;
    while (i < heap->size) {
        if (heap->tasks[i].priority < minPriority) {
            free(heap->tasks[i].description);
            heap->tasks[i] = heap->tasks[heap->size - 1];
            heap->size--;
            heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));
            heapify(heap, i);
            // NU i++ — elementul nou de pe pozitia i trebuie verificat
        } else {
            i++;
        }
    }
}

// ============================================================
// 4. MIN-HEAP — aceleasi functii, comparatia inversata
// ============================================================
//
// Diferenta fata de max-heap:
//   heapify:    cauta SMALLEST (< in loc de >)
//   insertHeap: sift-up cu < in loc de >
//   deleteFromHeap: extrage MINIMUL (radacina), structura identica

static void minHeapify(Heap* heap, int index) {
    int smallest = index;
    int left  = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < heap->size && heap->tasks[left].priority < heap->tasks[smallest].priority) {
        smallest = left;
    }

    if (right < heap->size && heap->tasks[right].priority < heap->tasks[smallest].priority) {
        smallest = right;
    }

    if (smallest != index) {
        swapTask(&heap->tasks[smallest], &heap->tasks[index]);
        minHeapify(heap, smallest);
    }
}

void minInsertHeap(Heap* heap, Task task) {
    heap->size++;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));

    int index  = heap->size - 1;
    heap->tasks[index] = task;

    int parent = (index - 1) / 2;

    while (index > 0 && heap->tasks[index].priority < heap->tasks[parent].priority) {
        swapTask(&heap->tasks[index], &heap->tasks[parent]);
        index  = parent;
        parent = (index - 1) / 2;
    }
}

Task minDeleteFromHeap(Heap* heap) {
    Task top = heap->tasks[0];

    heap->tasks[0] = heap->tasks[heap->size - 1];
    heap->size--;
    heap->tasks = realloc(heap->tasks, heap->size * sizeof(Task));

    minHeapify(heap, 0);

    return top;
}

// ============================================================
// 4. LOADER — CSV -> Task -> heap
// ============================================================

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

// ============================================================
// 4. MAIN
// ============================================================

int main() {

    Heap heap = initHeap();
    int count = loadTasks("scheduler.txt", &heap);

    if (count < 0) {
        printf("Failed to load tasks.\n");
        return 1;
    }

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
        {"Fix typo in docs",        3},
        {"Patch SQL injection",     28},
        {"Update dependencies",     6},
        {"Resolve merge conflict",  11},
        {"Rotate API keys",         20},
        {"Restart hung service",    15},
        {"Archive old logs",        2}
    };

    int size = sizeof(unordered) / sizeof(Task);
    Heap heap2 = buildHeap(unordered, size);

    printf("Heap built from unordered array:\n");
    printHeap(&heap2);

    freeHeap(&heap2);

    printf("\n--- deleteByCondition: sterge taskurile cu priority < 10 ---\n\n");

    Heap heap3 = initHeap();
    int count3 = loadTasks("scheduler.txt", &heap3);
    if (count3 > 0) {
        printf("Inainte:\n");
        printHeap(&heap3);
        deleteByCondition(&heap3, 10);
        printf("\nDupa (priority < 10 sterse):\n");
        printHeap(&heap3);
        freeHeap(&heap3);
    }

    printf("\n--- Min-heap demo (extrage in ordine CRESCATOARE) ---\n\n");

    Task tasks2[] = {
        {"Fix typo in docs",        3},
        {"Patch SQL injection",     28},
        {"Update dependencies",     6},
        {"Resolve merge conflict",  11},
        {"Rotate API keys",         20},
        {"Restart hung service",    15},
        {"Archive old logs",        2}
    };

    Heap minHeap = initHeap();
    int size2 = sizeof(tasks2) / sizeof(Task);
    for (int i = 0; i < size2; i++) {
        minInsertHeap(&minHeap, tasks2[i]);
    }

    printf("Processing tasks by priority (ascending):\n");
    while (minHeap.size > 0) {
        Task t = minDeleteFromHeap(&minHeap);
        printf("Processing: ");
        printTask(t);
    }

    freeHeap(&minHeap);

    return 0;
}
