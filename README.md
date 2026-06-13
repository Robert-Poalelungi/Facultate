# DSAD — Date Stiintifice si Analiza Datelor

Repo cu toate materialele pentru materia DSAD.

## Structura

```
Facultate/
├── Materiale/
│   ├── Curs/               # Cursuri oficiale, PDF-uri, note
│   ├── Seminar/            # Exercitii si proiecte de seminar
│   └── Rezolvari/          # Rezolvari personale si modele
├── Subiecte/
│   ├── Examen/             # Subiecte si materiale de examen
│   └── Test_Vinte/         # Subiecte si rezolvare test Vinte
└── Proiecte/               # Proiecte DSAD
```

---

## Materiale/Curs

Materialele teoretice principale:

| Fisier | Continut |
|--------|----------|
| `DSAD Nota 7.pdf` | Template-uri de cod pentru toate cele 5 analize (PCA, EFA, LDA, HCA, CCA) — **cel mai important** |
| `ANALIZE TOT(...).docx` | Ghid complet cu operatii, grafice si cod pentru fiecare analiza |
| `curs.pdf` / `DSAD.pdf` | Cursul oficial |
| `tematica examen.pdf` | Tematica oficiala pentru examen |
| `seminarii+ex.pdf` | Seminarii + exercitii din timpul anului |
| `cursuri_oficiale/` | Cursuri oficiale pe capitole |
| `DSAD/` | Exercitii de seminar (cod Python) |

---

## Materiale/Seminar

Exercitii practice din cadrul seminariilor, organizate pe teme:

- `Analize/` — exemple de analize complete
- `ClusterizareIerarhica/` — HCA (Ward, Complete, Average)
- `Industria_Alimentara/` — dataset aplicatie
- `SEMINARE/` — seminariile numerotate (1.1 → 9-AF, AC, ACP, AD, Cluster...)
- `seminar_extras/` — seminarii din alte grupe (1089, 1097, 1098) + dataset-uri tematice
- `seminar_furtuna/`, `seminar_obretin/` — materiale de la alti profesori
- `dsad_grupe/` — subiecte pe grupe

---

## Materiale/Rezolvari

Rezolvari proprii si modele:

- `EU_S1/`, `EU_S2/` — rezolvarile mele pentru S1 si S2
- `DSAD_EXAMEN/` — rezolvari complete pe tipuri de subiect (SUB_BUGET, SUB_C, SUB_E, SUB_ID, INTREGI)
- `examen_pregatire/` — exercitii de pregatire examen
- `modele_rezolvate/` — modele complete rezolvate
- `git_analize/`, `git_rezolvari/` — rezolvari din Git (alte colege)
- `AC/ACP/AD/ADC/AF toate cele cu Chatul.zip` — rezolvari cu explicatii complete pe fiecare tip de analiza

---

## Subiecte/Examen

```
Examen/
├── materiale/              # DSAD Nota 7.pdf, ANALIZE TOT.docx, note personale
├── README.md               # Ghid complet de analiza (PCA/EFA/LDA/HCA/CCA)
├── Model_subiect_RO.pdf    # Model oficial de subiect
├── subiecte_2022_feb/      # Subiecte din sesiunea februarie 2022 (foto)
├── subiecte_2025/          # Subiecte din 2025 (S8, S9, seria D/E)
│   └── S1_model/           # Model de subiect complet
├── subiecte_2026/          # Subiecte din 2026 (S1-S11)
├── subiecte_zi/            # Subiecte de la forma ZI + seturi de date
└── tutoring/               # Dataset-uri pentru practica (DataSet_34, Industrie, Populatie)
```

Ghidul de rezolvare complet se afla in `Examen/README.md`.

---

## Subiecte/Test_Vinte

Test de parcurs cu profesorul Vinte:

- `subiecte/` — fotografii cu subiectele (subiect_11 → subiect_34)
- `rezolvare_vinte/` — rezolvarea mea (`main.py` + date input)

---

## Proiecte

- `ale-mele/` — proiectele mele pe tipuri de analiza (ACP, Cluster, Discriminanta, Factoriala)
- `proiectDSAD_final/` — proiectul final predat
- `proiect_vechi/` — versiune anterioara a proiectului
- `proiect_dsad/` — varianta alternativa
- `Margineanu_Matei_1091.zip` — exemplu proiect coleg

---

## Tipuri de Analize

| Analiza | Librarie | Cand se foloseste |
|---------|----------|-------------------|
| **PCA** — Componente Principale | `sklearn.decomposition.PCA` | Reducere dimensionalitate, variabile corelate |
| **EFA** — Factoriala | `factor_analyzer` | Identificare factori latenti |
| **LDA** — Discriminanta | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis` | Clasificare grupe cunoscute |
| **HCA** — Clusteri Ierarhici | `scipy.cluster.hierarchy` | Grupare fara etichete, dendrograma |
| **CCA** — Canonica | `scipy.stats` / `numpy` | Relatie intre doua seturi de variabile |

Pentru cod complet vezi `Subiecte/Examen/README.md`.
