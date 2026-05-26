// Lab 10 — Graph (adjacency list, DFS, BFS)
// Compilare: gcc Lab_10.c -o Lab_10
// Rulare:   pune stations.csv si connections.txt langa executabil, apoi ./Lab_10

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ============================================================
// 1. DATA — Station
// ============================================================

typedef struct {
    int id;
    char* name;
    char* line;
} Station;

void printStation(const Station* station) {
    printf("[%d] %s (Line %s)\n", station->id, station->name, station->line);
}

// ============================================================
// 2. GRAPH — lista de adiacenta
// ============================================================
//
// GraphNode  = nod in graf (contine Station + lista de adiacenta)
// AdjNode    = element din lista de adiacenta (pointer la un GraphNode vecin)
//
// Structura:
//   graph -> [GraphNode] -> [GraphNode] -> [GraphNode] -> NULL
//                |                |
//             [AdjNode]        [AdjNode]
//                |                |
//             [AdjNode]          NULL
//                |
//               NULL

typedef struct AdjNode AdjNode;
typedef struct GraphNode GraphNode;

struct AdjNode {
    GraphNode* target;
    AdjNode* next;
};

struct GraphNode {
    Station* data;
    AdjNode* adj;
    GraphNode* next;
};

// ============================================================
// 3. CONSTRUCTIE GRAF
// ============================================================

void insertNode(GraphNode** graph, Station* station) {
    GraphNode* node = malloc(sizeof(GraphNode));
    node->data = station;
    node->adj  = NULL;
    node->next = *graph;
    *graph = node;
}

static void insertAdj(AdjNode** list, GraphNode* target) {
    AdjNode* adj = malloc(sizeof(AdjNode));
    adj->target = target;
    adj->next   = *list;
    *list = adj;
}

GraphNode* findById(GraphNode* graph, int id) {
    while (graph) {
        if (graph->data->id == id) return graph;
        graph = graph->next;
    }
    return NULL;
}

void addEdge(GraphNode* graph, int id1, int id2) {
    GraphNode* n1 = findById(graph, id1);
    GraphNode* n2 = findById(graph, id2);
    if (n1 && n2) {
        insertAdj(&n1->adj, n2);
        insertAdj(&n2->adj, n1);
    }
}

// ============================================================
// 4. AFISARE
// ============================================================

void printGraph(GraphNode* graph) {
    while (graph) {
        printStation(graph->data);
        printf("  -> ");
        AdjNode* adj = graph->adj;
        while (adj) {
            printf("%s", adj->target->data->name);
            if (adj->next) printf(", ");
            adj = adj->next;
        }
        printf("\n");
        graph = graph->next;
    }
}

// ============================================================
// 5. STIVA — folosita de DFS
// ============================================================
//
// DFS (Depth-First Search) — merge cat mai adanc pe un drum,
// inainte sa se intoarca si sa exploreze alte ramuri.
// Foloseste o STIVA: LIFO — ultimul introdus, primul scos.

typedef struct StackNode {
    int id;
    struct StackNode* next;
} StackNode;

static void push(StackNode** top, int id) {
    StackNode* node = malloc(sizeof(StackNode));
    node->id   = id;
    node->next = *top;
    *top = node;
}

static int pop(StackNode** top) {
    StackNode* node = *top;
    int id = node->id;
    *top = node->next;
    free(node);
    return id;
}

// ============================================================
// 6. COADA — folosita de BFS
// ============================================================
//
// BFS (Breadth-First Search) — exploreaza mai intai toti vecinii
// unui nod, inainte sa mearga mai adanc.
// Foloseste o COADA: FIFO — primul introdus, primul scos.

typedef struct QueueNode {
    int id;
    struct QueueNode* next;
} QueueNode;

typedef struct {
    QueueNode* front;
    QueueNode* back;
} Queue;

static void enqueue(Queue* q, int id) {
    QueueNode* node = malloc(sizeof(QueueNode));
    node->id   = id;
    node->next = NULL;
    if (q->back) q->back->next = node;
    else         q->front = node;
    q->back = node;
}

static int dequeue(Queue* q) {
    QueueNode* node = q->front;
    int id = node->id;
    q->front = node->next;
    if (!q->front) q->back = NULL;
    free(node);
    return id;
}

// ============================================================
// 7. PARCURGERI
// ============================================================

