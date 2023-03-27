import sqlite3
conn = sqlite3.connect("marie.db")
cur = conn.cursor()

def create_table():
    cur.execute(
        "CREATE TABLE contact(id integer primary key autoincrement, prenom text,nom text, email text UNIQUE, telephone str UNIQUE, adresse text)"
    )
create_table()
conn.commit()



class Contact:
    def __init__(self, prenom: str = "", nom: str = "", email: str = "", telephone: str = "", adresse: str = ""):
        print("Initialisation de l'instance", self)
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.telephone = telephone
        self.adresse = adresse


    def ajouter_contact(self, prenom, nom, email, telephone, adresse):
        req = ('''INSERT INTO contact(prenom, nom, email, telephone, adresse)
                                VALUES (?, ?, ?, ?, ?)''')
        cur.execute(req, (prenom, nom, email, telephone, adresse))
        
    def modifier_contact(self, ancien_numero,nouveau_numero):
        req=('UPDATE contact SET telephone=ancien_numero WHERE telephone = nouveau_numero')
        cur.execute(req,(ancien_numero,nouveau_numero))
        
    def supprimer_contact(self, sup):
        req=("DELETE FROM contact WHERE id = ?")
        cur.execute(req,sup)
        
    def afficher_tous_contacts(self):
        req=("SELECT * FROM contact")
        cur.execute(req)
        
    def afficher_un_contact(self, telephone):
        req=("SELECT * FROM contact WHERE telephone = ?", )
        cur.execute(req, telephone)
       
        
       

personne = Contact()
prenom = input("veuillez donnez votre prenom svp: ")
nom = input("veuillez donnez votre nom svp: ")
email = input("veuillez donnez votre email svp: ")
telephone = input("veuillez donnez votre numero telephone svp: ")
adresse = input("veuillez donnez votre adresse svp:")
personne.ajouter_contact(prenom, nom, email, telephone, adresse)
print("Contact ajouté avec succès !")
conn.commit()


modifier = Contact()
ancien_numero = int(input('donnez votre ancien numero: '))
nouveau_numero = int(input("donnez votre nouveau numero"))
modifier.modifier_contact(ancien_numero,nouveau_numero)
print("Contact modifié avec succès !")
conn.commit()


supprimer=Contact()
sup=int(input("veuillez donner le numero a supprimer svp: "))
supprimer.supprimer_contact(sup)         
print("Contact supprimé avec succès !")
conn.commit()

afficher=Contact()
personnels= cur.fetchall()
if len(personnels) == 0:
            print("Aucun contact trouvé.")
else:
    for personnel in personnels:
        print(personnel)
afficher.afficher_tous_contacts(personnels)
conn.commit()
        
        
affiche=Contact()
persons = cur.fetchall()
if len(persons) == 0:
    print("Aucun contact trouvé avec ce numéro de téléphone.")
else:
    for person in persons:
        print(person)
        affiche.afficher_un_contact(persons)
        conn.commit()
        

conn.close()