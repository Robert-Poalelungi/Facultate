# Facultate

Conținutul fiecărei materii este pe un **branch** separat. Schimbă branch-ul (dropdown-ul `main` din colțul stânga sus) ca să vezi materialele.

## Branch-uri disponibile

- [`SDD`](../../tree/SDD) — Structuri de Date

## Cum funcționează

Fiecare branch e independent (orphan branch — istoric separat). Asta înseamnă că:
- Nu apare README-ul de pe `main` în branch-urile de materii
- Fiecare materie e izolată
- Pentru a clona o materie specifică:
  ```
  git clone -b SDD https://github.com/Robert-Poalelungi/Facultate.git
  ```

## Adăugare materie nouă

```bash
git checkout main
git checkout --orphan <nume-materie>
git rm -rf .
# copiezi conținutul materiei aici
git add .
git commit -m "Initial <materie>"
git push -u origin <nume-materie>
```
