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
felix_ = Students("Felix") # Entrer le nom de l'élèves ici
charles_ = Students("Charles") # Entrer le nom de l'élèves ici
pierre_alex_ = Students("Pierre-Alexandre") # Entrer le nom de l'élèves ici
louis_ = Students("louis")
note_pa = pierre_alex_.Matiere(56, 67) # Les 2 nombres sont les notes reçus dans les différente matière au dessu
note_felix = felix_.Matiere(90, 85) # Les 2 nombres sont les notes reçus dans les différente matière au dessu
note_charles = charles_.Matiere(60, 75)  # Les 2 nombres sont les notes reçus dans les différente matière au dessu
note_louis = louis_.Matiere(80, 60)

# Print des résultat
final_calcul = int((note_felix + note_charles + note_pa + note_louis) / Students.nombre_eleve)
print(f"\nLa moyenne du groupe est de : {final_calcul}%")