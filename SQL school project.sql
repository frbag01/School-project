1. Qual è il "Rendimento Medio" per ogni corso?

Domanda: Classifica i corsi (course) in base al punteggio medio degli esami, mostrando anche il numero totale di studenti per corso.

SELECT course AS corso,COUNT(*) AS studenti,ROUND(AVG(exam_score),2) AS punteggio_medio
FROM exam
GROUP BY course


2. Quale metodo di studio è più efficace per chi frequenta poco?

Domanda: Per gli studenti con una frequenza scolastica (class_attendance) inferiore al 70%, qual è il study_method che garantisce il punteggio medio più alto?


SELECT study_method AS metodo,COUNT(*) AS studenti,ROUND(AVG(exam_score),2) AS punteggio_medio
FROM exam
WHERE class_attendance<70.00
GROUP BY study_method
ORDER BY punteggio_medio DESC
LIMIT 1


3. Analisi dell'impatto delle infrastrutture e internet.

Domanda: Crea una tabella che mostri il punteggio medio incrociando internet_access e facility_rating. Esiste un gap significativo tra chi ha alta qualità delle strutture e chi no?

SELECT internet_access AS accesso_web,facility_rating AS struttura,ROUND(AVG(exam_score),2) AS punteggio_medio
FROM exam
GROUP BY struttura,accesso_web
ORDER BY 
	CASE facility_rating
        WHEN 'high' THEN 1
        WHEN 'medium' THEN 2
        WHEN 'low' THEN 3
    END;



4.Identificazione del "Profilo a Rischio" (Early Warning).

Domanda: Estrai l'elenco dei primi 50 studenti con i punteggi più bassi che hanno contemporaneamente meno di 5 ore di sonno e una qualità del sonno "poor".

SELECT student_id AS studente,sleep_hours AS sonno,sleep_quality AS qualità,ROUND(exam_score,2) AS punteggio
FROM exam
WHERE sleep_hours<5 AND sleep_quality='poor'
ORDER BY punteggio
LIMIT 50


5.Benchmarking dei voti (Percentili).

Domanda: Usa una Window Function per calcolare quanto ogni studente si distanzia dalla media del suo specifico corso (course). Chi sono gli "outperformer" (voto > 20% rispetto alla media del corso)?


WITH exam_avg AS (
    SELECT 
        student_id,
        exam_score AS punteggio,
        AVG(exam_score) OVER (PARTITION BY course) AS punteggio_medio_corso
    FROM exam
)

SELECT *
FROM exam_avg
WHERE punteggio > (punteggio_medio_corso+punteggio_medio_corso/5)
ORDER BY punteggio DESC

