
def listing():
    check=0
    CUSTOMERCODE=input("\n\t [+] Entrer le customer code: \n\t\t> ")

    with open('host.txt', 'r') as fl:
                for line in fl.readlines() :
                        if CUSTOMERCODE in line:
                            tmp=line.split("|")
                            print("\n\t\t -",CUSTOMERCODE,':\n\t\t\t Nom:',tmp[1],'\n\t\t\t IP:',tmp[2])
                            check=1
                if check!=1:
                    print("\n\t [!] Le customer code entré n'est pas dans la base de donnée.\n\t\t->", CUSTOMERCODE)

def repeat():
    repeat=input("\n\t [+] Voulez-vous recommencer le script? (oui/non) \n\t\t>")
    return repeat

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
        print("\n\t[!] Vous n'avez pas rentré un nombre.")

def goodprint(parsing):
    i=0
    for i in range(5):
        if i==0:
            print("\n--START--")
            severity="Severity: "+parsing[0]
            print(severity)
        elif i==1:
            date="Date: "+parsing[1]
            print(date)
        elif i==2:
            time="Time: "+parsing[2]
            print(time)  
        elif i==3:
            host="Host: "+parsing[3]
            print(host)
        elif i==4:
            msg="Message: "+parsing[4]
            print(msg)  
        i+=1

def pathlog():
    check=0
    path=""
    tmp=[]
    CUSTOMERCODE=input("\n\t [+] Entrer le customer code: \n\t\t> ")
    NAME=input("\n\t [+] Entrer le nom de l'appareil(RT1,SW1..): \n\t\t> ")
    MOUNTH=input("\n\t [+] Entrer le mois des logs recherché (01,02..): \n\t\t> ")
    DAY=input("\n\t [+] Entrer le jour des logs recherché (1,2..): \n\t\t> ")

    with open('host.txt', 'r') as fl:                        
        for line in fl.readlines() :                  
                if CUSTOMERCODE in line:
                    tmp=line.split("|")
                    if tmp[1]==NAME:
                        path="/var/log/cisco/" + tmp[2].rstrip('\n') + "/" + MOUNTH + "/" + DAY + "/compacte_cisco.log"
                        check=1
    if check!=1:
        print("\n\t [!] Aucune donnée pour",CUSTOMERCODE,"à l'appareil",NAME,"en date du %s/%s" %(MOUNTH, DAY))


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