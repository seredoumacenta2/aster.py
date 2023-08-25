import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Récupération des informations du compte utilisateur
nom_utilisateur = 'nom_utilisateur'
cursor.execute("SELECT * FROM Utilisateurs WHERE nom_utilisateur = ?", (nom_utilisateur,))
compte_utilisateur = cursor.fetchone()

# Vérification de l'existence du compte utilisateur
if compte_utilisateur is not None:
    # Affichage des informations du compte utilisateur
    print("Informations du compte utilisateur :")
    print("Nom d'utilisateur :", compte_utilisateur[1])
    print("Email :", compte_utilisateur[2])
    print("Autres informations :", compte_utilisateur[3])

    # Modification des informations personnelles
    nouveau_nom = input("Nouveau nom : ")
    nouveau_email = input("Nouvel email : ")
    cursor.execute("UPDATE Utilisateurs SET nom = ?, email = ? WHERE nom_utilisateur = ?", (nouveau_nom, nouveau_email, nom_utilisateur))
    conn.commit()
    print("Informations personnelles mises à jour avec succès.")

    # Gestion des abonnements
    # ...

    # Consultation des factures
    # ...

    # Visualisation de l'historique des appels
    # ...

    # Configuration des préférences
    # ...

else:
    print("Le compte utilisateur n'existe pas.")

# Fermeture de la connexion à la base de données
conn.close()
