#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    unsigned int gameID;
    char* title;
    char* studio;
    int releaseYear;
} VideoGame;

void printGame(const VideoGame* game) {
    printf("[%u] %s - %s (%d)\n", game->gameID, game->title, game->studio, game->releaseYear);
}

typedef struct AVLNode {
    VideoGame* data;
    struct AVLNode* left;
    struct AVLNode* right;
} AVLNode;

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

void avlRotateRight(AVLNode** root) {
    AVLNode* aux = (*root)->left;
    (*root)->left = aux->right;
    aux->right = *root;
    *root = aux;
}

void avlRotateLeft(AVLNode** root) {
    AVLNode* aux = (*root)->right;
    (*root)->right = aux->left;
    aux->left = *root;
    *root = aux;
}

static void rebalance(AVLNode** root) {
    int balance = avlBalanceFactor(*root);

    if (balance == 2) {
        if (avlBalanceFactor((*root)->right) >= 0) {
            avlRotateLeft(root);
        } else {
            avlRotateRight(&(*root)->right);
            avlRotateLeft(root);
        }
    }

    if (balance == -2) {
        if (avlBalanceFactor((*root)->left) <= 0) {
            avlRotateRight(root);
        } else {
            avlRotateLeft(&(*root)->left);
            avlRotateRight(root);
        }
    }
}

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

AVLNode* avlSearch(AVLNode* root, unsigned int gameID) {
    if (root == NULL)                 return NULL;
    if (gameID == root->data->gameID) return root;
    if (gameID  < root->data->gameID) return avlSearch(root->left,  gameID);
    return                                   avlSearch(root->right, gameID);
}

AVLNode* avlFindMin(AVLNode* root) {
    if (root == NULL)       return NULL;
    if (root->left == NULL) return root;
    return avlFindMin(root->left);
}

AVLNode* avlFindMax(AVLNode* root) {
    if (root == NULL)        return NULL;
    if (root->right == NULL) return root;
    return avlFindMax(root->right);
}

int avlCountNodes(AVLNode* root) {
    if (root == NULL) return 0;
    return 1 + avlCountNodes(root->left) + avlCountNodes(root->right);
}

void avlDeleteNode(AVLNode** root, unsigned int gameID) {
    if (*root == NULL) {
        printf("Game with ID %u not found.\n", gameID);
        return;
    }

    if (gameID < (*root)->data->gameID) {
        avlDeleteNode(&(*root)->left, gameID);
    } else if (gameID > (*root)->data->gameID) {
        avlDeleteNode(&(*root)->right, gameID);
    } else {
        if ((*root)->left == NULL && (*root)->right == NULL) {
            free((*root)->data->title);
            free((*root)->data->studio);
            free((*root)->data);
            free(*root);
            *root = NULL;
            return;
        } else if ((*root)->left == NULL) {
            AVLNode* toDelete = *root;
            *root = (*root)->right;
            free(toDelete->data->title);
            free(toDelete->data->studio);
            free(toDelete->data);
            free(toDelete);
        } else if ((*root)->right == NULL) {
            AVLNode* toDelete = *root;
            *root = (*root)->left;
            free(toDelete->data->title);
            free(toDelete->data->studio);
            free(toDelete->data);
            free(toDelete);
        } else {
            AVLNode* successor = avlFindMin((*root)->right);

            free((*root)->data->title);
            free((*root)->data->studio);
            (*root)->data->gameID      = successor->data->gameID;
            (*root)->data->releaseYear = successor->data->releaseYear;
            (*root)->data->title  = malloc(strlen(successor->data->title)  + 1);
            (*root)->data->studio = malloc(strlen(successor->data->studio) + 1);
            strcpy((*root)->data->title,  successor->data->title);
            strcpy((*root)->data->studio, successor->data->studio);

            avlDeleteNode(&(*root)->right, successor->data->gameID);
        }
    }

    if (*root) rebalance(root);
}

void avlInorder(AVLNode* root) {
    if (root) { avlInorder(root->left); printGame(root->data); avlInorder(root->right); }
}

void avlPreorder(AVLNode* root) {
    if (root) { printGame(root->data); avlPreorder(root->left); avlPreorder(root->right); }
}

void avlPostorder(AVLNode* root) {
    if (root) { avlPostorder(root->left); avlPostorder(root->right); printGame(root->data); }
}

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

void avlFreeTree(AVLNode* root) {
    if (root) {
        avlFreeTree(root->left);
        avlFreeTree(root->right);
        free(root->data->title);
        free(root->data->studio);
        free(root->data);
        free(root);
    }
}

int avlLoadGames(const char* filename, AVLNode** root) {
    FILE* f = fopen(filename, "r");
    if (f == NULL) {
        printf("Error: could not open file '%s'\n", filename);
        return -1;
    }

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

        avlInsert(root, game);
        count++;
    }

    fclose(f);
    return count;
}

int main() {

    AVLNode* root = NULL;
    int count = avlLoadGames("games.csv", &root);

    if (count < 0) {
        printf("Failed to load games.\n");
        return 1;
    }

    printf("Loaded %d games.\n\n", count);

    printf("--- AVL tree visual (balance factors shown) ---\n");
    avlPrintTree(root, 0);

    printf("\n\n--- Inorder traversal (sorted by ID) ---\n");
    avlInorder(root);

    printf("\n--- Tree info ---\n");
    printf("Height: %d\n", avlHeight(root));
    printf("Node count: %d\n", avlCountNodes(root));
    printf("Root balance factor: %d\n", avlBalanceFactor(root));

    AVLNode* minNode = avlFindMin(root);
    AVLNode* maxNode = avlFindMax(root);
    printf("Min ID: ");
    printGame(minNode->data);
    printf("Max ID: ");
    printGame(maxNode->data);

    printf("\n--- Search ---\n");
    unsigned int searchID = 105;
    AVLNode* result = avlSearch(root, searchID);
    if (result) {
        printf("Found: ");
        printGame(result->data);
    } else {
        printf("Game with ID %u not found.\n", searchID);
    }

    printf("\n--- Delete game with ID 108 ---\n");
    avlDeleteNode(&root, 108);
    printf("After deletion:\n");
    avlPrintTree(root, 0);
    printf("\n\n");

    avlFreeTree(root);

    return 0;
}