void dfs(GraphNode* graph, int startId, int nodeCount) {
    int* visited = calloc(nodeCount + 1, sizeof(int));
    StackNode* stack = NULL;
    push(&stack, startId);

    printf("DFS from node %d:\n", startId);

    while (stack) {
        int id = pop(&stack);
        if (visited[id]) continue;
        visited[id] = 1;

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

void bfs(GraphNode* graph, int startId, int nodeCount) {
    int* visited = calloc(nodeCount + 1, sizeof(int));
    Queue q = {NULL, NULL};
    visited[startId] = 1;
    enqueue(&q, startId);

    printf("BFS from node %d:\n", startId);

    while (q.front) {
        int id = dequeue(&q);
        GraphNode* node = findById(graph, id);
        if (node) {
            printStation(node->data);
            AdjNode* adj = node->adj;
            while (adj) {
                int adjId = adj->target->data->id;
                if (!visited[adjId]) {
                    visited[adjId] = 1;
                    enqueue(&q, adjId);
                }
                adj = adj->next;
            }
        }
    }

    free(visited);
}

// ============================================================
// 8. INCARCARE DIN FISIER + CLEANUP
// ============================================================

int loadGraph(GraphNode** graph, const char* nodesFile, const char* edgesFile) {
    FILE* f = fopen(nodesFile, "r");
    if (!f) {
        printf("Error: could not open '%s'\n", nodesFile);
        return -1;
    }

    char line[256];
    int count = 0;

    while (fgets(line, sizeof(line), f)) {
        Station* s = malloc(sizeof(Station));

        char* token = strtok(line, ",");
        s->id = atoi(token);

        token = strtok(NULL, ",");
        s->name = malloc(strlen(token) + 1);
        strcpy(s->name, token);

        token = strtok(NULL, ",");
        token[strcspn(token, "\n")] = '\0';
        s->line = malloc(strlen(token) + 1);
        strcpy(s->line, token);

        insertNode(graph, s);
        count++;
    }

    fclose(f);

    f = fopen(edgesFile, "r");
    if (!f) {
        printf("Error: could not open '%s'\n", edgesFile);
        return -1;
    }

    while (fgets(line, sizeof(line), f)) {
        char* token = strtok(line, ",");
        int id1 = atoi(token);
        token = strtok(NULL, ",");
        int id2 = atoi(token);
        addEdge(*graph, id1, id2);
    }

    fclose(f);
    return count;
}

void freeGraph(GraphNode* graph) {
    while (graph) {
        AdjNode* adj = graph->adj;
        while (adj) {
            AdjNode* nextAdj = adj->next;
            free(adj);
            adj = nextAdj;
        }
        free(graph->data->name);
        free(graph->data->line);
        free(graph->data);
        GraphNode* next = graph->next;
        free(graph);
        graph = next;
    }
}

// ============================================================
// 9. MAIN
// ============================================================

int main() {

    // --- Incarcare din fisiere ---
    GraphNode* graph = NULL;
    int count = loadGraph(&graph, "stations.csv", "connections.txt");

    if (count < 0) {
        printf("Failed to load graph.\n");
        return 1;
    }

    printf("Loaded %d stations.\n\n", count);

    printf("--- Graph (adjacency list) ---\n");
    printGraph(graph);

    printf("\n--- Depth-First Search from node 1 ---\n");
    dfs(graph, 1, count);

    printf("\n--- Breadth-First Search from node 1 ---\n");
    bfs(graph, 1, count);

    freeGraph(graph);

    // --- Graf hardcodat (fara fisiere) ---
    printf("\n--- Graf hardcodat (5 noduri) ---\n");

    Station s1 = {1, "Alpha", "M1"};
    Station s2 = {2, "Beta",  "M1"};
    Station s3 = {3, "Gamma", "M2"};
    Station s4 = {4, "Delta", "M2"};
    Station s5 = {5, "Epsilon","M3"};

    GraphNode* g2 = NULL;
    insertNode(&g2, &s1);
    insertNode(&g2, &s2);
    insertNode(&g2, &s3);
    insertNode(&g2, &s4);
    insertNode(&g2, &s5);

    addEdge(g2, 1, 2);
    addEdge(g2, 1, 3);
    addEdge(g2, 2, 4);
    addEdge(g2, 3, 4);
    addEdge(g2, 4, 5);

    printf("Adjacency list:\n");
    printGraph(g2);

    printf("\nDFS:\n");
    dfs(g2, 1, 5);

    printf("\nBFS:\n");
    bfs(g2, 1, 5);

    // freeGraph nu apelam — s1..s5 sunt pe stack, nu heap
    // eliberam doar nodurile grafului si adiacentele
    GraphNode* cur = g2;
    while (cur) {
        AdjNode* adj = cur->adj;
        while (adj) { AdjNode* nx = adj->next; free(adj); adj = nx; }
        GraphNode* nx = cur->next;
        free(cur);
        cur = nx;
    }

    return 0;
}
