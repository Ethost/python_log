import mysql.connector 

def connection_bdd():
    i=0
    while i<3:
        try:
            mdp=str(input("\n\t [+] Entrer le mot de passe de connexion à la base de donnée. ({} essai restant)\n\t\t>".format(3-i)))

            mydb = mysql.connector.connect(
            host="192.168.50.151",
            user="ciscolog",
            password=mdp,
            database="customer",
            auth_plugin="sha256_password"
            )

            return mydb
        
        except:
            print("\n\t [!] Vous avez entré un mauvais mot de passe.\n")
            if i==2:
                exit()
        
        i+=1


def listing():
    check=0
    customercode=input("\n\t [+] Entrer le customer code: \n\t\t> ")
    
    db=connection_bdd()
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM hosts")
    myresult = mycursor.fetchall()

    for x in myresult:
        if customercode == x[1]:
            print("\n\t\t -",x[1],':\n\t\t\t Nom:',x[2],'\n\t\t\t IP:',x[3])
            check=1

        if check != 1:
            print("\n\t [!] Le customer code entré n'est pas dans la base de donnée.\n\t\t-> '{}'".format(x[1]))

def repeat():
    REPEAT=input("\n\t [+] Voulez-vous recommencer le script? (oui/non) \n\t\t>")
    return REPEAT

def time(path):
    timechoose=[None]*2
    try:
        timechoose[0]=int(input("\n\t [+] Entrer la première heure : \n\t\t> "))
        timechoose[1]=int(input("\n\t [+] Entrer la deuxième heure : \n\t\t> "))

        if timechoose[1] > timechoose[0]:
            tmp=timechoose[0]
            timechoose[0]=timechoose[1]
            timechoose[1]=tmp

        with open(path, 'r') as fl:                        
            for line in fl.readlines() :                  
                parsing=line.split(";")
                time=parsing[2].split(':')
                HOUR=int(time[0])
                if HOUR >= timechoose[1] and HOUR < timechoose[0]:
                    goodprint(parsing)
    except:
        print("\n\t [!] Vous n'avez pas rentré un nombre.")

def goodprint(parsing):
    i=0
    print("\n--START--")
    for i in range(5):
        severity="Severity: "+parsing[0]
        date="Date: "+parsing[1]
        time="Time: "+parsing[2]
        host="Host: "+parsing[3]
        msg="Message: "+parsing[4]

        switcher = {
                    0: severity,
                    1: date,
                    2: time,
                    3: host,
                    4: msg
            }
        print(switcher.get(i))

        i+=1

def pathlog():
    check=0
    path=""
    customercode=input("\n\t [+] Entrer le customer code: \n\t\t> ")
    name=input("\n\t [+] Entrer le nom de l'appareil(RT1,SW1..): \n\t\t> ")
    date = input("\n\t [+] Entrer la date de logs recherché (02/19..): \n\t\t> ")
    date = str(date)
    liste = date.split("/")
    month = liste[0]
    day = liste[1]

    db=connection_bdd()
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM hosts")
    myresult = mycursor.fetchall()

    for x in myresult:
        if customercode == x[1]:
            if name == x[2]:
                path="/var/log/cisco/" + x[3] + "/" + month + "/" + day + "/compacte_cisco.log"
                check=1

    if check!=1:
        print("\n\t [!] Aucune donnée pour le client '{}' à l'appareil '{}' en date du {}/{}\n".format(customercode,name,month,day))
        exit()

    return path

def main():
    choose=0
    while choose==0:
        print("\n\t [+] Choisissez l'une des options suivantes(1,2..):\n")
        print("\t\t |> 1. Afficher la liste des appareils d'un client.")
        print("\t\t |> 2. Afficher toutes les logs d'un appareils cisco.")
        print("\t\t |> 3. Afficher les logs d'une heure d'un appareils cisco.")
        print("\t\t |> 4. Sortir.")

        try:
            choose=int(input("\n\t\t -> "))
        except Exception as e:
                print('Error: %s' %(e))

        if choose == 1:
            listing()
        elif choose == 2:
            path=pathlog()
            try:
                with open(path, 'r') as fl:
                    for line in fl.readlines() :
                        parsing=line.split(";")

                        goodprint(parsing)
            except Exception as e:
                print('Error: %s' %(e))
        
        elif choose==3:
            path=pathlog()
            time(path)

        elif choose==4:
            exit()
            
        else:
            print("\t\n [!] Vous n'avez pas choisis l'une des options afficher.")
        
        if repeat()=='oui':
            main()
        else:
            exit()

main()