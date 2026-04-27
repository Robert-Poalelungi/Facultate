#!/usr/bin/env bash
# Adauga o materie noua ca orphan branch + actualizeaza README pe main si pune push pe ambele.
#
# Usage:
#   ./add-materie.sh <BRANCH_NAME> <SOURCE_FOLDER> <FULL_NAME>
#
# Exemplu:
#   ./add-materie.sh POO /c/Users/Robert/Desktop/poo "Programare Orientata Obiect"
#
# Ce face:
# 1. Verifica ca branch-ul nu exista (local + remote)
# 2. Verifica ca nu ai modificari necomise
# 3. Comuta pe main, creeaza orphan branch nou, copiaza continutul
# 4. Commit + push branch
# 5. Comuta inapoi pe main, adauga linie in README inainte de <!-- BRANCHES_END -->
# 6. Commit + push main

set -e   # iese din script la prima eroare

# === Validare argumente ===
BRANCH="$1"
SOURCE="$2"
FULL_NAME="$3"

if [ -z "$BRANCH" ] || [ -z "$SOURCE" ] || [ -z "$FULL_NAME" ]; then
    echo "Usage: $0 <BRANCH_NAME> <SOURCE_FOLDER> <FULL_NAME>"
    echo ""
    echo "Exemplu:"
    echo "  $0 POO /c/Users/Robert/Desktop/poo \"Programare Orientata Obiect\""
    echo ""
    echo "Toate cele 3 argumente sunt obligatorii (FULL_NAME pentru README)."
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "❌ Eroare: folderul '$SOURCE' nu exista"
    exit 1
fi

# === Verificari de siguranta ===

if [ ! -d ".git" ]; then
    echo "❌ Eroare: nu esti intr-un repo git (lipseste folderul .git)"
    exit 1
fi

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
    echo "❌ Eroare: branch-ul '$BRANCH' exista deja local"
    exit 1
fi

if git ls-remote --heads origin "$BRANCH" 2>/dev/null | grep -q "$BRANCH"; then
    echo "❌ Eroare: branch-ul '$BRANCH' exista deja pe origin"
    exit 1
fi

if ! git diff-index --quiet HEAD --; then
    echo "❌ Eroare: ai modificari necomise. Commit sau stash inainte."
    exit 1
fi

# Verifica ca markerul exista in README
if ! grep -q "<!-- BRANCHES_END -->" README.md 2>/dev/null; then
    echo "❌ Eroare: README-ul de pe main nu contine marker-ul '<!-- BRANCHES_END -->'."
    echo "   Adauga marker-ul manual sub ultima linie de branch."
    exit 1
fi

# === PARTEA 1: Creare branch nou ===

echo ">>> [1/6] Comut pe main..."
git checkout main

echo ">>> [2/6] Creez orphan branch '$BRANCH'..."
git checkout --orphan "$BRANCH"

echo ">>> [3/6] Curat staging si untracked, apoi copiez din '$SOURCE'..."
git rm -rf . > /dev/null 2>&1 || true
# Sterge si fisierele untracked / ignored (ex. practice/ leftover din alte branch-uri)
git clean -fdx > /dev/null 2>&1 || true
cp -r "$SOURCE"/. .

# Daca sursa nu are .gitignore, creez unul default ca sa NU se traceze accidental
# practice/, build artifacts, .vs/, etc.
if [ ! -f .gitignore ]; then
    cat > .gitignore <<'EOF'
# Codul de drill local
practice/

# Build artifacts (MSVC / VS)
*.exe
*.obj
*.pdb
*.ilk
*.idb
Debug/
Release/
x64/
.vs/

# Editor / OS
.vscode/
*.swp
.DS_Store
Thumbs.db
EOF
fi

echo ">>> [4/6] Commit + push branch '$BRANCH'..."
git add .
git commit -m "Initial $BRANCH content"
git push -u origin "$BRANCH"

# === PARTEA 2: Update README pe main ===

echo ">>> [5/6] Actualizez README pe main..."
git checkout main

# Insereaza linie noua INAINTE de marker
NEW_LINE="- [\`$BRANCH\`](../../tree/$BRANCH) — $FULL_NAME"

# sed -i pe Windows/Git Bash necesita backup ('') sau direct in-place
# Folosim awk care e mai portabil
awk -v new_line="$NEW_LINE" '
/<!-- BRANCHES_END -->/ {
    print new_line
}
{ print }
' README.md > README.md.tmp && mv README.md.tmp README.md

echo ">>> [6/6] Commit + push README..."
git add README.md
git commit -m "Add $BRANCH branch to README"
git push origin main

echo ""
echo "✅ Gata! Branch '$BRANCH' creat, push-uit, README actualizat."
echo "   Branch link: https://github.com/Robert-Poalelungi/Facultate/tree/$BRANCH"
echo "   Main:        https://github.com/Robert-Poalelungi/Facultate"
