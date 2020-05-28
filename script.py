# Les librairies
from inspect import getargspec

# Calcul des note
class Students:
    nombre_eleve = 0
    def __init__(self, name_):
        Students.nombre_eleve += 1 
        self.name_ = name_
    def Matiere(self, french, math):
        self.french = french
        self.math = math
        a = len(getargspec(Students.Matiere).args) - 1
        calcul = (math + french) / a 
        print(f"La note de, {self.name_}, est de: {abs(int(calcul))}%")
        return calcul
    
# Liste des élvèves 
felix_ = Students("Félix") # Le nom de l'élèves ici
charles_ = Students("Charles") 
pierre_alex_ = Students("Pierre-Alexandre")
note_pa = pierre_alex_.Matiere(56, 67) # Les 2 nombres sont les notes reçus dans les différente matière si dessu
note_felix = felix_.Matiere(90, 85) 
note_charles = charles_.Matiere(60, 75)

# Calculation des notes
notes_eleve = (note_felix + note_charles + note_pa)

# Print des résultat
final_calcul = int(notes_eleve / Students.nombre_eleve)
print(f"\nLa moyenne du groupe est de : {final_calcul}%")

###############################
########  Things to do ########
###############################
'''[A ajouter]
Les inputs pour les notes et pour les noms;
Automatiser la calculations des notes;
Optimiser le script
'''