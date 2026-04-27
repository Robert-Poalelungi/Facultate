# Facultate

Conținutul fiecărei materii este pe un **branch** separat. Schimbă branch-ul (dropdown-ul `main` din colțul stânga sus) ca să vezi materialele.

## Branch-uri disponibile

- [`sdd`](../../tree/sdd) — Structuri de date

## Cum funcționează

Fiecare branch e independent (orphan branch — istoric separat). Asta înseamnă că:
- Nu apare README-ul de pe `main` în branch-urile de materii
- Fiecare materie e izolată
- Pentru a clona o materie specifică:
  ```
  git clone -b sdd https://github.com/Robert-Poalelungi/Facultate.git
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
