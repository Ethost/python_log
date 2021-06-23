#!/usr/bin/python3
#Ethost
#Version 4


############
"""IMPORT"""
############

import mysql.connector 
import os.path
from os import path
from os import system
from os import listdir
import time


##############
"""FONCTION"""
##############

#Authentification puis connection à la base de donnée.
def connection_bdd():
    i=0
    while i<3:
        try:
            mdp=str(input("\n\t [+] Entrer le mot de passe de connexion à la base de donnée. ({} essai restant)\n\t\t>".format(3-i)))       #Demande la saisie du mot de passe pour se connecter à la base de donnée

            mydb = mysql.connector.connect(                                                                                                 #Connexion à la base de donnée.
            host="192.168.50.151",                                                                                                          #Serveur herbergeant la base de donnée.
            user="ciscolog",                                                                                                                #Utilisateurs se connectant à la base de donnée.
            password=mdp,                                                                                                                   #Mot de passe fourni par l'utilisateur
            database="customer",                                                                                                            #Nom de la base de donnée ciblé.
            )

            return mydb                                                                                                                     #Retourne la connexion.
        
        except:
            print("\n\t [!] Vous avez entré un mauvais mot de passe.\n")
            if i==2:                                                                                                                        #Si le 3ème essaie de connexion échoue, alors on quitte le programme.
                demontage_log()
                exit()
        
        i+=1

#Permet de monter les fichiers sur le client.main()                                                       
def montage_log():
    Exist=path.exists('/tmp/cisco')                                                                                                         #Vérifie l'existance du dossier cisco dans /tmp/, retourne True si vrais.
    if Exist == True:                                                                                                                       #Vérifie si le retour est True
        if len(os.listdir('/tmp/cisco')) == 0:                                                                                              #Si le contenue du dossier cisco = 0 (vide) alors on peut télécharger les données.
            print("\n\t [+] Montage des logs dans '/tmp/cisco'")
            os.system("sshfs -o reconnect,IdentityFile=~/.ssh/ciscolog.rsa ciscolog@192.168.50.151:/var/log/cisco /tmp/cisco/")             #Montage des fichiers siué sur le serveur vers notre client. 
            time.sleep(1)
        else:
            print("\n\t [!] Les logs sont déjà montée.")

    else:                                                                                                                                   #Si le dossier cisco n'existe pas alors on le créé.
        print("\n\t [+] Création du fichier '/tmp/cisco'")
        os.system("mkdir -p /tmp/cisco")                                                                                                    #Création du dossier cisco.
        print("\n\t [+] Montage des logs dans '/tmp/cisco'")
        os.system("sshfs -o reconnect,IdentityFile=~/.ssh/ciscolog.rsa ciscolog@192.168.50.151:/var/log/cisco /tmp/cisco/")                 #Montage des fichiers situé sur le serveur vers notre client.
        time.sleep(1)

#Permet de démonter les fichiers qui ont été monté sur le client.
def demontage_log():
    if len(os.listdir('/tmp/cisco')) == 0:                                                                                                  #Si le dossier cisco = 0 (vide) alors le démontage des fichiers a déjà été effectué.
        print("\n\t [!] Les logs sont déjà démontée.\n")
    else:
        print("\n\t [+] Démontage des logs dans '/tmp/cisco'\n")
        os.system("fusermount -u /tmp/cisco/")                                                                                              #Démontage des fichiers

#Permet de lister les informations par "customercode".
def listing():
    check=0
    customercode=input("\n\t [+] Entrer le customer code: \n\t\t> ")
    
    db=connection_bdd()                                                                                                                     #Appel la fonction "connection_bdd" pour nous retourner les paramètres de connection
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM hosts")                                                                                                 #Execute la commande "select * from hosts"
    myresult = mycursor.fetchall()                                                                                                          #Récupère la sortie de la commande

    for x in myresult:                                                                                                                      #Parcours les lignes retournées
        if customercode == x[1]:                                                                                                            #Vérifie que le customercode rentré par l'utilisateur correspond bien à l'un des lignes parcouru.
            print("\n\t\t -",x[1],':\n\t\t\t Nom:',x[2],'\n\t\t\t IP:',x[3])                                                                #Si le customercode correspond, on affiche les informations de ce dernier.
            check=1

        if check != 1:
            print("\n\t [!] Le customer code entré n'est pas dans la base de donnée.\n\t\t-> '{}'".format(x[1]))

#Permet de relancer le script ou de l'arréter.
def repeat():
    REPEAT=input("\n\t [+] Voulez-vous recommencer le script? (oui/non) \n\t\t>")
    return REPEAT

