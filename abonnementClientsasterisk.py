import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Récupération des informations du nouveau client
numero = input("Numéro du client : ")
nom = input("Nom du client : ")
prenom = input("Prénom du client : ")
# Ajoutez ici les autres informations du client que vous souhaitez collecter

# Insertion du nouveau client dans la table "clients" avec l'abonnement par défaut
cursor.execute('''
    INSERT INTO clients (numero, nom, prenom, id_abonnement) VALUES (?, ?, ?, ?)
''', (numero, nom, prenom, 1))  # 1 est l'identifiant de l'abonnement par défaut
# Ajoutez ici les autres colonnes et valeurs correspondantes pour le nouveau client

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()

print("Le nouveau client a été ajouté avec succès !")
