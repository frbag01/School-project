# Introduzione
Il dataset utilizzato in questo progetto appartiene alla categoria dei dataset sul rendimento scolastico ed accademico (Student Performance & Exam Score Prediction). L'obiettivo principale è analizzare le variabili comportamentali, infrastrutturali e psicofisiche che influenzano il punteggio finale degli studenti durante gli esami.

L'analisi esplora come fattori quali le ore di studio, la frequenza alle lezioni, le abitudini di sonno, i metodi di apprendimento e le strutture scolastiche impattino sul successo accademico, identificando contemporaneamente profili di studenti a rischio e fattori di stabilità delle performance.
# Background
## Metadati principali del dataset
Il dataset comprende 13 variabili che descrivono le caratteristiche demografiche, le abitudini di studio e il contesto ambientale degli studenti:  
- student_id – Identificatore univoco dello studente
- age – Età dello studente
- gender – Genere dello studente 
- course – Corso di studio frequentato 
- study_hours – Ore di studio giornaliere
- class_attendance – Percentuale di frequenza alle lezioni
- internet_access – Disponibilità di connessione internet 
- sleep_hours – Ore di sonno medie per notte
- sleep_quality – Qualità percepita del sonno (poor, average, good)
- study_method – Metodo di studio prevalente (es. coaching, online videos, self-study, group study)
- facility_rating – Valutazione delle infrastrutture scolastiche (low, medium, high)
- exam_difficulty – Livello di difficoltà dell'esame (easy, moderate, hard)
- exam_score – Punteggio finale ottenuto nell'esame (Target Variable)


# Domande di Analisi

### Query & Analisi SQL
1.   Rendimento Medio per Corso: Qual è il punteggio medio degli esami per ciascun corso e come si distribuiscono gli studenti?
2.   Efficienza del Metodo con Bassa Frequenza: Per gli studenti con frequenza scolastica inferiore al 70%, qual è il metodo di studio che garantisce il punteggio medio più alto?
3.   Impatto Infrastrutturale e Digitale: Esiste un gap significativo nel punteggio medio tra chi ha accesso ad internet e diverse qualità delle strutture scolastiche?
4.   Profilo a Rischio (Early Warning): Chi sono gli studenti a maggior rischio di fallimento basati su scarso sonno (< 5 ore) e qualità del sonno scadente ("poor")?
   ### Analisi Statistica e Data Visualization (Python)
5.   Driver del Successo (Correlation Heatmap): Quale variabile tra ore di studio, frequenza e sonno guida maggiormente il punteggio finale?
6.   Difficoltà dell'Esame e Distribuzione (KDE Plot): La difficoltà dell'esame sposta la media dei voti o modifica la varianza?
7.   Sonno vs Studio (Scatter Plot & Rendimenti Decrescenti): Studiare molte ore sacrificando il sonno porta a risultati peggiori?
8.   Stabilità dei Metodi di Studio (Box Plot): Quale metodo di studio presenta meno outliers negativi e garantisce voti più stabili?
9.   Analisi Demografica per Età e Genere (Bar Chart): Esistono differenze di rendimento legate all'età o al genere degli studenti?

#### Dashboard Excel

La dashboard include un riepilogo interattivo dei principali KPI accademici:
- Studenti Totali Analizzati
- Media Punteggio Esami
- Media Ore di Studio e Frequenza
- Distribuzione delle Performance per Corso

# Tools utilizzati
Durante lo sviluppo del progetto sono stati utilizzati diversi strumenti e tecnologie:

- Python per l’analisi dei dati e i test statistici
- SQL per interrogare e aggregare i dati
- Excel per la creazione di una dashboard riassuntiva e interattiva

Per supportare alcune fasi del processo analitico e migliorare l’efficienza nello sviluppo delle query e del codice, è stato utilizzato anche l’ausilio di strumenti di Intelligenza Artificiale.

Il progetto è stato inoltre ispirato ai progetti di data analysis realizzati da Luke Barousse, noto per i suoi contenuti educativi nel campo della data analytics e per i suoi esempi pratici di portfolio basati su SQL, Python e dashboard.

# Analisi
### 1.Rendimento Medio per ogni corso
Classifica i corsi (course) in base al punteggio medio degli esami, mostrando anche il numero totale di studenti per corso
```sql
SELECT course AS corso,COUNT(*) AS studenti,ROUND(AVG(exam_score),2) AS punteggio_medio
FROM exam
GROUP BY course
```

#### Risultati e Insights

| Corso di Studio (`course`) | Numero Studenti | Punteggio Medio (`exam_score`) |
| :--- | :---: | :---: |
| **BBA** | 2.836 | **62,93** |
| **B.Sc** | 2.878 | **62,72** |
| **B.Tech** | 2.798 | **62,65** |
| **BCA** | 2.902 | **62,52** |
| **B.Com** | 2.864 | **62,33** |
| **Diploma** | 2.826 | **62,33** |
| **BA** | 2.896 | **62,11** |

