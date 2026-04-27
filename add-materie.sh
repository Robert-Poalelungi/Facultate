#!/usr/bin/env bash
# Adauga o materie noua ca orphan branch in repo-ul Facultate.
#
# Usage:
#   ./add-materie.sh <BRANCH_NAME> <SOURCE_FOLDER> [FULL_NAME]
#
# Exemplu:
#   ./add-materie.sh POO /c/Users/Robert/Desktop/poo "Programare Orientata Obiect"
#
# Ce face:
# 1. Verifica ca branch-ul nu exista (local + remote)
# 2. Verifica ca nu ai modificari necomise
# 3. Comuta pe main, creeaza orphan branch nou, copiaza continutul
# 4. Commit + push
# 5. Iti spune ce sa adaugi in README-ul de pe main

set -e   # iese din script la prima eroare

# === Validare argumente ===
BRANCH="$1"
SOURCE="$2"
FULL_NAME="$3"

if [ -z "$BRANCH" ] || [ -z "$SOURCE" ]; then
    echo "Usage: $0 <BRANCH_NAME> <SOURCE_FOLDER> [FULL_NAME]"
    echo ""
    echo "Exemplu:"
    echo "  $0 POO /c/Users/Robert/Desktop/poo \"Programare Orientata Obiect\""
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "❌ Eroare: folderul '$SOURCE' nu exista"
    exit 1
fi

# === Verificari de siguranta ===

# Esti intr-un repo git?
if [ ! -d ".git" ]; then
    echo "❌ Eroare: nu esti intr-un repo git (lipseste folderul .git)"
    exit 1
fi

# Branch-ul exista deja local?
if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
    echo "❌ Eroare: branch-ul '$BRANCH' exista deja local"
    exit 1
fi

# Branch-ul exista pe remote?
if git ls-remote --heads origin "$BRANCH" 2>/dev/null | grep -q "$BRANCH"; then
    echo "❌ Eroare: branch-ul '$BRANCH' exista deja pe origin"
    exit 1
fi

# Modificari necomise?
if ! git diff-index --quiet HEAD --; then
    echo "❌ Eroare: ai modificari necomise. Commit sau stash inainte."
    exit 1
fi

# === Executie ===

echo ">>> Comut pe main..."
git checkout main

echo ">>> Creez orphan branch '$BRANCH'..."
git checkout --orphan "$BRANCH"

echo ">>> Curat staging area..."
git rm -rf . > /dev/null 2>&1 || true

echo ">>> Copiez continutul din '$SOURCE'..."
# /. la final = copiaza si fisierele ascunse, dar nu folderul in sine
cp -r "$SOURCE"/. .

echo ">>> Stage + commit..."
git add .
git commit -m "Initial $BRANCH content"

echo ">>> Push pe origin..."
git push -u origin "$BRANCH"

echo ""
echo "✅ Branch '$BRANCH' creat si pus pe GitHub."
echo "   Link: https://github.com/Robert-Poalelungi/Facultate/tree/$BRANCH"
echo ""

# === Reminder pentru README ===
if [ -n "$FULL_NAME" ]; then
    echo "📝 Adauga in README-ul de pe main, sub '## Branch-uri disponibile':"
    echo ""
    echo "    - [\`$BRANCH\`](../../tree/$BRANCH) — $FULL_NAME"
    echo ""
    echo "Apoi:"
    echo "    git checkout main"
    echo "    # editeaza README.md"
    echo "    git add README.md && git commit -m \"Add $BRANCH to README\""
    echo "    git push origin main"
else
    echo "📝 Nu ai dat FULL_NAME — adauga manual in README:"
    echo ""
    echo "    - [\`$BRANCH\`](../../tree/$BRANCH) — <numele complet al materiei>"
fi