#Permet de choisir une plage horaire afin d'aficher les logs de cettes dernières.
def choosetime(path):
    timechoose=[None]*2
    try:
        timechoose[0]=int(input("\n\t [+] Entrer la première heure : \n\t\t> "))
        timechoose[1]=int(input("\n\t [+] Entrer la deuxième heure : \n\t\t> "))

        if timechoose[1] > timechoose[0]:                                                                                                   #Vérifie que la deuxième heure entré est supérieure à la première
            tmp=timechoose[0]                                                                                                               #Si c'est le cas, alors on va inverser les deux cases.
            timechoose[0]=timechoose[1]
            timechoose[1]=tmp

        with open(path, 'r') as fl:                                                                                                         #Ouvre le fichier en lecture seule
            for line in fl.readlines() :                                                                                                    #Parcours les lignes du fichiers
                parsing=line.split(";")                                                                                                     #Utilise le delimiter ';' pour séparer les colonnes
                time=parsing[2].split(':')                                                                                                  #Sépare les heurs,secondes et minutes du fichiers
                HOUR=int(time[0])                                                                                                           #Stocke l'heure dans une variable
                if HOUR >= timechoose[1] and HOUR < timechoose[0]:                                                                          #Si l'heure stocké est supérieur ou égale à l'heure la plus basse entré par l'utilisateur ET inférieur ou égale à l'heure la plus haute.
                    goodprint(parsing)                                                                                                      #Alors on peut lancer l'affichage de cette log
    except:
        print("\n\t [!] Vous n'avez pas rentré un nombre.")

#Permet d'afficher les logs d'une manière claire.
def goodprint(parsing):
    i=0
    print("\n--START--")
    for i in range(5):
        severity="Severity: "+parsing[0]
        date="Date: "+parsing[1]
        time="Time: "+parsing[2]
        host="Host: "+parsing[3]
        msg="Message: "+parsing[4]

        switcher = {                                                                                                                        #L'équivalent d'un switch case en c, pour afficher
                    0: severity,
                    1: date,
                    2: time,
                    3: host,
                    4: msg
            }
        print(switcher.get(i))                                                                                                              #Print les cases (severity, date...) en fonction de i.

        i+=1

#Défini le chemin des logs qui sera utilisé.
def pathlog():
    check=0
    path=""
    customercode=input("\n\t [+] Entrer le customer code: \n\t\t> ")
    name=input("\n\t [+] Entrer le nom de l'appareil(RT1,SW1..): \n\t\t> ")
    date = input("\n\t [+] Entrer la date de logs recherché (02/19..): \n\t\t> ")
    date = str(date)
    liste = date.split("/")                                                                                                                 #Sépare la date en 2, mois et jours.
    month = liste[0]
    day = liste[1]

    montage_log()                                                                                                                           #Appel la fonction pour monter les logs sur le clients.

    db=connection_bdd()                                                                                                                     #Appel la fonction connection_bdd pour initialiser la connexion.
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM hosts")                                                                                                 #effectue un 'select * from hosts', pour récupérer les informations des clients.
    myresult = mycursor.fetchall()                                                                                                          #Récupère les données demandées et les stock dans une variable.

    for x in myresult:                                                                                                                      #Parcours les résultats ligne par ligne.
        if customercode == x[1]:                                                                                                            #Vérifie que le customercode entré correspond à celui de la ligne x dans la colonne 1.
            if name == x[2]:                                                                                                                #Vérifie que le nom de l'appareil correspond à celui de la ligne x dans la colonne 2.
                path="/tmp/cisco/" + x[3] + "/" + month + "/" + day + "/compacte_cisco.log"                                                 #Concatenation de l'ip de l'appareil(x[3]), du mois, du jours avec le chemin par défaut.
                check=1

    if check!=1:
        print("\n\t [!] Aucune donnée pour le client '{}' à l'appareil '{}' en date du {}/{}\n".format(customercode,name,month,day))
        exit()

    return path


###########
"""MAIN"""
###########

def main():
    choose=0
    while choose==0:
        print("\n\t [+] Choisissez l'une des options suivantes(1,2..):\n")
        print("\t\t |> 1. Afficher la liste des appareils d'un client.")
        print("\t\t |> 2. Afficher toutes les logs d'un appareils cisco.")
        print("\t\t |> 3. Afficher les logs d'une heure d'un appareils cisco.")
        print("\t\t |> 4. Déconnecter les fichiers logs.")
        print("\t\t |> 5. Sortir.")

        try:
            choose=int(input("\n\t\t -> "))
        except Exception as e:
                print('Error: %s' %(e))

        if choose == 1:
            listing()
        elif choose == 2:
            path=pathlog()

            with open(path, 'r') as fl:
                for line in fl.readlines() :
                    parsing=line.split(";")
                    goodprint(parsing)
            
        
        elif choose==3:
            path=pathlog()
            choosetime(path)

        elif choose==4:
            demontage_log()

        elif choose==5:
            demontage_log()
            exit()       

        else:
            print("\t\n [!] Vous n'avez pas choisis l'une des options afficher.")
        
        if repeat()=='oui':
            main()
        else:
            demontage_log()
            exit()

if __name__ == "__main__":
    main()