#### Key Takeaways:
- **Omogeneità del Rendimento:** Il punteggio medio tra i vari corsi di studio mostra una **distribuzione estremamente uniforme**, fluttuando in un intervallo ristretto tra **62,11** (BA) e **62,93** (BBA).
- **Equidistribuzione del Campione:** Il numero di studenti per ogni corso è bilanciato (circa 2.800–2.900 studenti per indirizzo), confermando un campionamento omogeneo del dataset.

### 2.Metodo di studio è più efficace per chi frequenta poco
Per gli studenti con una frequenza scolastica (class_attendance) inferiore al 70%, qual è il study_method che garantisce il punteggio medio più alto?

```sql
SELECT study_method AS metodo,COUNT(*) AS studenti,ROUND(AVG(exam_score),2) AS punteggio_medio
FROM exam
WHERE class_attendance<70.00
GROUP BY study_method
ORDER BY punteggio_medio DESC
LIMIT 1
```

#### Risultati e Insights
| Metodo di Studio (`study_method`) | Studenti Non Frequentanti | Punteggio Medio (`exam_score`) |
| :--- | :---: | :---: |
| **Coaching** | **2.033** | **63,61** |

#### Key Takeaways:
- **L'Efficacia del Coaching:** Per gli studenti con una frequenza scolastica critica (inferiore al 70%), il metodo **"Coaching"** si attesta come la strategia d'apprendimento nettamente più efficace, garantendo una media voto di **63,61** su 2.033 studenti.
- **Superamento della Media di Corso (Insight Chiave):** Il dato più rilevante emerge dal confronto con i rendimenti generali: il punteggio medio ottenuto dai non frequentanti che usano il *coaching* (**63,61**) supera perfino la media generale del corso di studio più performante dell'intero dataset (**BBA**, che si attesta a **62,93**).
- **Valore Strategico:** Questo risultato suggerisce che un affiancamento strutturato (coaching) è in grado di **compensare pienamente lo svantaggio della scarsa frequenza alle lezioni**.

### 3.Analisi dell'impatto delle infrastrutture e internet
Tabella che mostra il punteggio medio incrociando internet_access e facility_rating. Esiste un gap significativo tra chi ha alta qualità delle strutture e chi no?

```sql
SELECT internet_access AS accesso_web,facility_rating AS struttura,ROUND(AVG(exam_score),2) AS punteggio_medio
FROM exam
GROUP BY struttura,accesso_web
ORDER BY 
	CASE facility_rating
        WHEN 'high' THEN 1
        WHEN 'medium' THEN 2
        WHEN 'low' THEN 3
    END;
```

#### Risultati e Insights

| Qualità Strutture (`facility_rating`) | Accesso Web (`internet_access`) | Punteggio Medio (`exam_score`) |
| :--- | :---: | :---: |
| **High (Alta)** | **No** | **66,84** |
| **High (Alta)** | **Yes** | **66,04** |
| **Medium (Media)** | **No** | **63,07** |
| **Medium (Media)** | **Yes** | **62,75** |
| **Low (Bassa)** | **No** | **58,65** |
| **Low (Bassa)** | **Yes** | **58,58** |

#### Key Takeaways:
- **Impatto Determinante delle Strutture Scolastiche:** La qualità delle infrastrutture rappresenta un forte driver di rendimento: passare da strutture di bassa qualità (`low`) a strutture di alta qualità (`high`) genera un **incremento medio di circa +8 punti sul punteggio finale** (da ~58,6 a ~66,4).
- **Assenza di Gap Digitale Significativo:** La presenza o l'assenza dell'accesso a Internet non mostra un impatto positivo sui voti; gli studenti senza connessione internet registrano punteggi medi lievemente superiori o del tutto sovrapponibili a chi dispone di accesso web, a parità di livello infrastrutturale.
- **Conclusione:** L'ambiente fisico di apprendimento (aule, laboratori e risorse della struttura) influisce in modo nettamente più marcato sulle prestazioni accademiche rispetto alla sola disponibilità della connessione internet.

### 4.Identificazione del "Profilo a Rischio"
Estrazione dell'elenco dei primi 50 studenti con i punteggi più bassi che hanno contemporaneamente meno di 5 ore di sonno e una qualità del sonno "poor"

```sql
SELECT student_id AS studente,sleep_hours AS sonno,sleep_quality AS qualità,ROUND(exam_score,2) AS punteggio
FROM exam
WHERE sleep_hours<5 AND sleep_quality='poor'
ORDER BY punteggio
LIMIT 50
```

#### Risultati e Insights

#### Key Takeaways:
- **Correlazione Diretta tra Deprivazione del Sonno e Insuccesso:** I primi 50 studenti che combinano un numero di ore di sonno insufficiente (< 5 ore) con una qualità del sonno scadente (`poor`) registrano tutti **punteggi esageratamente bassi, compresi in un intervallo critico tra 19,60 e 24,00**.
- **Impatto della Frizione Psicofisica:** Questi risultati posizionano gli studenti a forte deprivazione di sonno nella fascia di rendimento peggiore dell'intero dataset, dimostrando che il riposo insufficiente costituisce una vera e propria **barriera insuperabile al successo scolastico**.

# PYTHON 

Puoi vedere il codice principale qui: [1] [Python Script](https://github.com/frbag01/School-project/blob/main/school.py)

