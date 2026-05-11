# S09 — Magazin Online | Observer + Strategy

## Pattern 1: Observer — 5p

**Indicatori în cerință:**
- *„clienții pot fi informați referitor la reduceri"* — notificare la schimbarea stării
- *„poate primi prin email și/sau telefon notificări"* — mai mulți observatori pe același subiect
- *„clientul poate să se dezaboneze"* — subscribe/unsubscribe = Observer
- *„eveniment care să impună notificarea clienților abonați"* — trigger → notificare

**Regula:** „abonare/dezabonare la notificări", „mai mulți clienți notificați la un eveniment" → **Observer**

---

## Pattern 2: Strategy — 5p

**Indicatori în cerință:**
- *„posibilitatea de a plăti prin card bancar sau prin virament bancar"* — comportament interschimbabil
- Clientul alege modalitatea de plată la runtime
- Ambele variante realizează același lucru (plata) dar diferit

**Regula:** „clientul alege între moduri diferite de a face același lucru" → **Strategy**
