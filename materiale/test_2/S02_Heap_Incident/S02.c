// S02 - Max-Heap | Incident Response System
// Compilare: gcc S02.c -o S02
// Rulare:   pune incidents.csv langa executabil, apoi ./S02

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================================
// 1. DATA — Incident
// ============================================================

typedef struct {
    int id;
    char* title;
    char* affectedSystem;
    int severity;
    int responseTime;
} Incident;

void printIncident(Incident* i) {
    printf("[%d] %s | %s | Severity: %d | Response: %d min\n",
        i->id, i->title, i->affectedSystem, i->severity, i->responseTime);
}

// ============================================================
// 2. HEAP — max-heap pe vector dinamic (keyed by severity)
// ============================================================

typedef struct {
    Incident* incidents;
    int size;
} Heap;

static void swapIncident(Incident* a, Incident* b) {
    Incident aux = *a;
    *a = *b;
    *b = aux;
}

static void heapify(Heap* heap, int index) {
    int largest = index;
    int left  = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < heap->size && heap->incidents[left].severity > heap->incidents[largest].severity)
        largest = left;

    if (right < heap->size && heap->incidents[right].severity > heap->incidents[largest].severity)
        largest = right;

    if (largest != index) {
        swapIncident(&heap->incidents[largest], &heap->incidents[index]);
        heapify(heap, largest);
    }
}

Heap initHeap() {
    Heap heap;
    heap.size = 0;
    heap.incidents = malloc(0);
    return heap;
}

void insertHeap(Heap* heap, Incident incident) {
    heap->size++;
    heap->incidents = realloc(heap->incidents, heap->size * sizeof(Incident));

    int index = heap->size - 1;
    heap->incidents[index] = incident;

    int parent = (index - 1) / 2;

    while (index > 0 && heap->incidents[index].severity > heap->incidents[parent].severity) {
        swapIncident(&heap->incidents[index], &heap->incidents[parent]);
        index  = parent;
        parent = (index - 1) / 2;
    }
}

Incident deleteFromHeap(Heap* heap) {
    Incident top = heap->incidents[0];

    heap->incidents[0] = heap->incidents[heap->size - 1];
    heap->size--;
    heap->incidents = realloc(heap->incidents, heap->size * sizeof(Incident));

    heapify(heap, 0);

    return top;
}

Heap buildHeap(Incident* incidents, int size) {
    Heap heap;
    heap.size = size;
    heap.incidents = malloc(size * sizeof(Incident));

    for (int i = 0; i < size; i++)
        heap.incidents[i] = incidents[i];

    for (int i = heap.size / 2 - 1; i >= 0; i--)
        heapify(&heap, i);

    return heap;
}

void printHeap(Heap* heap) {
    for (int i = 0; i < heap->size; i++)
        printIncident(&heap->incidents[i]);
}

void freeHeap(Heap* heap) {
    for (int i = 0; i < heap->size; i++) {
        free(heap->incidents[i].title);
        free(heap->incidents[i].affectedSystem);
    }
    free(heap->incidents);
    heap->incidents = NULL;
    heap->size = 0;
}

// ============================================================
// 3. LOADER — CSV -> Incident -> heap
// ============================================================

int loadIncidents(const char* filename, Heap* heap) {
    FILE* f = fopen(filename, "r");
    if (f == NULL) {
        printf("Error: could not open file '%s'\n", filename);
        return -1;
    }

    char line[256];
    int count = 0;

    while (fgets(line, sizeof(line), f) != NULL) {
        Incident incident;

        char* token = strtok(line, ",");
        incident.id = atoi(token);

        token = strtok(NULL, ",");
        incident.title = malloc(strlen(token) + 1);
        strcpy(incident.title, token);

        token = strtok(NULL, ",");
        incident.affectedSystem = malloc(strlen(token) + 1);
        strcpy(incident.affectedSystem, token);

        token = strtok(NULL, ",");
        incident.severity = atoi(token);

        token = strtok(NULL, ",");
        token[strcspn(token, "\n")] = '\0';
        incident.responseTime = atoi(token);

        insertHeap(heap, incident);
        count++;
    }

    fclose(f);
    return count;
}

