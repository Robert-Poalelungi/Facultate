# Facultate

Conținutul fiecărei materii este pe un **branch** separat. Schimbă branch-ul (dropdown-ul `main` din colțul stânga sus) ca să vezi materialele.

## Branch-uri disponibile

- [`SDD`](../../tree/SDD) — Structuri de Date
- [`DSAD`](../../tree/DSAD) — Dezvoltare Software Pentru Analiza De Date
- [`PAW`](../../tree/PAW) — Programarea aplicațiilor Windows
<!-- BRANCHES_END -->

## Cum funcționează

Fiecare branch e independent (orphan branch — istoric separat). Asta înseamnă că:
- Nu apare README-ul de pe `main` în branch-urile de materii
- Fiecare materie e izolată
- Pentru a clona o materie specifică:
  ```
  git clone -b SDD https://github.com/Robert-Poalelungi/Facultate.git
  ```

## Adăugare materie nouă

**Varianta rapidă — script:**

```bash
./add-materie.sh POO /c/Users/Robert/Desktop/poo "Programare Orientată Obiect"
```

Argumente:
1. **Numele branch-ului** (ex. `POO`, `BD`, `Algo`)
2. **Folderul sursă** cu conținutul materiei
3. **Numele complet** (opțional, doar pentru README)

Scriptul verifică că branch-ul nu există deja, comută pe main, creează orphan branch, copiază conținutul, commit + push automat.

**Varianta manuală** (dacă preferi pas cu pas):

```bash
git checkout main
git checkout --orphan <nume-materie>
git rm -rf .
# copiezi conținutul materiei aici
git add .
git commit -m "Initial <materie>"
git push -u origin <nume-materie>
```
