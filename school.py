#1.Quali variabili guidano davvero il successo? (Correlation Heatmap)

#Task: Crea una heatmap di correlazione tra ore di studio, frequenza, ore di sonno e punteggio finale. Qual è il driver principale?


from datasets.exceptions import DefunctDatasetError
# Importing Libraries
import ast
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns # Import seaborn for enhanced plotting

# To load a local file, you first need to upload it to your Colab environment.
# You can do this by clicking the folder icon on the left panel, then the upload icon.
# Once uploaded, the file will be in the /content/ directory.

# If the file 'Exam_Score_Prediction.csv' has been uploaded to the Colab session,
# you can load it using its relative path.


df = pd.read_csv('Exam_Score_Prediction.csv')
df=df.dropna(how='all')
dfcorr=df.loc[:,['study_hours','class_attendance','sleep_hours','exam_score']].reset_index(drop=True)
corrdata=dfcorr.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corrdata, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


#2.L'impatto della difficoltà dell'esame sulla distribuzione dei voti.

#Task: Usa un KDE Plot (distribuzione) per confrontare i punteggi ottenuti in esami "Hard", "Moderate" ed "Easy". La difficoltà sposta la media o aumenta solo la varianza?



sns.kdeplot(data=df, x="exam_score",fill=True,hue="exam_difficulty")
plt.title("Exam Score Distribution")
plt.xlabel("Exam Score")
plt.ylabel("Density")
plt.show()









#3. Il "Sonno vs Studio": Esiste un punto di rendimento decrescente?

#Task: Crea un JointPlot o uno Scatter Plot tra study_hours e exam_score. Usa il colore per indicare sleep_quality. Troppa fatica senza sonno peggiora i risultati?

# Importing Libraries
import ast
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# To load a local file, you first need to upload it to your Colab environment.
# You can do this by clicking the folder icon on the left panel, then the upload icon.
# Once uploaded, the file will be in the /content/ directory.

# If the file 'Exam_Score_Prediction.csv' has been uploaded to the Colab session,
# you can load it using its relative path.

colori={'poor':'red','average':'yellow','good':'green'}

df = pd.read_csv('Exam_Score_Prediction.csv')
df=df.dropna(how='all')
df=df[df['class_attendance']>70].copy()
dfm=df[df['gender']=='male'].copy()
dff=df[df['gender']=='female'].copy()


dff.plot(kind='scatter',x='study_hours',y='exam_score',color=dff['sleep_quality'].apply(lambda x: colori[x]))
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Scatter Plot of Study Hours vs Score for Female Students')


dfm.plot(kind='scatter',x='study_hours',y='exam_score',color=dfm['sleep_quality'].apply(lambda x: colori[x]))
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Scatter Plot of Study Hours vs Score for Male Students')

plt.tight_layout()
plt.show()

#4.Task: Visualizza la distribuzione dei voti per ogni study_method. Quale metodo ha meno "outliers" negativi (risultati più stabili)?


method_list=df['study_method'].unique().tolist()
method=[df[df['study_method']==m]['exam_score'] for m in method_list]
plt.boxplot(method,labels=method_list,vert=False)
plt.xlabel('Exam Score')
plt.title('Exam Score Distribution by Study Method')
plt.show()

#5.Analisi demografica e di genere 
#Task: Crea un bar chart categorico che mostri il punteggio medio per Genere ed Età. Esistono differenze statisticamente significative o il rendimento è uniforme?


df=df[df['gender'].isin(['male','female'])]
# Calculate mean exam score by age and gender
mean_scores_by_age_gender = df.groupby(['age', 'gender'])['exam_score'].mean().reset_index()

plt.figure(figsize=(12, 7)) # Adjust figure size for better readability

# Create a grouped bar plot using seaborn
sns.barplot(x='age', y='exam_score', hue='gender', data=mean_scores_by_age_gender, palette={'male': 'blue', 'female': 'pink'})

plt.title('Mean Exam Score by Age and Gender')
plt.xlabel('Age')
plt.ylabel('Mean Exam Score')
plt.legend(title='Gender')
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a grid for better readability
plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()