// ============================================================
// 4. EXPORT CU FUNCTION POINTER (cerinta 4)
// ============================================================

typedef int (*IncidentFilter)(Incident*);

Incident** exportIncidents(Heap* heap, IncidentFilter filter, int* count) {
    *count = 0;
    Incident** result = NULL;

    for (int i = 0; i < heap->size; i++) {
        if (filter(&heap->incidents[i])) {
            (*count)++;
            result = realloc(result, (*count) * sizeof(Incident*));
            result[*count - 1] = &heap->incidents[i];
        }
    }

    return result;
}

static int severityThreshold = 7;
static char* systemFilter = "Database";

int filterBySeverity(Incident* i) {
    return i->severity > severityThreshold;
}

int filterBySystem(Incident* i) {
    return strcmp(i->affectedSystem, systemFilter) == 0;
}

// ============================================================
// 5. MAIN
// ============================================================

int main() {

    // --- Cerinta 1: incarcare din CSV + print heap ---
    printf("=== Cerinta 1: Incarcare din CSV ===\n");
    Heap heap = initHeap();
    int count = loadIncidents("incidents.csv", &heap);
    if (count < 0) return 1;
    printf("Loaded %d incidents:\n", count);
    printHeap(&heap);
    printf("\n");

    // --- Cerinta 2: buildHeap din array hardcodat ---
    printf("=== Cerinta 2: BuildHeap din array hardcodat ===\n");

    Incident hardcoded[] = {
        {11, "CPU overload on prod",     "Application Server", 6, 20},
        {12, "Ransomware detected",      "Endpoint",           10, 2},
        {13, "API rate limit exceeded",  "API Gateway",        5, 35},
        {14, "Root access attempt",      "Auth Service",       9, 7},
        {15, "Backup job failed",        "File Storage",       4, 60}
    };

    int hardcodedSize = sizeof(hardcoded) / sizeof(Incident);
    Heap heap2 = buildHeap(hardcoded, hardcodedSize);

    printf("Heap built from hardcoded array:\n");
    printHeap(&heap2);
    printf("\n");

    freeHeap(&heap2);

    // --- Cerinta 3: extrage pana cand severity < threshold ---
    printf("=== Cerinta 3: Extrage pana cand severity < 8 ===\n");

    int threshold = 8;
    printf("Extracting all incidents with severity >= %d:\n\n", threshold);

    while (heap.size > 0 && heap.incidents[0].severity >= threshold) {
        Incident extracted = deleteFromHeap(&heap);
        printf("Extracted: ");
        printIncident(&extracted);
        free(extracted.title);
        free(extracted.affectedSystem);
        printf("Heap state:\n");
        printHeap(&heap);
        printf("\n");
    }

    // --- Cerinta 4: export cu function pointer ---
    printf("=== Cerinta 4: Export cu function pointer ===\n");

    int outCount = 0;

    // Filtru 1: severity > 7
    severityThreshold = 7;
    Incident** highSeverity = exportIncidents(&heap, filterBySeverity, &outCount);
    printf("Incidents with severity > %d (%d found):\n", severityThreshold, outCount);
    for (int i = 0; i < outCount; i++)
        printIncident(highSeverity[i]);
    free(highSeverity);
    printf("\n");

    // Filtru 2: affectedSystem == "Database"
    systemFilter = "Database";
    Incident** dbIncidents = exportIncidents(&heap, filterBySystem, &outCount);
    printf("Incidents affecting '%s' (%d found):\n", systemFilter, outCount);
    for (int i = 0; i < outCount; i++)
        printIncident(dbIncidents[i]);
    free(dbIncidents);

    freeHeap(&heap);
    return 0;
}
