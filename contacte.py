import sqlite3
conn = sqlite3.connect("marie.db")
cur = conn.cursor()
#creation de la table contact
def create_table():
    cur.execute(
        "CREATE TABLE contact(id integer primary key autoincrement, prenom text,nom text, email text UNIQUE, telephone text UNIQUE, adresse text)"
    )
create_table()
conn.commit()

#creation de la classe contact
class Contact:
    def __init__(self, prenom: str = "", nom: str = "", email: str = "", telephone: str = "", adresse: str = ""):
    
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.telephone = telephone
        self.adresse = adresse

#creation des methodes de la classe contact
    def ajouter_contact(self, prenom, nom, email, telephone, adresse):
        req = ('''INSERT INTO contact(prenom, nom, email, telephone, adresse)
                                VALUES (?, ?, ?, ?, ?)''')
        cur.execute(req, (prenom, nom, email, telephone, adresse))
        
    def modifier_contact(self, ancien_numero,nouveau_numero):
        cur.execute(
        "UPDATE contact SET telephone = ? WHERE telephone = ?",
        (nouveau_numero, ancien_numero)
    )
    conn.commit()
        
    def supprimer_contact(self):
        req = ('DELETE FROM contact WHERE telephone = 777777777')
        cur.execute(req)
        conn.commit()

        
        
        
    def afficher_tous_contacts(self):
        ma= cur.execute("SELECT * FROM contact").fetchall()
        print(ma)
        
    def afficher_un_contact(self):
        ma= cur.execute("SELECT * FROM contact WHERE telephone = 785350368").fetchone()
        print(ma)

#creation du menu permettant d'afficher les differentes choix
while True:
    print("=======Menu=====")
    print("1 ajouter contact")
    print("2 modifier contact")
    print("3 supprimer contact")
    print("4 afficher liste contact")
    print("5 recherche contact")
    choix = input("entrez le chiffre choisi: ")
    #instanciation de la classe contact
    personne = Contact()
   #choix et methode appelee
    if choix == '1':
        prenom = input("veuillez donnez votre prenom svp: ")
        nom = input("veuillez donnez votre nom svp: ")
        email = input("veuillez donnez votre email svp: ")
        telephone = input("veuillez donnez votre numero telephone svp: ")
        adresse = input("veuillez donnez votre adresse svp:")
        personne.ajouter_contact(prenom, nom, email, telephone, adresse)
        print("Contact ajouté avec succès !")
        conn.commit()
        
    elif choix=='2':
        ancien_numero = int(input("veuillez entrez votre ancien numero"))
        nouveau_numero = int(input("veuillez entrez votre nouveau numero"))
        personne.modifier_contact(ancien_numero, nouveau_numero)
        print("Contact modifié avec succès !")
        conn.commit()
        
    elif choix=='3':
        personne.supprimer_contact()
        print("Contact supprimé avec succès !")
        
    elif choix=='4':
        print("voici la liste de vos contact: ")
        personne.afficher_tous_contacts()
        conn.commit()
        
    elif choix=='5' : 
        print("voici le contact demander: ")
        personne.afficher_un_contact()
        conn.commit()
        
#fermeture de la connexion
    conn.close()